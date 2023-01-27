from bs4 import BeautifulSoup
import requests
import json
# import re

o = open("politikere.json")
passeringsregister = json.load(o)

url = "https://www.vg.no/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all(['a'], href=True)

for i in tags:
    for politiker in passeringsregister["representanter_oversikt"]["representanter_liste"]["representant"]:
        if "https" in i["href"]:
            url = i["href"]
            
            if ("/" + politiker["etternavn"].lower() + "-" in url.lower()) or ("-" + politiker["etternavn"].lower() + "-" in url.lower()):
                print(f"{politiker['fornavn']} {politiker['etternavn']} URL: {url}")

            else:
                pass