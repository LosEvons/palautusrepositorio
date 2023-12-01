KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko: int = OLETUSKASVATUS):
        if kapasiteetti < 0:
            raise Exception("Liian pieni kapasiteetti")
        else:
            self.kapasiteetti: int = kapasiteetti
            
        if kasvatuskoko < 0:
            raise Exception("Liian pieni kasvatuskoko")
        else:
            self.kasvatuskoko: int = kasvatuskoko

        self.ljono: list[int] = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm: int = 0

    def kuuluu(self, p_alkio) -> bool:
        for alkio in self.ljono:
            if p_alkio == alkio:
                return True
        return False

    def lisaa(self, p_alkio) -> bool:
        if not self.kuuluu(p_alkio):
            self.ljono[self.alkioiden_lkm] = p_alkio
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm == len(self.ljono):
                self.ljono = self.ljono + self._luo_lista(self.kasvatuskoko)
            return True
        return False

    def poista(self, p_alkio) -> bool:
        for alkio in self.ljono:
            if p_alkio == alkio:
                self.ljono.remove(alkio)
                self.alkioiden_lkm -= 1
                return True
        
        return False

    def mahtavuus(self) -> int:
        return self.alkioiden_lkm

    def to_int_list(self) -> list[int]:
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(p_taulu1: object, p_taulu2: object) -> object:
        uusi_joukko = IntJoukko()
        for alkio in p_taulu1.to_int_list() + p_taulu2.to_int_list():
            uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def leikkaus(p_taulu1, p_taulu2) -> object:
        uusi_joukko = IntJoukko()
        for alkio in p_taulu1.to_int_list():
            if p_taulu2.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def erotus(p_taulu1: object, p_taulu2: object) -> object:
        uusi_joukko = IntJoukko()
        for alkio in p_taulu1.to_int_list():
            if not p_taulu2.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)
        return uusi_joukko

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"