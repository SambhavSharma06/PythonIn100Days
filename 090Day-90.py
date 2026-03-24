# API CALL

import requests

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=075a77a378a04641ad5564cad4ff8351"

response = requests.get(url)
data = response.json

for article in data["articles"]:
    print(article["title"])