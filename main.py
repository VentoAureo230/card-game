from models import PresidentGame


def print_ln():
    print('\n')

if __name__ == '__main__':
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    g = PresidentGame(3)
    g.distribute_cards()
    g.game_loop()
    print('Thank you for playing. I hope you enjoyed !')
