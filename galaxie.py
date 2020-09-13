"""
fichier galaxie.py

Martin Canals

DIU EIL

Projet pédagogique découverte de la notion de graphe

"""
""" version 1
galaxie = { "A" : ["G" , "D","H" ],
            "B" : ["C" , "E"],
            "C" : ["E"],
            "D" : ["H" , "C"],
            "E" : ["F" , "G"],
            "F" : ["B" , "C",],
            "G" : ["D"],
            "H" : ["A"]  } 
"""
galaxie = { "A" : ["B" ,"C","D","E"],
            "B" : ["G" , "F"],
            "C" : ["G","H","K"],
            "D" : ["I", "H", "L"],
            "E" : ["F", "I","M"],
            "F" : ["A"],
            "G" : ["A"],
            "H" : ["A"],
            "I" : ["A"],
          "J" : ["M","N","B"],
          "K" :["J","P","C"],
          "L" :["K","R","D"],
          "M" :["L","T","E"],
          "N" :["O"],
          "O" :["U"],
          "P" : ["Q"],
          "Q" : ["K"],
          "R" : ["S","V"],
          "S" : ["L"],
          "T" : ["M"],
          "U" : ["V"],
          "V" : ["U"]} 
visites = set(["A"])

def message1() :
    print("Explore systématiquement toutes les destinations et dessine la carte")
def message2() :
    print(" vous ne pouvez pas connaitre les destinations d'une étoile non découverte ")
def message3() :
    print(" Je vois que tu as fait le tour de la question et que tu n'a toujours \n pas trouvé Terminus")
    print(" La planète qui abrite la fondation est un secret bien gardé.")
    print(" Je vais te donner une indication : ")
    print(" Aller sur Terminus depuis Trantor nécessite au minimum 6 étapes")
def message4() :
    print(" Le parcours pour aller sur Terminus est incorrect")
def message5() :
    print(" Bravo !!")
    print(" Tu as trouvé la planète et un chemin pour y aller, mais est-ce le plus court ? ")
    
    
conseil_a_donner = message1
etoiles = set (galaxie.keys())

def destinations(etoile) :
    global conseil_a_donner
    if etoile in etoiles :etoiles.remove(etoile)
    if etoiles == set() :
        conseil_a_donner = message3
    if etoile in visites :
        voisins = galaxie[etoile]
        for star in voisins : visites.add(star)       
        return voisins
    message2()  # Tentative sur une etoile non encore visitée

def verifie_parcours(parcours) :
    if len(parcours) == 0 :
        message4() 
        return False

    if parcours[0] != "A" or parcours[-1] !="U" :
        message4() 
        return False

    for i in range(len(parcours) -1 ) :
        if parcours[i+1] not in destinations(parcours[i]): 
            message4() 
            return False
    message5()
    return True

def conseil() :
    conseil_a_donner()

