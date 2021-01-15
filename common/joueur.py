from ficheResultats import FicheResultats

class Joueur: 

    def __init__(self):
        self.nom = "joueur"
        self.score = 0
        self.jeu = 5
        self.des_gardes = []
        #self.lance = 3
        self.fiche = FicheResultats()

    def iter_attributes(self):
        return iter(self.__dict__.items())