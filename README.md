# 🧠 HabitHero AI - Your Personal Habit Detective & Coach

Ever written in a journal and wondered "why do I keep doing this to myself?" Or stared at your 3am doom-scrolling session and thought "there's gotta be a better way?" 

Well, I built HabitHero AI because my journal was basically a graveyard of broken promises to myself. Now it's an AI-powered intervention that actually understands context and doesn't just tell you to "drink more water" for every problem.

## 🎯 Live Demo

[Currently living rent-free on my Laptop, making the fans go brrrrr 🔥]

## ✨ Features

### The Core Magic ✅

- **Zero-Shot Habit Detection** - Feed it any journal rambling and watch it spot your habits like a concerned friend who actually pays attention
- **Context-Aware AI Coaching** - Get advice that actually relates to YOUR situation, not copy-paste wellness tips from 2012
- **100% Local Processing** - Your deepest 3am thoughts stay on YOUR machine. No cloud, no cookies, no creepy data harvesting
- **Real-Time Analysis** - Because waiting for results is so Web 2.0

### The Cool Stuff That Makes Me Smile 😊

- **Apple Silicon Optimization** - Uses that fancy M1/M2 chip you paid extra for (finally, a use case!)
- **Confidence Scoring** - See how sure the AI is about your procrastination problem (spoiler: very sure)
- **Habit Progress Bars** - Visual proof that yes, you mention "screen time" in 87% of your entries
- **Empathetic AI Responses** - The LLM actually sounds like it cares (because I prompted it really nicely)
- **No Generic Advice** - Banned phrases include "just breathe" and "have you tried yoga?"
- **Lightning Fast Caching** - Models load once, then stick around like that friend who won't leave your couch

## 📸 Screenshots

[Coming soon after I figure out how to screenshot without showing my actual journal entries 😅]

### The Analysis View
Clean Streamlit interface with calming colors because stressed users don't need aggressive UI

### The Results Dashboard  
Progress bars showing your habits ranked by "how much you need to work on this"

### The AI Coach Responses
Thoughtful, contextual suggestions that don't sound like they came from a fortune cookie

## 🛠️ Tech Stack (For My Fellow Nerds)

