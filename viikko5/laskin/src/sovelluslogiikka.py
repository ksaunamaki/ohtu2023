class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_komento = None

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def aseta_edellinen_komento(self, komento):
        self.edellinen_komento = komento

class Summa:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
        self.edellinen = 0

    def suorita(self):
        self.edellinen = self.sovellus.tulos

        self.sovellus.aseta_arvo(self.sovellus.tulos + self.lue_syote())
        self.sovellus.aseta_edellinen_komento(self)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
        self.edellinen = 0

    def suorita(self):
        self.edellinen = self.sovellus.tulos

        self.sovellus.aseta_arvo(self.sovellus.tulos - self.lue_syote())
        self.sovellus.aseta_edellinen_komento(self)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen)

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus
        self.edellinen = 0

    def suorita(self):
        self.edellinen = self.sovellus.tulos

        self.sovellus.aseta_arvo(0)
        self.sovellus.aseta_edellinen_komento(self)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen)

class Kumoa:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        if self.sovellus.edellinen_komento is not None:
            self.sovellus.edellinen_komento.kumoa()