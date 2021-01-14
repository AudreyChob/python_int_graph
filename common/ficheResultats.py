class FicheResultats: 
    
    def __init__(self):
        self.t_1 = ['total 1',0, True]
        self.t_2 = ['total 2',0, True]
        self.t_3 = ['total 3',0, True]
        self.t_4 = ['total 4',0, True]
        self.t_5 = ['total 5',0, True]
        self.t_6 = ['total 6',0, True]
        self.score_inter = ['total intermédiaire',0, True]
        self.bonus = ['bonus',0, True] #35pts si scoreInter>63
        self.total1 = ['Total partie sup',0, True] #scoreInter + bonus
        self.brelan = ['brelan',0, True] #total 3 des
        self.carre = ['carre',0, True] #total 4 des
        self.full = ['full',0, True] #25pts
        self.p_suite = ['petite suite',0, True] #30pts
        self.g_suite = ['grande suite',0, True] #40pts
        self.yams = ['yams',0, True] #50pts
        self.chance = ['chance',0, True] #total 5 dés
        self.total2 = ['total partie inf',0, True]
        self.totaux = ['Total',0, True] #total1 + total2
        



