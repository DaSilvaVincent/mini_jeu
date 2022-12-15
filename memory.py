from random import *

def initGrille(nbLettres:int, nbLignes:int, nbColonnes:int) -> list:
    """
    Initialise une grille avec comme taille les paramètres données.
    :param nbLettres: le nombre de pairs disponible dans la grille
    :param nbLignes: le nombre de lignes dans la grille
    :param nbColonnes: le nombre de colonnes dans la grille
    :type nbLettres: int
    :type nbLignes: int
    :type nbColonnes: int
    :return: Une matrice avec nbLettres nombres de pairs
    :rtype: list
    """
    symboles = ['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H','I','I','J','J','K','K','L','L','M','M','N','N','O','O','P','P','Q','Q','R','R','S','S','T','T','U','U','V','V','W','W','X','X','Y','Y','Z','Z']
    compteur=0
    # Test sur les paramètres donnés pour savoir si la grille est possible
    if nbLignes*nbColonnes %2 != 0:
        print(nbLignes, "*", nbColonnes, " n'est pas paire")
        return None
    if 2 * nbLettres < nbLignes * nbColonnes:
        print("Il y a pas assez de symboles")
        return None
    elif 2 * nbLettres > nbLignes * nbColonnes or nbLettres*2 > len(symboles):
        print("Il y a trop de symboles")
        return None

    grille=[]
    # Création de la grille
    for l in range(nbLignes):
        grille.append([])
        for c in range(nbColonnes):
            grille[l].append(symboles[compteur])
            compteur+=1
    return grille


def melange(grille:list):
    """
    Permet de mélanger une matrice
    :param grille: une matrice qui sera mélangé
    :type grille: list
    """
    compteur = -1
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            compteur += 1
    for k in range(compteur*2):
        valeur1 = randint(0,compteur)
        valeur2 = randint(0,compteur)
        rang1 = 0
        rang2 = 0
        while valeur1 >= len(grille[0]):
            valeur1 -= len(grille[0])
            rang1 += 1
        while valeur2 >= len(grille[0]):
            valeur2 -= len(grille[0])
            rang2 += 1
        grille[rang1][valeur1], grille[rang2][valeur2] = grille[rang2][valeur2], grille[rang1][valeur1]

        
def initMarked(nbLignes:int, nbColonnes:int) -> list:
    """
    Créer une matrice aidant à savoir si les éléments de la grilles sont visibles ou non
    avec une taille donnée en paramètre avec False comme valeurs 
    :param nbLignes: nombre de lignes de la matrice
    :param nbColonnes: nombre de colonnes de la matrice
    :type nbLignes: int
    :type nbColonnes: int
    :return: retourne une matrice
    :rtype: list
    """
    grille=[]
    for l in range(nbLignes):
        grille.append([])
        for c in range(nbColonnes):
            grille[l].append(False)
    return grille

def initMarkedTrue(nbLignes:int, nbColonnes:int) -> list:
    """
    Créer une matrice aidant à savoir si une matrice est composé uniquement de True
    avec une taille donnée en paramètre avec True comme valeurs 
    :param nbLignes: nombre de lignes de la matrice
    :param nbColonnes: nombre de colonnes de la matrice
    :type nbLignes: int
    :type nbColonnes: int
    :return: retourne une matrice
    :rtype: list
    """
    grille=[]
    for l in range(nbLignes):
        grille.append([])
        for c in range(nbColonnes):
            grille[l].append(True)
    return grille

def display(grilleJeu:list, grilleVisible:list):
    """
    Permet d'afficher le grille de jeu si la case est visible selon la liste grilleVisible
    :param grilleJeu: la grille comportant les paires
    :param grilleVisible: la grille qui contient l'information de si une case est visible ou non
    """
    # Affichage des numéros de la grille
    ligne = "  "
    for i in range(len(grilleJeu[0])):
        ligne += f"{i+1} "
    print(ligne)

    # Affichage des pairs
    for i in range(len(grilleJeu)):
        ligne = f"{i+1} " # Affichage du numéro de la ligne
        for j in range(len(grilleJeu[i])):
            if grilleVisible[i][j]:
                ligne += f"{grilleJeu[i][j]} "
            else:
                ligne += "? "
        print(ligne)

def askPosition(grilleVisible:list)-> tuple:
    """
    Permet de demander au joueur quelle ligne il veut regarder en gérant si les lignes et colonnes sont disponibles
    :param grilleVisible: La grille que l'utilisateur voit
    :type grille: list
    :return: retourne un tuple vide si la case est déjà visible ou retourne un tuple avec les coordonnées de la case choisis par l'utilisateur
    :rtype: tuple
    """
    reponse = ""
    lignedisponible = [str(i+1) for i in range(len(grilleVisible))] # Défini les réponses possibles par l'utilisateur
    while reponse not in lignedisponible: # Boucle pour que l'utilisateur rentre un élément autorisé
        reponse = input("Numéro de la ligne : ")
    ligne = int(reponse) - 1 # L'utilisateur rentre un numéro de ligne mais on a besoin de l'index d'où le -1

    reponse = ""
    colonnedisponible = [str(i+1) for i in range(len(grilleVisible[0]))] # Défini les réponses possibles par l'utilisateur
    while reponse not in colonnedisponible: # Boucle pour que l'utilisateur rentre un élément autorisé
        reponse = input("Numéro de la colonne : ")
    colonne = int(reponse) - 1 # L'utilisateur rentre un numéro de ligne mais on a besoin de l'index d'où le -1
    
    if not grilleVisible[ligne][colonne]:
        return ligne, colonne
    return ()
    

