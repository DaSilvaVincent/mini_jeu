from juste_prix import *
from jeu_allumettes import *
from juniper_green import *
from chasse_au_tresor import *
from memory import *

def choix_du_jeu():
    """
    Permet de faire l'affichage du menu et du choix des jeux
    """
    premier_choix=None
    second_choix=None
    menu()
    trait="----------------------------------------------------"
    print(trait)
    #Choix du jeu que l'utilsateur veut jouer.
    #Boucle pour reposer la question jusqu'à avoir 1, 2, 3, 4 ou 5 en entrée
    while premier_choix not in ["1","2","3","4","5"]:
        premier_choix=input("A quoi voulez-vous jouer\n Appuyez sur 1 pour le juste prix\n Appuyez sur 2 pour le jeu des allumettes\n Appuyez sur 3 pour le junipergreen\n Appuyez sur 4 pour la chasse aux trésors\n Appuyez sur 5 pour le memory\n")
        print(trait)
    #Si il choix le 1er jeu, alors choix du mode de ce jeu.
    if premier_choix=="1":
        #Boucle pour reposer la question jusqu'à avoir un 1 ou un 2 en entrée
        while second_choix not in ["1","2"]:
            second_choix=input("Tapez 1 pour que l'ordinateur cherche votre valeur\nTapez 2 pour chercher la valeur de l'ordinateur\n")
            print(trait)
        if second_choix=="1":
            nombre_mystere_humain_contre_ordinateur()
        elif second_choix=="2":
            nombre_mystere_ordinateur_contre_humain()
    #Si il choix le 2er jeu, alors choix du mode de ce jeu.
    elif premier_choix=="2":
        #Boucle pour reposer la question jusqu'à avoir un 1 ou un 2 en entrée
        while second_choix not in ["1","2"]:
            second_choix=input("Tapez 1 pour jouer à deux\nTapez 2 pour que l'ordinateur joue contre vous\n")
            print(trait)
        if second_choix=="1":
            jeu_des_allumettes_contre_humain()
        elif second_choix=="2":
            jeu_des_allumettes_contre_ordi()
    elif premier_choix=="3":
        juniperGreen()
    elif premier_choix=="4":
        chasse_tresor_manuel()
    elif premier_choix=="5":
        memory()

def menu():
    print("----------------------------------------------------")
    print("Bienvenue sur notre interface de choix de jeu")
    print("Vous avez le choix entre :\n - Le juste prix\n - Le jeu de l'allumette\n - Le juniper green\n - Une chasse au trésor\n - Un memory")
    input("Appuyez sur entrée pour jouer\n")
    
if __name__=="__main__":
    choix_du_jeu()