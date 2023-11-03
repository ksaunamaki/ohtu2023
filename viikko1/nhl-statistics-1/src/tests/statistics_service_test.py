import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_loytaa_pelaajan(self):
        player = self.stats.search("Semenko")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_haku_ei_loyda_pelaajaa(self):
        player = self.stats.search("X")

        self.assertIsNone(player)
    
    def test_haku_loytaa_tiimin_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

    def test_haku_ei_loyda_tiimin_pelaajia(self):
        players = self.stats.team("X")

        self.assertEqual(len(players), 0)

    def test_top_points_pelaajat_palautuu_oikein(self):
        players = self.stats.top(2)

        # top() metodissa on bugi, se palauttaa yhden enemmän kuin pyydetty määrä johtuen 0 indeksoinnista
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_goals_pelaajat_palautuu_oikein(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")

    def test_top_assists_pelaajat_palautuu_oikein(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
    
