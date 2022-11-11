import unittest

import models


class TestFunctionCardGame(unittest.TestCase):

    def test_victory(self):
        """Test la fin du jeu quand le joueur (humain pas IA) n'a plus de carte en main"""
        game = models.PresidentGame()
        game.distribute_cards()
        player_1 = game.players[0]
        player_2 = []
        self.assertGreater(len(player_1.hand), 0, "Le joueur a des cartes en main")
        self.assertEqual(len(player_2), 0, "Le joueur n'a plus de carte")

    def test_is_active(self):
        """Un joueur est actif s'il a au moins 1 carte en main"""
        game = models.PresidentGame()
        game.distribute_cards()
        game.player_active()
        player_1 = game.players[0]
        player_2 = []
        self.assertTrue(len(game.player_active()) > 1)
        self.assertFalse(game.player_active(len(player_2)) is False)

    def test_end_game(self):
        """Affiche la fin de game quand il reste 1 seul joueur avec des cartes en main"""
        game = models.PresidentGame()
        game.distribute_cards()
        game.player_active()
        player_1 = game.players[0]
        player_2 = game.players[1]
        player_3 = []
        print(player_1.hand, '\n', player_2.hand, '\n', player_3)
        self.assertGreater(len(game.player_active()), 1, "There should be more than 1 active players")


    def test_round(self):
        """  """
        game = models.PresidentGame()
        game.round()
        self.assertTrue()
        pass