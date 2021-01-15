from ficheResultats import FicheResultats

class Joueur: 

    def __init__(self):
        self.nom = "joueur"
        self.des_gardes = []
        self.fiche = FicheResultats()

    def iter_attributes(self):
        return iter(self.__dict__.items())