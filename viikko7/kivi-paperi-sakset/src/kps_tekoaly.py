from tekoaly import Tekoaly
from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly: Tekoaly):
        super().__init__()
        self._tekoaly = tekoaly

    def _siirron_jalkeiset_toimenpiteet(self, ekan_siirto, tokan_siirto):
        self._tekoaly.aseta_siirto(ekan_siirto)

    def _lue_siirrot(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return (ekan_siirto, tokan_siirto)
