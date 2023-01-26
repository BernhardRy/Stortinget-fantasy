from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.find_all("button", {"class": "hei"})
# tags = doc.find_all(text=re.compile("\$.*"))

# tag['style'] = 'display: flex;'
# tag['color'] = 'blue'

# print(tag.attrs)

tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "Du er byttet ut!"

with open("endret.html", "w") as file:
    file.write(str(doc))
