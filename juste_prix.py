from os import lstat
from random import *

def nombre_aleatoire() -> int:
    """
    Permet de choisir un nombre aléatoire entre 1 et 1000
    :return: un nombre aléatoire
    :rtype: int
    """
    return randint(1,1000)

def creer_liste() -> list:
    """
    Permet de créer une liste allant de 0 à 999
    :return: Retourne une liste allant de 0 à 999
    :rtype: list
    """
    liste=[]
    for i in range(1000):
        liste.append(i)
    return liste

def est_trier(liste:list) -> bool:
    """
    Vérifie si la liste rentré en argument est trié ou non
    :param liste: une liste quelconque
    :type liste: list
    :return: Renvoie si la liste est trié ou non
    :rtype: bool
    """
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

def trier(liste:list) -> list:
    """
    Permet de trier une liste passé en argument si elle n'est pas trié
    :param liste: Une liste quelconque
    :type liste: list
    :return: Retourne la liste passé en argument triée
    :rtype: list
    """
    if not est_trier(liste):
        for i in range(len(liste)):
            referent = liste[i]
            rang=i
            while rang!=0 and liste[rang-1] > referent:
                liste[rang], liste[rang-1] = liste[rang-1], liste[rang]
                rang-=1
    return liste

def recherche_dichotomique(liste:list, valeur:int, nombre_essaie:int):
    """
    Permet de rechercher de manière dichotomique et récursif une valeur dans une liste avec un certain nombre d'essais
    :param liste: la liste où on cherche la valeur de manière dichotomique
    :param valeur: la valeur qu'on cherche dans la liste
    :param nombre_essaie: la recherche à le droit à un nombre d'essaies limité
    :type liste: list
    :type valeur: int
    :type nombre_essaie: int
    :return: retourne la valeur si l'élément est trouvé et False si il n'est pas trouvé
    :rtype: int or bool
    """
    trier(liste)
    longueur=len(liste)
    milieu=longueur//2
    # Permet d'arrêter le programme si on a plus d'essais
    if nombre_essaie==0:
        return False
    # Cran d'arret de la récursivité
    if liste[milieu]==valeur:
        nombre_essaie-=1
        print("l'ordinateur regarde : ",liste[milieu],"nombre d'essais restants : ",nombre_essaie)
        return milieu
    # Permet de travailler seulement sur la moitié de droite 
    elif liste[milieu]<valeur:
        nombre_essaie-=1
        print("l'ordinateur regarde : ",liste[milieu],"nombre d'essais restants : ",nombre_essaie)
        return recherche_dichotomique(liste[milieu:],valeur,nombre_essaie)
    # Permet de travailler seulement sur la moitié de gauche
    else:
        nombre_essaie-=1
        print("l'ordinateur regarde : ",liste[milieu],"nombre d'essais restants : ",nombre_essaie)
        return recherche_dichotomique(liste[:milieu],valeur,nombre_essaie)

def nombre_mystere_humain_contre_ordinateur():
    """
    Le jeu permet de choisir une valeur entre 1 et 1000
    et l'ordinateur doit deviner la valeur en 10 essais maximum pour gagner
    """
    liste=creer_liste()
    nombre_aleatoire=int(input("Entrez un nombre entre 1 et 1000\n"))
    #Permet de reposer la question jusqu'a avoir une valeur réglementaire
    while nombre_aleatoire>1000 or nombre_aleatoire<1:
        nombre_aleatoire=int(input("Entrez un nombre entre 1 et 1000\n"))
    nombre_essaie=10
    resultat=recherche_dichotomique(liste,nombre_aleatoire,nombre_essaie)
    if resultat==False:
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")
            
def nombre_mystere_ordinateur_contre_humain():
    """
    Le jeu fait choisir a l'ordinateur une valeur entre 1 et 1000 
    ensuite on doit essayer de le retrouver en 10 essais maximum pour gagner
    """
    liste=creer_liste()
    aleatoire=nombre_aleatoire()
    nombre_essaie=10
    while nombre_essaie>0:
        valeur=int(input("Entrez un nombre entre 1 et 1000\n"))
        if valeur==aleatoire:
            print("Vous avez gagné")
            return
        elif valeur>aleatoire:
            #Permet de savoir si la valeur est trop haute
            nombre_essaie-=1
            print("La valeur choisis est trop haute")
        elif valeur<aleatoire:
            #Permet de savoir si la valeur est trop faible 
            nombre_essaie-=1
            print("La valeur choisis est trop basse")
        else :
            #Permet de reposer la question jusqu'a rentrer une valeur réglementaire
            valeur=int(input("Entrez un nombre entre 1 et 1000\n"))
    print("Vous avez perdu car vous n'avez plus d'essais")