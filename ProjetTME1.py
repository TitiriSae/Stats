import numpy as np

dico = {0 : ("vide", 0), 
        1 : ("torpilleur", 2),
        2 : ("sous-marin", 3),
        3 : ("contre-torpilleur", 3),
        4 : ("croiseur", 4),
        5 : ("porte-avion", 5),
        -1 : ("touché", -1)}

class bateau :
    def __init__(self, id) : 
        if id in list(dico.keys())[1:-1] : 
            self.id = id
            self.nom = dico[id][0]
            self.taille = dico[id][1]
        else : 
            print("identifiant invalide")



class plateau :
    def __init__(self) :
        self.plate = np.array([[0 for i in range (10)] for i in range(10)])
        
    def aff(self) :
        print(self.plate)

    def peut_placer(self, bateau, position, direction):
        """Fonction qui prend en argument une grille, un bateau, une position et une direction (horizontal, vertical)
        Elle retourne True s'il est possible de placer le bateau à la position et dans la direction souhaitée sur la grille."""

        if not (direction == 1 or direction == 2) :
            return False

        if direction == 1 :
            if not (0 <= position[1] <= 10-bateau.taille) or not (0 <= position[0] <= 9) :
                return False
        else : 
            if not (0 <= position[0] <= 10-bateau.taille) or not (0 <= position[1] <= 9) :
                return False

        for i in range(bateau.taille):
            if(direction ==1) : # disposition horizontale
                if self.plate[position[0]][position[1]+i] != 0 :
                    return False
                  
            else : #disposition verticale
                if self.plate[position[0]+i][position[1]] != 0 :
                    return False
        return True