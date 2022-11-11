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
    is_president = False
    is_trouduc = False

    def __init__(self, player_name=None,id=None):
        if self.is_human==True:
            player_name='You'
        self._name: str = player_name if player_name is not None else names.get_first_name()
        self._id=id
        self._hand: list = []

    def __eq__(self, other):
        return self._id == other._id

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
        return str(self._id)#f"{self.name}\t: {self.hand}"

    def has_symbol(self, card_symbol) -> int:
        nb_cards = 0
        for card in self._hand:
            if card.symbol == card_symbol:
                nb_cards += 1
        return nb_cards

class AIPlayer(Player):
    is_human = False

    def play(self, choices, nb_cards: int) -> list:
        """
        Play a card corresponding to what has been played on the table.
        TODO: Implement an AI
        Args:
            choice: The minimum card value to play.
            nb_cards: The number of cards to play.

        Returns: An array of cards to play.

        """
        if choices is not None:
            choice=choices[0]
        else:
            choice=None
        if choice is None:
            choice = self.hand[random.randint(0, len(self.hand) - 1)]
        best_choice = None
        for index, card in enumerate(self.hand):
            if best_choice is None and card.value >= choice.value and self.has_symbol(card.symbol) >= nb_cards:
                cards_played = self._hand[index:index + nb_cards]
                best_choice = card.symbol
                self.remove_from_hand(cards_played)
        print(f"{self.name} plays \t {cards_played if best_choice is not None else []}")
        return cards_played if best_choice is not None else None


class PresidentGame:
    def __init__(self, nb_players: int = 3):
        self.__generate_players(nb_players)
        self.__generate_cards()
        self.round = 0
        self.nb_players = nb_players
        self.troufion=None
        self.president=None

    def __generate_players(self, nb_players: int):
        self.__players = [Player(None,0)]
        for i in range(nb_players - 1):
            self.__players.append(AIPlayer(None,i+1))

    def __generate_cards(self):
        self.__deck = Deck()
        self.__deck.shuffle()

    def distribute_cards(self):
        self.__generate_cards()
        giving_card_to_player = 0
        nb_players = len(self.__players)
        while len(self.__deck.cards) >= nb_players - giving_card_to_player:
            card = self.__deck.pick_card()
            self.__players[giving_card_to_player].add_to_hand(card)
            giving_card_to_player = (giving_card_to_player + 1) % nb_players
        if self.president is not None and self.troufion is not None:
            self.cards_switch()
    def cards_switch(self):
        for _ in range (2):
            troufion_card=self.troufion.hand.pop(-1)
            i=0
            hand=self.president.hand
            while hand[i].value<troufion_card.value and i<len(hand):
                i+=1
            self.president.hand.insert(i,troufion_card)
            i=0
            president_card=self.president.hand.pop(0)
            hand=self.troufion.hand
            while hand[i].value<president_card.value and i<len(hand):
                i+=1
            self.troufion.hand.insert(i,president_card)
        print(self.president.hand,self.troufion.hand)

    def player_active(self):
        """Un joueur est défini comme actif s'il a au moins une carte en main"""
        return [player for player in self.__players if len(player.hand) > 0]

    def human_asked_to_play(self,player):
        if self.previous_cards_played is not None:
            self.nb_cards_round = len(self.previous_cards_played)
            self.is_first_turn = False
        else:
            self.nb_cards_round = 1
            self.is_first_turn = True
        print('Your current deck is : ')
        print(player.hand, )
        player_choice = None
        choice_player_value = 0
        while (player.has_symbol(player_choice) < self.nb_cards_round or self.previous_cards_played_value() > choice_player_value) and player_choice != 'ff':
            player_choice = input('What value do you wish to play ? ')
            if player_choice != 'ff':
                try:
                    choice_player_value = VALUES[player_choice]
                except:
                    pass
                if player.has_symbol(player_choice) > 1 and self.is_first_turn:
                    self.nb_cards_round = int(input('How many ? '))
                elif self.is_first_turn:
                    self.nb_cards_round = 1
                else:
                    pass
        if player_choice != 'ff':
            choice = player.play(player_choice, self.nb_cards_round)
            print(f"You play {self.previous_cards_played}")
            self.previous_cards_played=choice
        else:
            print(f"You skipped")
            choice=None
        return choice
    def player_ran_out_of_cards(self,player):
        print(player.name, "n'as plus de carte")
        self.players_list_still_has_card.remove(player)
        self.players_to_remove.append(player)
        if self.president == None:
            self.president = player
            player.is_president = True
    def round_over(self):
        if len(self.players_list_still_has_card) == 1:#game over
            self.troufion = self.players_list_still_has_card[0]
            self.troufion.is_trouduc = True
            self.players_list_still_has_card[0]._hand = []
            self.active_game = False
        else:#new round
            round_winner = self.still_playing_round[0].name
            print(round_winner, 'gagne, fin de la manche')
            j = 0
            self.still_playing_round = []
            for player in self.players_list_still_has_card:
                if player.name == round_winner:
                    z = 0
                    while self.players_list_still_has_card[j].name != round_winner or z == 0:
                        self.still_playing_round.append(self.players_list_still_has_card[j])
                        z += 1
                        j += 1
                        if j >= len(self.players_list_still_has_card):
                            j = 0
                j += 1
    def game_loop(self):
        """
        The main game loop.
        Loops in circle until the user wants to quit the application.
        Args:
            g: The President Game instance.
        """
        wanna_continue=True
        while wanna_continue:
            self.distribute_cards()
            self.still_playing_round = [x for x in self.players]
            self.players_list_still_has_card = [x for x in self.players]
            active_game = True
            while active_game:
                print('\n')
                for joueur in self.players_list_still_has_card:
                    print(joueur.name, "has", len(joueur.hand), "cards")
                self.previous_cards_played = None
                self.players_to_remove = []
                i=0
                while len(self.still_playing_round) > 1:
                    if i > len(self.still_playing_round) - 1:
                        i = 0
                    player=self.still_playing_round[i]

                    if player.is_human == True:#human
                        player_choice=self.human_asked_to_play(player)

                    else:#bot
                        player_choice=player.play(self.previous_cards_played, self.nb_cards_round)
                        if player_choice is not None:
                            self.previous_cards_played=player_choice

                    if len(player.hand) < 1:
                        self.player_ran_out_of_cards(player)

                    # Update the latest card played
                    elif player_choice is not None:
                        i+=1
                    else:
                        self.players_to_remove.append(player)

                    for player_to_remove in self.players_to_remove:
                        self.still_playing_round.remove(player_to_remove)
                    self.players_to_remove = []
                self.round_over()

            print('Thank you for playing. I hope you enjoyed !')
            response_user = input('continue O/N')
            if response_user == 'o' or response_user == 'O':
                wanna_continue = True
            else:
                wanna_continue = False
    def previous_cards_played_value(self):
        if self.previous_cards_played is not None:
            previous_cards_played_value=self.previous_cards_played[0].value
        else:
            previous_cards_played_value =0
        return  previous_cards_played_value
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