- **Frontend**: Streamlit (because who has time for React when you're processing existential crises?)
- **Habit Detection**: BART-Large-MNLI via Hugging Face (zero-shot classification magic ✨)
- **AI Coach**: OpenHermes 2.5 Mistral 7B running locally via llama-cpp (4-bit quantized because RAM is precious)
- **Acceleration**: PyTorch with MPS for Apple Silicon (making those GPU cores earn their keep)
- **Caching**: Streamlit's `@st.cache_resource` (because loading 7B params repeatedly is masochism)
- **Privacy**: Your laptop and nothing else

## 🏃‍♀️ Want to Try It?

**Warning**: This will download ~5GB of AI goodness and turn your Mac into a space heater. Worth it though!

1. **Clone this bad boy**:
```bash
git clone https://github.com/anmolv11n/MyPal
cd MyPal
```

2. **Create a cozy virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows folks: venv\Scripts\activate
```

3. **Install the magic** (grab coffee, maybe lunch too):
```bash
pip install streamlit torch transformers sentencepiece accelerate llama-cpp-python
```

4. **Fire it up**:
```bash
streamlit run Habit_Tracker.py
```

5. **Open your browser** to `http://localhost:8501` and start confessing to the AI

## 💡 The Philosophy Behind This

**Why Local Models?** Because your journal about midnight ice cream binges doesn't need to live on some server in Virginia. Privacy isn't dead, it's just hiding on your SSD.

**Why These Specific Models?** 
- BART for classification because it actually understands nuance
- OpenHermes because it gives advice like a wise friend, not a judgy life coach
- 7B parameters because bigger isn't always better (but 7 billion is pretty good)

**Why Streamlit?** Have you SEEN how fast you can prototype with this thing? Also, I had 48 hours and a dream.

**The Context Thing**: Generic advice is everywhere. "Exercise more!" Yeah thanks, hadn't thought of that. This AI actually reads your entry and goes "Hey, since you mentioned knee pain, here's a sitting meditation practice instead."

## 🎯 What Actually Happens

1. You pour your heart out in the text box
2. BART scans it like a therapist taking notes
3. It spots habits with scientific confidence scores
4. OpenHermes reads the whole thing and crafts two suggestions:
   - How to reduce/quit the problematic habit
   - What healthy habit could replace it
5. Everything happens on your machine in ~3 seconds
6. Your secrets die with your laptop

## 🐛 "Features" I'm Still Calling Features

- Sometimes the AI thinks sarcasm about exercise means you love exercise (working on its humor detection)
- The fans WILL spin up (free white noise machine!)  
- Occasionally suggests "go for a walk" to someone who just wrote about living in a snowstorm (context window issues)
- Uses enough RAM to make Chrome jealous

## 🚀 Where This Is Going (The Webapp Dreams)

### The API-Powered Future 🌟

Since you (my other personality) asked about moving beyond local models, here's the game plan:

**Phase 1: The Hybrid Approach** (Next 2-3 months)
- Keep local models as fallback (privacy-first users love this)
- Add **OPENAI API** for enhanced coaching when users opt-in
- Implement **Cohere** for multilingual support (porque no everyone journals in English)
- Smart routing: Quick stuff locally, complex coaching via API

**Phase 2: The Full Webapp** (3-6 months)
- **Frontend**: Next.js (time to get serious)
- **Backend**: FastAPI + Supabase (PostgreSQL for the win)
- **Auth**: Magic links because passwords are so 2010
- **APIs**: 
  - OpenAI for general analysis (with strict prompting to maintain personality)
  - Anthropic Claude for longer entries (those 100k context windows 👀)
  - Custom fine-tuned SLM for habit detection (training on anonymized community data)

**Phase 3: Community Features** (6-9 months)
- **Habit Circles**: Anonymous groups for similar struggles
- **Success Stories**: Share what worked (with heavy PII scrubbing)
- **Crowdsourced Strategies**: "87% of users who quit doom-scrolling tried this..."
- **Accountability Buddies**: Match with someone on the same journey
- **Weekly Challenges**: Community goals with opt-in leaderboards

### The Technical Evolution 🔧

**Current State** → **Target State**
- Local models → API calls with local fallback
- Single-user → Multi-tenant with auth
- Streamlit → React/Next + FastAPI
- In-memory → PostgreSQL with vector embeddings
- Static habits → ML-learned personal patterns
- Text-only → Voice notes, image journaling

**Why APIs Make Sense**:
- **Cost**: $5/month of API calls > $5000 MacBook Pro thermal throttling
- **Quality**: GPT-4/Claude beat local 7B models (sorry OpenHermes, still love you)
- **Speed**: 100ms API call > 30 seconds of local inference
- **Features**: Streaming responses, better context, multilingual support

**But Keeping Privacy Options**:
- Toggle for "privacy mode" (all local)
- Data deletion on demand
- End-to-end encryption for community features
- Anonymous usage always available
- Python middleware for privacy in prompts

## 🤝 Contributing

Got ideas? Found bugs? Want to add your favorite habit to the list? 

- **Issues**: Be kind, I'm sensitive about my code children
- **Forks**: Take it, make it better, just give credit (karma is real)

## 🙏 Acknowledgments

- My Laptop for not melting (yet)
- The Streamlit team for making prototyping addictive
- Hugging Face for democratizing AI
- OpenHermes for being wise without being preachy
- Coffee for making 3am coding sessions possible
- My journal for being patient while I turned it into a dataset
- You for reading this far (seriously, thank you!)

## 📊 Real Talk: Performance & Limits

**On My M2 Max (your mileage may vary)**:
- First load: ~45 seconds (downloading democracy takes time)
- Subsequent analyses: ~2-3 seconds (thanks, caching!)
- RAM usage: 8-12GB (Chrome: "those are rookie numbers")
- Temperature: Hot enough to warm your coffee ☕

**Current Limits**:
- 15 habits hardcoded (but easily expandable)
- English only (for now - multilingual coming in v2)
- 8K token context (long journals get truncated)
- Single user (your roommate needs their own instance)

## 🎮 Pro Tips for Power Users

1. **Better Prompts = Better Results**: Be specific! "I ate an entire pizza at 2am while crying" gets better advice than "bad eating"

2. **Hack the Habit List**: Edit `HABIT_LABELS` in the code to add your specific struggles. "Revenge bedtime procrastination" anyone?

3. **GPU Goes Brrrr**: Adjust `n_gpu_layers` based on your RAM. More layers = faster but hungrier

4. **Batch Process**: Got years of journals? Write a script to process them all and see your habit evolution (depressing but insightful!)

## 🔮 The Community Vision

**Imagine This**:
- **HabitHero Hub**: Where thousands of anonymous users pool their wisdom
- **The Algorithm of Change**: ML model trained on successful habit changes
- **Streak Street**: Gamification that doesn't feel patronizing  
- **The Confession Wall**: Anonymous shares with supportive responses
- **Habit Matchmaking**: Find your "quit smoking" buddy based on similar contexts

**Community Features Coming**:
```
📍 Location-based challenges ("No phone Tuesdays in SF")
🏆 Milestone celebrations (30 days = custom AI congratulations)
💬 Peer coaching (verified success stories help newbies)
📈 Aggregate insights ("Peak procrastination: Sunday 11pm")
🤝 Accountability contracts (stake your reputation, not money)
```

## 🚧 Current Development Status

### What's Working 💪
- ✅ Habit detection (scary accurate)
- ✅ Contextual AI coaching (actually helpful)
- ✅ Local processing (privacy protected)
- ✅ Apple Silicon optimization (those cores singing)
- ✅ Clean UI (Streamlit doing heavy lifting)

### What's In Progress 🔨
- 🔄 Streaming responses (watching AI think is fun)
- 🔄 Multi-habit analysis (because problems rarely travel alone)
- 🔄 Sentiment tracking (mood ↔️ habits correlation)
- 🔄 Export functionality (your data, your rules)

### What's Planned 📋
- 📅 API integration with fallbacks
- 📅 User accounts & persistence  
- 📅 Community features
- 📅 Mobile app (React Native probably)
- 📅 Browser extension (catch habits in real-time)
- 📅 Wearable integration (Apple Watch habits?)

## 💰 The Business Model (Eventually)

**Free Forever Tier**:
- 50 analyses/month
- Local processing only
- Basic habits
- Community access

**Pro Tier ($5/month)**:
- Unlimited analyses
- API-powered coaching
- Custom habits
- Priority support
- Advanced analytics

**Team/Family Plans**:
- Shared insights (opt-in)
- Group challenges
- Family habit tracking
- Volume pricing

**Your Data = Your Choice**:
- Never sell user data
- Optional anonymized research participation
- Export everything anytime
- Delete = actually deleted

## 🎯 Success Metrics

**For Users**:
- Habits identified accurately
- Actionable advice given
- Privacy maintained
- Progress tracked

**For the Project**:
- Users helped (target: 10K in year 1)
- Habits changed (self-reported)
- Community wisdom generated
- Sustainable without being evil

## 🐞 Bug Bounty

Find a bug? Here's what you get:
- 🐛 Minor bug: Eternal gratitude + mention in commits
- 🐝 Major bug: Above + custom AI coaching prompt
- 🦟 Security issue: Above + first dibs on Pro features
- 🦗 Crash bug: Above + I name a function after you

## 📝 License

MIT License - Because good ideas should spread like good habits

**TL;DR**: Take it, fork it, sell it, just:
- Give credit (karma matters)
- Share improvements (community matters)
- Don't be evil (ethics matter)

## 🌈 Final Thoughts

This started as a weekend project born from frustration with my own habits. Now it's becoming something that could actually help people change their lives, one journal entry at a time.

The tech is cool, but the real magic is in understanding that changing habits isn't about willpower but about awareness, context, and having the right support at the right time.

Whether this stays a local Mac app or becomes the next big wellness platform, the core mission remains: **Help humans understand and improve themselves, privately and compassionately.**

---

**Built with 💜, excessive caffeine, and a genuine belief that AI should help us become better humans**

*P.S. - If you're reading this at 3am procrastinating on something important... the AI is ready to chat about that. Just saying.* 😉

---

### 🎬 Quick Start Video
[Coming soon - after I figure out how to record my screen without exposing my journal entries about my coffee addiction]

### 📧 Contact
- **Email**: work.anmolvohra@gmail.com

### 🏃‍♂️ Join the Journey

⭐ Star this repo (dopamine hit for me, bookmark for you)  
🔀 Fork it (make it yours)  
🐛 Report issues (be gentle)  
💡 Share ideas (be bold)  
🤝 Contribute (be awesome)

**Remember**: Every massive life change started with someone deciding to track their habits. Maybe this little AI assistant will be part of your story.

*Now go journal something. The AI is waiting, and it's surprisingly good at its job.* 🚀
