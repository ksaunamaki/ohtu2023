KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti = KAPASITEETTI, kasvatuskoko = OLETUSKASVATUS):
        self.lahtokapasiteetti = KAPASITEETTI
        
        if isinstance(kapasiteetti, int) and kapasiteetti > 0:
            self.lahtokapasiteetti = kapasiteetti

        if isinstance(kasvatuskoko, int) and kasvatuskoko > 0:
            self.kasvatuskoko = kasvatuskoko
        else:
            self.kasvatuskoko = OLETUSKASVATUS

        self.lista = self._luo_lista()
        self.seuraava_alkio = 0

    def _kopioi(self, lahde_lista, kohde_lista,\
                lahde_ensi_elementti = 0, kohde_ensi_elementti = 0,\
                elementtien_lkm = None):
        if lahde_lista is None:
            return
        
        if elementtien_lkm is None:
            elementtien_lkm = len(lahde_lista)
        
        indeksi = 0
        
        for _ in range(0, elementtien_lkm):
            kohde_lista[kohde_ensi_elementti + indeksi] = lahde_lista[lahde_ensi_elementti + indeksi]
            indeksi += 1


    def _luo_lista(self, edellinen_lista = None):
        uusi_koko = self.lahtokapasiteetti

        if edellinen_lista is not None:
            uusi_koko = len(edellinen_lista) + self.kasvatuskoko

        lista = [0] * uusi_koko
        self._kopioi(edellinen_lista, lista)

        return lista
    
    def kuuluu(self, n):
        for i in range(0, self.seuraava_alkio):
            if n == self.lista[i]:
                return True

        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        if len(self.lista) == self.seuraava_alkio:
            # pitää kasvattaa
            self.lista = self._luo_lista(self.lista)

        self.lista[self.seuraava_alkio] = n
        self.seuraava_alkio += 1

        return True

    def poista(self, n):
        for i in range(0, self.seuraava_alkio):
            if n == self.lista[i]:
                # löytyi, siirretään mahdollisia loppualkioita taaksepäin
                self._kopioi(self.lista, self.lista, i + 1, i, self.seuraava_alkio - i)
                self.seuraava_alkio -= 1
                
                return True

        return False

    def mahtavuus(self):
        return self.seuraava_alkio

    def to_int_list(self):
        lista = [0] * self.seuraava_alkio
        self._kopioi(self.lista, lista, 0, 0, len(lista))

        return lista

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()

        for alkio in a.to_int_list():
            yhdiste.lisaa(alkio)

        for alkio in b.to_int_list():
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()

        for alkio in a.to_int_list():
            if b.kuuluu(alkio):
                leikkaus.lisaa(alkio)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()

        for alkio in a.to_int_list():
            if not b.kuuluu(alkio):
                erotus.lisaa(alkio)

        return erotus

    def __str__(self):
        return "{" + ", ".join(map(lambda num: num.__str__(), self.to_int_list())) + "}"
