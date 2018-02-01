from tkinter import*
from Jeu_du_8 import*
from Francais import*
from Jeu_du_9 import*

def menu():
    global fen, fen2, fen3
    fen=Tk()
    aire=Canvas(fen,height=768, width=1802)
    mon_image = PhotoImage(file="menu.png", master=fen)
    logo= aire.create_image(901,384, image=mon_image)
    aire.image = mon_image
    aire.pack()
    Bouton1=Button(fen, text = "Billard Americain",command = Américain)
    Bouton1.pack()
    Bouton2=Button(fen, text= "Billard Français",command = Billard_Français)
    Bouton2.pack()
    Bouton3=Button(fen, text= "Quitter", command= fen.destroy)
    Bouton3.pack()

def Américain():
    fen.destroy()
    Billard_Americain()

def Billard_Français():
    fen.destroy()
    Francais()

def Jeu8():
    fen.destroy()
    Jeu_du_8()

def Jeu9():
    fen.destroy()
    Jeu_du_9()

def Billard_Americain():
    global fen, fen2, fen3
    fen=Tk()
    aire=Canvas(fen,height=768, width=1802)
    mon_image = PhotoImage(file="menu.png", master=fen)
    logo= aire.create_image(901,384, image=mon_image)
    aire.image = mon_image
    aire.pack()
    Bouton1=Button(fen, text = "Jeu du 8",command= Jeu8)
    Bouton1.pack()
    Bouton2=Button(fen, text= "Jeu du 9",command= Jeu9)
    Bouton2.pack()
    Bouton3=Button(fen, text= "Quitter",command=fen.destroy)
    Bouton3.pack()
    Bouton4=Button(fen, text= "Retour",command=Retour)
    Bouton4.pack()

def Retour():
    fen.destroy()
    menu()
menu()
fen.mainloop()