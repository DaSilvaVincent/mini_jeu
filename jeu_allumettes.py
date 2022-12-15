from random import randint

def jeu_des_allumettes_contre_humain():
    """
    Permet de jouer au jeu des allumettes avec 2 joueurs humains
    """
    nb_allumettes = 21
    while nb_allumettes != 0:
        # Affichage des allumettes
        print("I"*nb_allumettes)
        # La boucle permet de gérer les erreurs de saisis
        tour_joueur1 = True
        while tour_joueur1:
            choix_joueur1 = int(input("Joueur 1: Combien d'allumettes enlèves-tu ?\n"))
            if (1 <= choix_joueur1 <=3) and (choix_joueur1 <= nb_allumettes):
                nb_allumettes -= choix_joueur1
                tour_joueur1 = False
            else:
                print("Erreur de saisi")
        if nb_allumettes == 0:
            print("Victoire du joueur 2!")
        else:
            # Affichage des allumettes
            print("I"*nb_allumettes)
            # La boucle permet de gérer les erreurs de saisis
            tour_joueur2 = True
            while tour_joueur2:
                choix_joueur2 = int(input("Joueur 2: Combien d'allumettes enlèves-tu ?\n"))
                if (1 <= choix_joueur2 <=3) and (choix_joueur2 <= nb_allumettes):
                    nb_allumettes -= choix_joueur2
                    tour_joueur2 = False
                else:
                    print("Erreur de saisi")
            if nb_allumettes == 0:
                print("Victoire du joueur 1!")
    
def jeu_des_allumettes_contre_ordi():
    """
    Permet de jouer au jeu des allumettes avec l'ordinateur
    """
    nb_allumettes = 21
    while nb_allumettes != 0:
        # Affichage des allumettes
        print("I"*nb_allumettes)
        # La boucle permet de gérer les erreurs de saisis
        tour_joueur = True
        while tour_joueur:
            choix_joueur = int(input("Joueur: Combien d'allumettes enlèves-tu ?\n"))
            if (1 <= choix_joueur <=3) and (choix_joueur <= nb_allumettes):
                nb_allumettes -= choix_joueur
                tour_joueur = False
            else:
                print("Erreur de saisi")
        if nb_allumettes == 0:
            print("Victoire de l'ordinateur!")
        else:
            print("I"*nb_allumettes)
            # Donne une petite intelligence à l'ordinateur
            if nb_allumettes in [2,3]:
                choix_ordi = randint(1,2)
            elif nb_allumettes == 1:
                choix_ordi = 1
            else:
                choix_ordi = randint(1,3)
            print("L'ordinateur enlève {} allumette(s)".format(choix_ordi))
            nb_allumettes -= choix_ordi
            if nb_allumettes == 0:
                print("Victoire du joueur 1!")
    