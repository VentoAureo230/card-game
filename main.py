from models import PresidentGame

if __name__ == '__main__':
    print('\n')
    print(
        """        *********************************************
        *** President : The cards game ***
        ********************************************* """)
    g = PresidentGame(5)
    g.game_loop()

