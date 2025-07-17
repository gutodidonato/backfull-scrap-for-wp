from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route("/tech")
def get_tech_news():
    url = "https://www.theverge.com/tech"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.select("a"): 
        title = item.text.strip()
        articles.append(title)

    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
