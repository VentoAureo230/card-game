from models import PresidentGame
from models import VALUES

def print_ln():
    print('\n')


def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """
    wanna_continue = True
    players_list=[]
    for player in g.players:
        players_list.append(player)
    while wanna_continue:
        players_list = []
        for player in g.players:
            players_list.append(player)
        print_ln()
        for joueur in g.players:
            print(joueur.name,"has",len(joueur.hand),"cards")

        joueurs_debouts=players_list
        choice=None
        while len(joueurs_debouts)>1:
            i=0
            print("Nouveau Tour")
            for player in joueurs_debouts:
                if len(player.hand)<1:
                    print(player.name,"wins")
                    wanna_continue=False
                if choice is not None:
                    choice_before = choice.value
                    nb_cards = len(plays)
                    is_first_turn = False
                else:
                    nb_cards = 1
                    choice_before = 0
                    is_first_turn = True
                if player.is_human==True:
                    print('Your current deck is : ')
                    print(g.main_player.hand, )
                    player_choice=None
                    choice_player_value =0
                    while (g.main_player.has_symbol(player_choice) < nb_cards or choice_before > choice_player_value ) and player_choice != 'ff':
                        player_choice = input('What value do you wish to play ? ')
                        if player_choice !='ff':
                            choice_player_value=VALUES[player_choice]
                            if g.main_player.has_symbol(player_choice)>1 and is_first_turn:
                                nb_cards = int(input('How many ? '))
                        print(player_choice != 'ff')
                    if player_choice != 'ff':
                        plays = g.main_player.play(player_choice,nb_cards)
                        print(f"You play {plays}")

                        nb_cards = len(plays)
                        choice = plays[0]
                    else:
                        print('tu es nul')
                        print(f"You skipped")
                        plays=[]


                else:
                    plays = player.play(choice, nb_cards)
                    print(f"{player.name} plays \t {plays}")

                # Update the latest card played
                if len(plays) > 0:
                    choice = plays[0]
                    i += 1
                else:
                    print(joueurs_debouts[i].name,'hors-jeu')
                    joueurs_debouts.pop(i)

        print('fin de la manche')

        #wanna_continue = input('Do you want to continue playing (y/N)? ')
        #wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')


if __name__ == '__main__':
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    g = PresidentGame(3)
    g.distribute_cards()
    game_loop(g)
    print('Thank you for playing. I hope you enjoyed !')
