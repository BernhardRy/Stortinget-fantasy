import json

class Bruker:
    def __init__(self):
        self._bank=1000
        self._objekt = {
            "navn": "Fred",
            "parti": "Bondepartiet",
            "penger": 10000,
            "stemmer": 64
        }
        #self._json_objekt = json.dump(self._objekt, indent=4)

    def hent_bank(self):
        return self._bank

    def sett_ny_bank(self, verdi):
        self._bank = verdi
        return self._bank

    def ny_bruker(self):
        with open("bruker.json", "w") as outfile:
            json.dump(self._objekt, outfile)

a = Bruker()

a.ny_bruker()
