from kayttoliittyma import Komento
from typing import Optional

class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._prev_arvo = 0
        self.komennot = {
            Komento.SUMMA: self.plus,
            Komento.EROTUS: self.miinus,
            Komento.NOLLAUS: self.nollaa,
            Komento.KUMOA: self.kumoa,
        }
        
    def hae(self, komento, operandi: Optional[int]):
        if operandi:
            return self.komennot[komento](operandi)
        else:
            return self.komennot[komento]()

    def miinus(self, operandi):
        self._prev_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._prev_arvo = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._prev_arvo = self._arvo
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._prev_arvo = self._arvo
        self._arvo = arvo
    
    def kumoa(self):
        self._arvo = self._prev_arvo

    def arvo(self):
        return self._arvo