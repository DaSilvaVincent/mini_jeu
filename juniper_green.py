def multiples(n:int, nMax:int) -> list:
    """
    Permet d'avoir les multiples du nombre n
    :param n: on recherche les multiples du nombre n
    :param nMax: la valeur max de la liste retournée
    :type n: int
    :type nMax: int
    :return: une liste avec les multiples de n
    :rtype: list
    """
    nombres_multiples = []
    compteur = 2
    while n * compteur <= nMax:
        nombres_multiples.append(n * compteur)
        compteur += 1
    return nombres_multiples

def diviseur(n:int) -> list:
    """
    Permet d'avoir les diviseurs du nombre n
    :param n: on recherche les diviseurs du nombre n
    :type n:int
    :return: une liste avec les diviseurs de n
    :rtype: list
    """
    nombres_diviseurs = []
    for i in range(1, n-1):
        if n % i == 0:
            nombres_diviseurs.append(i)
    return nombres_diviseurs

def union(lst1:list, lst2:list) -> list:
    """
    Permet de fusionner 2 listes
    :param lst1: 1er liste à concatener
    :param lst2: 2ème liste à concatener
    :type lst1: list    
    :type lst2: list
    :return: liste fusionné
    :rtype: list
    """
    return lst1 + lst2

def filtres(M:list, R:list):
    """
    Filtre la 1er liste avec les éléments de la 2ème liste
    :param M: 1er liste contenant des éléments à enlever
    :param R: Liste d'éléments qu'on veut supprimer dans la liste M
    :type M: list
    :type R: list
    """
    for nombre in R:
        while nombre in M: # Permet de gérer les doublons
            M.remove(nombre)
            
def est_pair(nb:int) -> bool:
    """
    Renvoie vrai ou faux si le nombre est pair
    :param nb: le nombre à décider si il est pair ou impair
    :type nb: int
    :return: Retourne True si le nombre est pair et False si il est impaire
    :rtype: bool
    """
    return nb % 2 == 0

# Fonction principale
def juniperGreen():
    """
    Lance le jeu du juniper green
    """
    nMax = int(input("Quelle est la valeur max du tableau ? (entier positif uniquement)\n"))
    # Création d'une liste ayant toutes les valeurs que les joueurs peuvent utiliser en compréhension
    liste_jeu = [i for i in range(1, nMax + 1)]
    
    print("---Joueur 1---")
    nombre_choisis = int(input("Choisissez le premier nombre (il doit être pair et entre 1 et {})\n".format(nMax)))
    # Cas où l'utilisateur met un nombre incorrect
    while not est_pair(nombre_choisis) or nombre_choisis > nMax:
        print("Le nombre n'est pas pair ou n'est pas entre 1 et {}\n".format(nMax))
        nombre_choisis = int(input("Joueur 1\nChoisissez le premier nombre (il doit être pair et entre 1 et {})\n".format(nMax)))
    
    # On enlève le nombre donné de la liste
    filtres(liste_jeu, [nombre_choisis])
    jeu = True
    # Numéro du joueur
    n_joueur = 2
    
    while jeu:
        # Toutes les possibilités possibles
        possibilite = union(multiples(nombre_choisis, nMax), diviseur(nombre_choisis))
        possibilite_avec_liste_jeu = []
        
        # Toutes les possiblités possibles incluses dans la liste du jeu
        for nombre in possibilite:
            if nombre in liste_jeu:
                possibilite_avec_liste_jeu.append(nombre)
        
        # Si il n'y a aucune possibilité alors un joueur gagne
        if len(possibilite_avec_liste_jeu) == 0:
            if n_joueur == 1:
                print("Joueur 2 a gagné")
                jeu = False
            else:
                print("Joueur 1 a gagné")
                jeu = False
        else:
            print("---Joueur {}---".format(n_joueur))
            print(liste_jeu)
            nombre_choisis = int(input("Choisis ton nombre\n"))
            # Si le joueur inscrit un nombre qui n'est ni un multiple ni un diviseur du nombre choisis
            while nombre_choisis not in possibilite_avec_liste_jeu:
                print("Le nombre n'est pas valide")
                print(liste_jeu)
                nombre_choisis = int(input("Choisis ton nombre\n"))
            # On enlève ce nombre de la liste du jeu
            filtres(liste_jeu, [nombre_choisis])
            
            # On change de joueur
            if n_joueur == 1:
                n_joueur = 2
            else:
                n_joueur = 1
            