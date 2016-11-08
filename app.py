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
    values[0] = page[0]['data-value']
    for x in range(2):
        values[x+1] = page[x+1].get_text()
    return dict(zip(titles,values))

if __name__ == '__main__':
    app.run()

# def writeOut(data):
#     with open("data.json", "w") as writeJSON:
#         json.dump(data,writeJSON)


# page = scrapeData(URL)
# data = getData(page)
# writeOut(data)
