from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
import os
# ✅ Define the Flask app first
app = Flask(__name__)
CORS(app, origins=["https://eval-ease-pu8m.vercel.app/"])

# ✅ Then define your route
@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return jsonify({
        "polarity": sentiment,
        "score": round(polarity, 3)
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

