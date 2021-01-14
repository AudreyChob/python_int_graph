class Ficheresultat:
    def __init__(self):
        self.t_de_1 = [1,"Total de 1",0,False]
        self.t_de_2 = [2,"Total de 2",0,True]
        self.t_de_3 = [3,"Total de 3",0,True]
        self.t_de_4 = [4,"Total de 4",0,True]
        self.t_de_5 = [5,"Total de 5",0,True]
        self.t_de_6 = [6,"Total de 6",0,True]
        self.brelan = [7,"Total brelan",0,True] #total des 3 dés
        self.carre = [8,"Total carrre",0,True] #total des 4 dé
        self.full = [9,"Total full",0,True] #25 pt
        self.ptt_suite = [10,"Total petite suite",0,True] #30 pt
        self.gd_suite = [11,"Total grande suite",0,True] #40 pt
        self.yams = [12,"Total yams",0,True] #50pt
        self.chance = [13,"Total chance",0,True] #total de 5 dé
        self.t_inter = [14,"Total intermediaire",0,True]
        self.bonus = [15,"Bonus",0,True] #si t_inter > 63, = 35pt
        self.total_1 = [16,"Total de la partie supérieure",0,True] # total partie sup
        self.total_2 = [17,"Total partie inferieure",0,True] #total partie inf
        self.total_glob = [18,"Score total",0,True] #total 1 + 2 

    def iter_attributes(self):
        return iter(self.__dict__.items())


