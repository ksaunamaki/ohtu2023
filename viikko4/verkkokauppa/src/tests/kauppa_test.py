import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 7)
            
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)

    def test_kahden_eri_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 12)

    def test_kahden_saman_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 14)

    def test_vain_varastossa_loytyvan_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 0

        # otetaan yliajettu toteutus käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)

    def test_aloita_asiointi_nollaa_tilan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # palautetaan alkutilanne
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jukka", "67890")

        # varmistetaan, että tilisiirtoa on kutsuttu uuden ostoksen tiedoilla
        self.pankki_mock.tilisiirto.assert_called_with("jukka", 42, "67890", self.kauppa._kaupan_tili, 5)

    def test_jokainen_maksutapahtuma_saa_uuden_viitenumeron(self):
        # Tehdään uusi mock-viitegenraattori joka palauttaa ennustettavat viitenumerot
        self.viitegeneraattori_mock = Mock()

        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella 2 ja kolmannella 3
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]
    
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jukka", "67890")

        # Varmistetaan ensimmäinen viitenumero generoituu oikein
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        # Toinen testiosto
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jukka", "67890")

        # Varmistetaan toinen viitenumero generoituu oikein
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)

    def test_poistettu_tuote_ei_mukana_maksussa(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla summalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 7)