def memory():
    """
    Fonction principale permettant de jouer au jeu du mémory
    """
    # ---
    # Initialisation de la partie
    # ---

    grille = None
    while grille == None: # Boucle tant que les paramètres ne sont pas bons
        trait = "----------------------"
        print(trait)
        print("Paramètres du jeu")
        nb_joueurs = ""
        nb_joueurs_possible = [str(i+1) for i in range(10)]
        while nb_joueurs not in nb_joueurs_possible:
            nb_joueurs = input("Combien de Joueurs ? (max 10): ")
        nb_lettres = ""
        while not nb_lettres.isdigit():
            nb_lettres = input("Combien de lettres ? : ")
        nb_lignes = ""
        while not nb_lignes.isdigit():
            nb_lignes = input("Combien de lignes ? : ")
        nb_colonnes =""
        while not nb_colonnes.isdigit():
            nb_colonnes = input("Combien de colonnes ? : ")
        nb_joueurs = int(nb_joueurs)
        nb_lettres = int(nb_lettres)
        nb_lignes = int(nb_lignes)
        nb_colonnes = int(nb_colonnes)
        grille = initGrille(nb_lettres, nb_lignes, nb_colonnes) # initGrille renvoie None si les valeurs ne sont pas bonnes
    
    # ---
    # Initialisation des varibles utilisés dans la boucle du jeu
    # ---

    print(trait)
    print("MEMORY")
    # Permet aux joueurs de ne pas remonter voir le résultat
    antiTriche = "\n"*30
    # Créer une matrice avec le même nombre d'éléments que la grille avec False comme valeurs
    visible = initMarked(nb_lignes, nb_colonnes) 
    score = [0 for i in range(nb_joueurs)]
    # Créer une matrice avec le même nombre d'éléments que la grille avec True comme valeurs 
    # pour savoir si la partie est finis ou non
    visibleComplet = initMarkedTrue(nb_lignes, nb_colonnes) 
    melange(grille)
    fini = False

    # ---
    # Boucle du jeu
    # ---

    while visible != visibleComplet: # Tant que les cases ne sont pas toutes visibles
        for joueur in range(1, nb_joueurs + 1):
            rejouer = True # Permet au joueur de rejouer quand il gagne un point
            # Regarde si la partie est fini ou non
            if not fini:
                while rejouer:
                    case_joue = [] # Contient la paire que l'utilisateur essaye
                    for i in range(2): # Pour que l'utilisateur puisse tester une paire
                        print(f"Scores : {score}")
                        display(grille, visible)
                        print(f"Joueur {joueur} :")
                        position = askPosition(visible)
                        # askPosition renvoie () si la case demandée est déjà visible
                        while position == ():
                            position = askPosition(visible)
                        visible[position[0]][position[1]] = True
                        case_joue.append(position)

                    premierEssai = case_joue[0]
                    deuxiemeEssai = case_joue[1]
                    # Si le joueur gagne le tour
                    if grille[premierEssai[0]][premierEssai[1]] == grille[deuxiemeEssai[0]][deuxiemeEssai[1]]:
                        score[joueur - 1] += 1
                        # Si la partie est fini
                        if visible == visibleComplet:
                            rejouer = False
                            display(grille, visible)
                            fini = True
                        else:
                            display(grille, visible)
                            input(f"Le joueur {joueur} rejoue ! (Appuyez sur entrée pour continuer)")
                    else:
                        display(grille, visible)
                        input(f"Le joueur {joueur} a finis son tour, au prochain ! (Appuyez sur entrée pour continuer)")
                        print(antiTriche)
                        visible[premierEssai[0]][premierEssai[1]] = False
                        visible[deuxiemeEssai[0]][deuxiemeEssai[1]] = False
                        rejouer = False
                    
    
    # ---
    # Fin de partie
    # ---

    # Permet de gérer les ex aequo
    phraseMilieu = ""
    maxScore = max(score)
    nbGagnant = 0
    lstGagnant = []
    for indexJoueur in range(len(score)):
        if score[indexJoueur] == maxScore:
            nbGagnant += 1
            lstGagnant.append(indexJoueur)
            if nbGagnant == 1:
                phraseMilieu += f"{indexJoueur + 1}"
            else:
                phraseMilieu += f", {indexJoueur + 1}"
    
    if nbGagnant == 1:
        print(f"Le joueur {phraseMilieu} a gagné !")
    else:
        print(f"Les joueurs {phraseMilieu} ont gagnés !")
    print(f"Liste des scores: {score}")


if __name__ == "__main__":
    memory()