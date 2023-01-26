from bs4 import BeautifulSoup
import requests
import re

url = "https://www.vg.no/nyheter/innenriks/i/P4j4lz/kjerkol-om-omsorgssvikt-blir-like-opproert-som-alle-andre"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tag = doc.find_all(text=re.compile("Kjerkol.*"))
#tag = doc.find_all(["article"], class_="article")
# parent = prices[0].parent

# print(doc.prettify())
print(tag)