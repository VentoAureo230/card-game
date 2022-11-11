import tkinter

from models import PresidentGame
from tkinter.messagebox import showinfo, askquestion
from tkinter import *
from PIL import Image, ImageTk


def new_game():
    result = askquestion("Nouvelle partie",
                         "Voulez-vous relancer une partie ? Si une partie est en cours elle ne sera pas sauvegardée.",
                         icon='info')
    if result == 'yes':
        print('Génération d\'une nouvelle partie')
    else:
        print('rien')


def forfeit():
    result = askquestion("Abandon", "Voulez-vous abandonner ?", icon="warning")
    if result == 'yes':
        print('Fin de Jeu')
    else:
        pass


def info():
    result = showinfo("Crédit", "Jeu du président développer par Anthony Mény et Gillian Charra", icon="info")

    if result == 'yes':
        pass
    else:
        pass


def press_shuffle():
    global button_shuffle
    button_shuffle = Button(root, text='Press to shuffle cards', bg="light green", padx=25, pady=25,
                            font=("Helvatica", 14), command=start_game)
    button_shuffle.place(relx=0.5, rely=0.5, anchor=CENTER)

def show_card_player():
    global photos_card_player, photo_cards_enemy_1

    photos_card_player = []
    photo_cards_enemy_1 = []

    for card in player_hand:
        resized_card = resized_card(f'images/Cartes/{carte}.png')
        photos_card_player.append(resized_card)
    for card in enemy_hand:
        resized_card = resized_card(f'images/Cartes/dos/{b2fv}.png')
        photo_cards_enemy_1.append(resized_card)

def cards_in_the_middle(card):
    panel_0 = Label(frame_cards_middle, image= card, bg="black")
    panel_0.grid(row=0, column=0)


if __name__ == '__main__':
    g = PresidentGame(3)
    root = Tk()
    root.title('Jeu du président')
    root.geometry("1200x800")
    root.configure(background="#008000")
    #window.iconbitmap(r'pictures/icon.ico')
    menubar = Menu(root)

    menu1 = Menu(tearoff=0)
    menu1.add_command(label="Nouvelle partie", command=new_game)
    menu1.add_command(label="Abandonner", command=forfeit)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=root.quit)
    menubar.add_cascade(label="Jeu", menu=menu1)

    menu2 = Menu(tearoff=0)
    menu2.add_command(label="Couper")
    menu2.add_command(label="Copier")
    menu2.add_command(label="Coller")
    menubar.add_cascade(label="Editer", menu=menu2)

    menu3 = Menu(tearoff=0)
    menu3.add_command(label="A propos", command=info)
    menubar.add_cascade(label="Crédit", menu=menu3)

    root.config(menu=menubar)

    image = Image.open('images/Cartes/2 carreau.png')
    image = Image.open('images/Cartes/3 carreau.png')
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(root, image= photo)
    label.pack()
    root.mainloop()
    g.distribute_cards()
