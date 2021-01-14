from ficheResultats import FicheResultats

class Joueur: 

    def __init__(self):
        self.nom = ""
        self.score = 0
        self.jeu = 12
        self.des_gardes = [5,5,6,4,5]
        #self.lance = 3
        self.fiche = FicheResultats()