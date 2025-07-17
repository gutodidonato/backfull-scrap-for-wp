from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/tech")
def get_tech_news():
    url = "https://www.theverge.com/tech"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    for item in soup.select("a"):  
        title = item.text.strip()
        articles.append(title)
        
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
