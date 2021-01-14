from ficheResultats import FicheResultats

class Joueur: 

    def __init__(self):
        self.nom = ""
        self.score = 0
        self.jeu = 12
        self.des_gardes = [5,3,2,4,6]
        #self.lance = 3
        self.fiche = FicheResultats()