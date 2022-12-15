from random import randint
def position_tresor(n:int, m:int) -> tuple:
    """
    Donne une position aléatoire du trésor
    :param n: n définis la valeur minimum de la position du trésor
    :param m: m définis la valeur maximum de la position du trésor
    :type n: int
    :type m: int
    :return: renvoie un couple de coordonnés
    :rtype: tuple
    """
    latitude_tresor=randint(n,m)
    longitude_tresor=randint(n,m)
    return latitude_tresor,longitude_tresor
    
def creer_une_liste(taille:int) -> list:
    """
    Créer une liste d'une taille souhaitée
    :param taille: définis la taille de la liste
    :type taille: int
    :return: une liste avec des valeurs de 0 à taille-1
    :rtype list
    """
    liste=[]
    for i in range(taille):
        liste.append(i)
    return liste

def chasse_tresor_manuel():
    """
    Permet de demander à l'utilisateur de trouver les coordonnées du trésor choisi de manière aléatoire
    """
    tresor="inconnu"
    latitude_tresor,longitude_tresor=position_tresor(0,99)
    nombre_essai=10
    while tresor != "trouvé" and nombre_essai > 0:
        print("Nombre d'essai restant :",nombre_essai)
        latitude = int(input("Entrer une latitude :"))
        longitude = int(input("Entrer une longitude :"))
        nombre_essai -= 1
        if latitude_tresor == latitude and longitude_tresor == longitude:
            tresor="trouvé"
            print("Gagner")
            break
        if latitude_tresor > latitude:
            print("Latitude trop petite")
        elif latitude_tresor < latitude:
            print("Latitude trop grande")
        else:
            print("Bonne Latitude")
        if longitude_tresor > longitude:
            print("longitude trop petite")
        elif longitude_tresor < longitude:
            print("longitude trop grande")
        else:
            print("Bonne Longitude")
    if nombre_essai == 0:
        print("Essai épuisé")
        print("Latitude du trésor : ", latitude_tresor, "Longitude du trésor : ", longitude_tresor)

def chasse_tresor_dichotomie() -> int:
    """
    Retourne le nombre d'essai que la recherche dichotomique a effectuée
    :return: nombre d'essai
    :rtype: int
    """
    latitude_tresor,longitude_tresor = position_tresor(0,99)
    latitude = creer_une_liste(100)
    longitude = creer_une_liste(100)
    essai_latitude = dichotomie(latitude, latitude_tresor)
    essai_longitude = dichotomie(longitude, longitude_tresor)
    return min(essai_latitude, essai_longitude)
    
def dichotomie(liste:list, nombre:int, nombre_essai=10):
    """
    recherche dichotomique de la chasse au trésor.
    :param liste: liste où on cherche l'élément
    :param nombre: valeur qu'on cherche dans la liste
    :param nombre_essai: nombre d'essai 
    :type liste
    :return: retourne le nombre d'essai que la fonction lui reste
    :rtype: int or str
    """
    milieu = len(liste)//2
    if nombre_essai == 0:
        return("Essai épuisé")
    nombre_essai -= 1
    if liste[milieu] == nombre:
        return ("Essai restant :",nombre_essai)
    elif liste[milieu] < nombre:
        liste = liste[milieu:len(liste)]
        return dichotomie(liste,nombre,nombre_essai)
    else:
        liste = liste[0:milieu]
        return dichotomie(liste,nombre,nombre_essai)
    
    
