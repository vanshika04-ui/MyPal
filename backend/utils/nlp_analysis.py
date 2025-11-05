from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of text using TextBlob.
    
    Returns:
        tuple: (sentiment_score, sentiment_label)
        - score: float between -1 (negative) and 1 (positive)
        - label: 'positive', 'negative', or 'neutral'
        
    Note: This is a basic implementation using TextBlob.
    The AI/ML team can replace this with advanced models later.
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