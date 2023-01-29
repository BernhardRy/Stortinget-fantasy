from bs4 import BeautifulSoup
import requests
import json
# import pprint

o = open("politikere.json")
politikere = json.load(o)

url = "https://www.vg.no/nyheter/innenriks"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

main = doc.find('section', class_='hyperion-css-1jxrrtc')

text = "I dag"
text2 = "For mindre enn"
artikler = []
artikler_med_politikere = []
artikler_dict = {}
artikler_m_politikere_dict = {}

def finn_artikler_i_dag():
    main = doc.find('section', class_='hyperion-css-1jxrrtc')
    i = 0

    for a in main:
        times = a.find_all('time')
        for time in times:
            if (text in time.text or text2 in time.text):
                alleUrler = a.find(['a'], href=True)
                finn_attr_href = alleUrler["href"]
                artikler.append(finn_attr_href)
                I = str(i)
                artikler_dict[I] = {'url': f"https://www.vg.no{finn_attr_href}", 'publisert': time.text}
                i += 1
                
                # print(f"ARTIKKEL: https://www.vg.no{finn_attr_href}")
                # print(f"BLE PUBLISERT: {time.text}")
                # print()

finn_artikler_i_dag()
print(len(artikler))

def finn_alle_artikler_med_politikere():
    for artikkel in artikler:
        url = "https://www.vg.no" + artikkel

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        
        for politiker in politikere["representanter_oversikt"]["representanter_liste"]["representant"]:
            if doc.body.find(text=f"{politiker['fornavn']} {politiker['etternavn']}"):
                print(f"{politiker['fornavn']} {politiker['etternavn']}")
                print(politiker["parti"]["id"])
                print(url)
                print()
                artikler_med_politikere.append("https://www.vg.no" + url)
                artikler_m_politikere_dict[f"{politiker['fornavn']} {politiker['etternavn']}"] = {"parti": politiker["parti"]["id"], "url": url}
                

# finn_alle_artikler_med_politikere()
# print_artikler_dict_fint = pprint.pformat(artikler_dict)
# print(print_artikler_dict_fint)
# print(artikler_m_politikere_dict)