import streamlit as st
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from llama_cpp import Llama

st.set_page_config(page_title="AI Habit Analyzer & OpenHermes Coach", page_icon="💡")

# ---- DEVICE FOR BART (Apple Silicon support) ----
def get_device():
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"

DEVICE = get_device()

# ---- LOAD HABIT DETECTION MODEL ----
@st.cache_resource
def load_classifier():
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
    model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")
    return pipeline("zero-shot-classification", model=model, tokenizer=tokenizer, device=0 if DEVICE == "mps" else -1)

classifier = load_classifier()

HABIT_LABELS = [
    "Exercising", "Healthy eating","junk food", "Sleep", "Procrastination", "Screen time", "Reading",
    "Mindfulness", "Smoking", "skincare","Alcohol consumption", "Hydration", "Journaling", "Negative thinking"
]

# ---- LOAD OpenHermes 2.5 Mistral 7B via llama-cpp-python (from_pretrained HuggingFace) ----
@st.cache_resource
def load_openhermes():
    llm = Llama.from_pretrained(
        repo_id="TheBloke/OpenHermes-2.5-Mistral-7B-GGUF",
        filename="openhermes-2.5-mistral-7b.Q4_K_M.gguf",
        n_ctx=8192,
        n_threads=8,
        n_gpu_layers=20,
        verbose=False
    )
    return llm
 
llm = load_openhermes()

# ---- OpenHermes-powered Suggestion Functions ----
def openhermes_suggest_strategy(habit, entry):
    prompt = (
        f"You are an empathetic, practical life coach. Here is a journal entry:\n\"{entry}\"\n"
        f"You notice the habit '{habit}' within this text. "
        "Suggest a specific, actionable, and supportive strategy to help leave or reduce this habit. "
        "Relate your answer to the content and feelings in the entry if possible. Respond in 2 short sentences, avoid generic advice."
        "\nAnswer:"
    )
    res = llm.create_completion(prompt, max_tokens=120, temperature=0.8, stop=["\n\n", "\nAnswer:"])
    return res["choices"][0]["text"].strip()

def openhermes_suggest_replacement(habit, entry):
    prompt = (
        f"You are an empathetic, practical life coach. Here is a journal entry:\n\"{entry}\"\n"
        f"The person wants to replace the habit '{habit}' with something better. "
        "Suggest one healthy, specific, and context-appropriate new habit, in 1-2 sentences. Reference the entry if meaningful. Avoid generic advice."
        "\nAnswer:"
    )
    res = llm.create_completion(prompt, max_tokens=120, temperature=0.8, stop=["\n\n", "\nAnswer:"])
    return res["choices"][0]["text"].strip()

# ---- UI ----
st.markdown(
    "<h1 style='color:#35A7FF;'>💡 AI Habit Analyzer & OpenHermes Habit Coach</h1>"
    "<p>Paste a journal entry, note, or reflection. The AI will detect habits and suggest how to leave or replace them - all running 100% on your Mac!</p>",
    unsafe_allow_html=True,
)

user_text = st.text_area("Your journal entry or daily note:", height=160)

if st.button("🔍 Analyze & Get Suggestions"):
    if not user_text.strip():
        st.warning("Please enter some text above.")
    else:
        with st.spinner("AI is analyzing your text..."):
            result = classifier(user_text, HABIT_LABELS)
        found = False
        top_habit = None

        st.markdown("### 🌱 Top Habits Found")
        for idx, (label, score) in enumerate(zip(result["labels"], result["scores"])):
            if score > 0.25:
                st.progress(float(score), text=f"{label}: {score*100:.1f}%")
                if idx == 0:
                    top_habit = label
                found = True

        if not found:
            st.info("No strong habits detected in this text.")

        # If we have a top habit, do suggestions
        if top_habit:
            st.markdown("---")
            st.markdown(f"## 💬 OpenHermes Suggestions for **{top_habit}**")

            with st.spinner("AI is considering the best way to leave/change this habit... (OpenHermes 2.5, local)"):
                out1 = openhermes_suggest_strategy(top_habit, user_text)
            st.markdown(f"**👉 How to quit or reduce:**\n> _{out1}_\n")

            with st.spinner("AI is considering a positive habit to replace it... (OpenHermes 2.5, local)"):
                out2 = openhermes_suggest_replacement(top_habit, user_text)
            st.markdown(f"**🌟 Good habit to replace it:**\n> _{out2}_\n")

        st.markdown("---")
        st.markdown("#### 📊 All Scores")
        st.dataframe({
            "Habit": result['labels'],
            "Confidence (%)": [f"{s*100:.1f}" for s in result['scores']]
        }, use_container_width=True)
        st.caption("Tip: Try with longer entries, or tweak the habit labels for your needs!")