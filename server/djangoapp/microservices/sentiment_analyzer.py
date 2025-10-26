from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()


@app.route('/analyze/<string:text>', methods=['GET'])
def analyze_sentiment(text):
    """
    Analyze sentiment of given text
    Returns: positive, neutral, or negative
    """
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return jsonify({"sentiment": sentiment})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
