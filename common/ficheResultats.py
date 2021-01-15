class FicheResultats: 
    
    def __init__(self):
        self.t_1 = [1,'total 1',0, True]
        self.t_2 = [2,'total 2',0, True]
        self.t_3 = [3,'total 3',0, True]
        self.t_4 = [4,'total 4',0, True]
        self.t_5 = [5,'total 5',0, True]
        self.t_6 = [6,'total 6',0, True]
        self.brelan = [7,'brelan',0, True] #total 3 des
        self.carre = [8,'carre',0, True] #total 4 des
        self.full = [9,'full',0, True] #25pts
        self.p_suite = [10,'petite suite',0, True] #30pts
        self.g_suite = [11,'grande suite',0, True] #40pts
        self.yams = [12,'yams',0, True] #50pts
        self.chance = [13,'chance',0, True] #total 5 dés
        self.score_inter = [14,'total intermédiaire',0, True]
        self.bonus = [15,'bonus',0, True] #35pts si scoreInter>63
        self.total1 = [16,'total partie sup',0, True] #scoreInter + bonus
        self.total2 = [17,'total partie inf',0, True]
        self.totaux = [18,'total',0, True] #total1 + total2
        
    def iter_attributes(self):
        return iter(self.__dict__.items())


