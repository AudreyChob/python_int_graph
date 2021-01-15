"""
imports
"""
import sys
import os
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur
sys.path.append("../python_int_graph/function")
from game import *



joueur_array = start_game()
print("Que les joueurs entrent dans la reine !!")
nb_jeu = 12
fin_de_partie = False
while nb_jeu > 0:
    for j in joueur_array:  
        print(j.nom)
        nb_relance = 3
        while nb_relance > 0:
            nb_des = nb_des_relancer(j)
            print("nb_des",nb_des)
            des_array = lance_des(nb_des)
            garder_des(des_array ,j, nb_relance)
            nb_relance -= 1
            print("nb_relance",nb_relance)
        nb_relance = 3
        grille_result(j)
        selection_case(j)
        calcul_totals(j)
        j.des_gardes = []
        nb_jeu -= 1
    fin_de_partie = True
    

