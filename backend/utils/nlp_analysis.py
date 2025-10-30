from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of text using TextBlob.
    Returns: (score, label)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 to 1
    
    if polarity > 0.1:
        label = 'positive'
    elif polarity < -0.1:
        label = 'negative'
    else:
        label = 'neutral'
    
    return round(polarity, 3), label