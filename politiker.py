from bruker import Bruker

bruker = Bruker()

class Politiker:
    def __init__(self, navn, parti, stemmer):
        self._navn=navn
        self._parti=parti
        self._stemmer=stemmer
        self._verdi=100

    def hent_navn(self):
        return self._navn

    def hent_parti(self):
        return self._parti

    def hent_stemmer(self):
        return self._stemmer

    def hent_verdi(self):
        return self._verdi

    def sett_ny_verdi(self, verdi):
        self._verdi = verdi
        return self._verdi

    def kjop_spiller(self):
        if self._verdi < bruker.hent_bank():
            ny_bank = bruker.hent_bank() - self._verdi
            print(bruker.sett_ny_bank(ny_bank))
        else:
            return f"Ikke råd"

a=Politiker("erna", "høyre", 100)

a.kjop_spiller()
        
    



        