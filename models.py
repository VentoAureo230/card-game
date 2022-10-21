import random
import names

# from random import *
COLORS = ['♡', '♤', '♧', '♢']
VALUES = {
    '2': 15,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'V': 11,
    'D': 12,
    'R': 13,
    'A': 14
}


class Deck:
    """ Deck du jeu de société du Président. """

    def __init__(self):
        self.__cards: list = []
        """ Génération d'un deck de 52 cartes"""
        for (symbol, val) in VALUES.items():
            for color in COLORS:
                new_card = Card(symbol, color)
                self.__cards.append(new_card)

    def shuffle(self) -> None:
        """ Mélanger les cartes de mon deck. """
        random.shuffle(self.__cards)

    def pick_card(self):
        return self.cards.pop(0)

    def __str__(self) -> str:
        return str(self.__cards)

    @property
    def cards(self):
        return self.__cards


class Card:
    __symbol: str
    __value: int
    __color: str

    def __init__(self, symbol: str, color: str):
        """
            Card Constructor.
            attrs:
                symbol: One of the VALUES keys.
                color:  One of the  COLORS values.
        """

        self.__symbol = symbol
        self.__value = VALUES[symbol]
        self.__color = color

    def __lt__(self, other):
        return self.__value < other.value

    def __gt__(self, other):
        return self.__value > other.value

    def __eq__(self, other):
        return self.__value == other.value

    def __ne__(self, other):
        return self.__value != other.value

    @property
    def value(self):
        return self.__value

    @property
    def symbol(self):
        return self.__symbol

    def __repr__(self):
        return f"{self.__symbol} {self.__color}"


class Player:
    is_human = True

    def __init__(self, player_name=None):
        self._name: str = player_name if player_name is not None else \
            names.get_first_name()
        self._hand: list = []

    def add_to_hand(self, card: Card):
        self._hand.append(card)
        self._hand.sort()

    def remove_from_hand(self, cards: list):
        for c in cards:
            self._hand.remove(c)

    @property
    def hand(self):
        return self._hand

    @property
    def name(self):
        return self._name

    def play(self, symbol, nb_cards) -> list:
        """
        Remove from the hand of the player, all cards having a corresponding symbol.
        Args:
            symbol: The symbol to look for.

        Returns: The cards removed from the hand of the player. It will return an empty array if
        nothing is found.

        """
        cards_played = []
        cards_available = [card for card in self._hand if card.symbol ==
                           symbol]
        for i in range(nb_cards):
            cards_played.append(cards_available.pop(0))

        self.remove_from_hand(cards_played)
        return cards_played

    def __repr__(self):
        return f"{self.name}\t: {self.hand}"

    def has_symbol(self, card_symbol) -> int:
        nb_cards = 0
        for card in self._hand:
            if card.symbol == card_symbol:
                nb_cards += 1
        return nb_cards


class AIPlayer(Player):
    is_human = False

    def play(self, choice, nb_cards: int) -> list:
        """
        Play a card corresponding to what has been played on the table.
        TODO: Implement an AI
        Args:
            choice: The minimum card value to play.
            nb_cards: The number of cards to play.

        Returns: An array of cards to play.

        """
        if choice is None:
            choice = self.hand[random.randint(0, len(self.hand) - 1)]
        best_choice = None
        for index, card in enumerate(self.hand):
            if best_choice is None and card.value >= choice.value and self.has_symbol(card.symbol) >= nb_cards:
                cards_played = self._hand[index:index + nb_cards]
                best_choice = card.symbol
                self.remove_from_hand(cards_played)
        return cards_played if best_choice is not None else []


class PresidentGame:
    def __init__(self, nb_players: int = 3):
        self.__generate_players(nb_players)
        self.__generate_cards()
        self.round = 0
        self.nb_players = nb_players

    def __generate_players(self, nb_players: int):
        self.__players = [Player()]
        for _ in range(nb_players - 1):
            self.__players.append(AIPlayer())

    def __generate_cards(self):
        self.__deck = Deck()
        self.__deck.shuffle()

    def distribute_cards(self):
        giving_card_to_player = 0
        nb_players = len(self.__players)
        while len(self.__deck.cards) >= nb_players - giving_card_to_player:
            card = self.__deck.pick_card()
            self.__players[giving_card_to_player].add_to_hand(card)
            giving_card_to_player = (giving_card_to_player + 1) % nb_players

    def player_active(self):
        """Un joueur est défini comme actif s'il a au moins une carte en main"""
        return [player for player in self.__players if len(player.hand) > 0]

    def new_round(self):
        self.last_played_card: Card = None
        pass

    def game_loop(self):
        """
        The main game loop.
        Loops in circle until the user wants to quit the application.
        """
        wanna_continue = True
        players_list = []
        for player in players_list:
            players_list.append(player)
        while wanna_continue:
            players_list = []
            for player in players_list:
                players_list.append(player)
            for joueur in players_list:
                print(joueur.name, "has", len(joueur.hand), "cards")

            joueurs_debouts = players_list
            choice = None
            while len(joueurs_debouts) > 1:
                i = 0
                for player in joueurs_debouts:
                    if len(player.hand) < 1:
                        print(player.name, "wins")
                        wanna_continue = False
                    if choice is not None:
                        choice_before = choice.value
                        nb_cards = len(plays)
                        is_first_turn = False
                    else:
                        nb_cards = 1
                        choice_before = 0
                        is_first_turn = True
                    if player.is_human:
                        print('Your current deck is : ')
                        print(self.main_player.hand, )
                        player_choice = None
                        choice_player_value = 0
                        while (self.main_player.has_symbol(
                                player_choice) < nb_cards or choice_before > choice_player_value) and player_choice != 'ff':
                            player_choice = input('What value do you wish to play ? ')
                            if player_choice != 'ff':
                                choice_player_value = VALUES[player_choice]
                                if self.main_player.has_symbol(player_choice) > 1 and is_first_turn:
                                    nb_cards = int(input('How many ? '))
                            print(player_choice != 'ff')
                        if player_choice != 'ff':
                            plays = self.main_player.play(player_choice, nb_cards)
                            print(f"You play {plays}")

                            len(plays)
                            choice = plays[0]
                        else:
                            print('tu es nul')
                            print(f"You skipped")
                            plays = []

                    else:
                        plays = player.play(choice, nb_cards)
                        print(f"{player.name} plays \t {plays}")

                    # Update the latest card played
                    if len(plays) > 0:
                        choice = plays[0]
                        i += 1
                    else:
                        print(joueurs_debouts[i].name, 'hors-jeu')
                        joueurs_debouts.pop(i)

            print('fin de la manche')

            # wanna_continue = input('Do you want to continue playing (y/N)? ')
            # wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')

    @property
    def players(self):
        return self.__players

    @property
    def ai_players(self):
        return self.__players[1:]

    @property
    def main_player(self):
        """ Main player is player 0 """
        return self.__players[0]
