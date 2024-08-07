from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    headlines = scrape_news()
    return render_template("index.html", headlines=headlines)


def scrape_news():
    url = "https://www.example-news.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []
    for headline in soup.find_all("h3", class_="headline"):
        headlines.append(headline.text)
    return headlines


if __name__ == "__main__":
    app.run(debug=True)
