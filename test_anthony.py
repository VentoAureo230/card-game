import unittest
import models



class TestFunctionCardGame(unittest.TestCase):

    def test_victory(self):
        """Test la fin du jeu quand le joueur (humain pas IA) n'a plus de carte en main"""
        game = models.PresidentGame()
        player_1 = game.players[0]
        self.assertTrue(len(player_1.hand) < 1)
        self.assertFalse(len(player_1.hand) > 1)

    def test_end_game(self):
        """Affche la fin de game quand il reste 1 seul joueur avec des cartes en main
         TODO :  doit attribuer le rôle de troufion et président en fin de game si le joueur relance une partie
        """
        game = models.PresidentGame()
        players = len(game.players)
        self.assertTrue(len(players.hand) < 2)

    def test_round(self):
        """Compte le nombre de rounds dans une partie ?"""
        game = models.PresidentGame()
        pass