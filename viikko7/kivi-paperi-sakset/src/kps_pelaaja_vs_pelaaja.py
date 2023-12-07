from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()

    def _lue_siirrot(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return (ekan_siirto, tokan_siirto)