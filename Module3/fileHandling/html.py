# requests
import requests

response = requests.get("https://dev.to")

html = response.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)