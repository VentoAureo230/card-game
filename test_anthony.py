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
         TODO :  vérifier l'attribution des rôles de troufion et président (et des vices si 4 joueurs ou plus) en fin de game si le joueur relance une partie
        """
        game = models.PresidentGame()
        game.distribute_cards()
        game.player_active()
        player_1 = game.players[0]
        player_2 = game.players[1]
        player_3 = game.players[2]
        nb_players = game.player_active
        print(player_1.hand, '\n', player_2.hand, '\n', player_3.hand)
        self.assertTrue()
        print('Un joueur a perdu')
        self.assertFalse()
        print('Il reste au moins 2 joueurs en jeu avec des cartes en main')

    def test_round(self):
        """Compte le nombre de rounds dans une partie ?"""
        game = models.PresidentGame()
        pass
