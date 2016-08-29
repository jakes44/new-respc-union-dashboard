from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests
#import json

#Setup

app = Flask(__name__)

URL = "https://www.sunnyportal.com/Templates/PublicPage.aspx?page=6d806835-63f7-4577-ab4c-8116de0ec142"


@app.route('/')
def index():
    response = scrapeData(URL)
    results = getData(response)
    return render_template('index.html', results=results)


def scrapeData(url):
    response = requests.get(url)
    return BeautifulSoup(response.content,"html.parser")

def getData(html):
    titles = ("currentPower", "energy", "co2Avoided")
    page = html.find_all("span", class_="mainValueAmount")
    values = [None for x in range(3)]
    for x in range(3):
        values[x] = page[x].get_text()
    return dict(zip(titles,values))


# def writeOut(data):
#     with open("data.json", "w") as writeJSON:
#         json.dump(data,writeJSON)


# page = scrapeData(URL)
# data = getData(page)
# writeOut(data)
