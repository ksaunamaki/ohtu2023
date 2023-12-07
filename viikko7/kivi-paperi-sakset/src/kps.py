from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self._tuomari = Tuomari()

    def tulosta_ohje(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

    def pelaa(self):
        # lue siirrot, pelimoottorista riippuen
        ekan_siirto, tokan_siirto = self._lue_siirrot()

        # pelaa kunnes virhe
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            # kirjaa siirrot
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            # siirron jälkeiset toimenpiteet, pelimoottorista riippuen
            self._siirron_jalkeiset_toimenpiteet(ekan_siirto, tokan_siirto)

            # seuraava kierros
            ekan_siirto, tokan_siirto = self._lue_siirrot()

        # tulosta lopputulos
        print("Kiitos!")
        print(self._tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def _lue_siirrot(self):
        return ("","")
    
    def _siirron_jalkeiset_toimenpiteet(self, ekan_siirto, tokan_siirto):
        pass

