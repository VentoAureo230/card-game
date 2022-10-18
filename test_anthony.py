import unittest
import models



class TestFunctionCardGame(unittest.TestCase):

    def test_end_game(self):
        game = models.PresidentGame()
        player_1 = game.players[0]
        print(player_1.hand)
        self.assertTrue(len(player_1.hand) < 1)
        self.assertFalse(len(player_1.hand) > 1)