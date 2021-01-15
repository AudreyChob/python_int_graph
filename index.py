import os
import sys
sys.path.append("../python_int_graph/common")
sys.path.append("../python_int_graph/function")
from joueur import Joueur
from de import De
from jeu import *


joueur_array = debut_jeu()
print("Debut du jeu")
nombrejeu = 2
while nombrejeu > 0:
    for j in joueur_array:
        nb_relance = 3 
        print(j.nom," joue")
        while nb_relance > 0:
            nb_de = nb_de_lancer(j)
            de_array = lancer_de(nb_de)
            garder_de(de_array,j,nb_relance)
            calcul_total(j)
            nb_relance -= 1
        grille_resultat(j)
        selection_case(j)
        calcul_total(j)
        j.de_garde = []
    nombrejeu -= 1
    calcul_total(j)
    grille_resultat(j)
vainqueur(joueur_array)
