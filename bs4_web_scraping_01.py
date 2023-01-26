from bs4 import BeautifulSoup
import requests
import re

url = "https://www.vg.no/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#tag = doc.find_all(text=re.compile("Kjerkol.*"))
#tag = doc.find_all(["article"], class_="article")
# parent = prices[0].parent

# print(doc.prettify())

tags = doc.find_all(['a'], href=True)

for i in tags:
    if "https" in i["href"]:
        url = i["href"]

        if "kjerkol-" in url.lower():
            print(url)

# print(tags[0])