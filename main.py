from models import PresidentGame

if __name__ == '__main__':
    print('\n')
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    wanna_continue=True
    g = PresidentGame(5)
    tdc = None
    el_prez = None
    while wanna_continue:

        g.distribute_cards()
        g.game_loop()


        for player in g.players:
            if player.is_trouduc==True:
                tdc=player
            if player.is_president==True:
                el_prez=player
        if el_prez is not None and tdc is not None:
            print(el_prez.name,'est le president',tdc.name,'est le trouduc')
        print('Thank you for playing. I hope you enjoyed !')
        response_user=input('continue O/N')
        if response_user=='o' or response_user=='O':
            wanna_continue=True
        else:
            wanna_continue=False
