from abc import abstractmethod
from tuomari import Tuomari

class Peli:
    def pelaa(self):
        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        tuomari = Tuomari()

        self.suorita(tuomari)

        print("Kiitos!")
        print(tuomari)
    
    @abstractmethod
    def suorita(self, tuomari):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

