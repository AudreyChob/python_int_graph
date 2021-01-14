import os
import sys
sys.path.append("../python_int_graph/common")
from joueur import Joueur
from de import De
from ficheresultat import Ficheresultat
from random import randint


def debut_jeu():
    """enregistrement des joueur + nb de joueur"""
    nb_joueur = int(input("Combien y a t\'il de joueur ?"))
    joueur_array = []
    i = 0 
    if(nb_joueur <= 0):
        print("il faut au minimum un joueur ")
    elif(nb_joueur >6):
        print("il ne peux y avoir que 6 joueur au maximum")
    else:
        while i < nb_joueur:
            j = Joueur()
            j.nom = input("comment s'appelle le joueur :")
            joueur_array.append(j)
            # print(joueur_array[i].nom)
            i += 1
    return joueur_array

def lancer_de(nb_de):
    """ simule un lancé de dé"""
    d = 0
    de_array = []
    while d < nb_de:
        de = De()
        de.nom = "De" + str(d+1)   
        de.score = randint(1,6)
        de_array.append(de)
        print(de_array[d].score)
        d += 1
    return de_array

def garder_de(de_array,Joueur):
    """permet de choisir le dé que l'on va conserver"""
    joujou = Joueur
    i = 0
    de_garde_array = joujou.de_garde
    while i < len(de_array):
        rep_gard_de = input("voulez vous garder le dé " + str(de_array[i].nom) + " avec un score de : " + str(de_array[i].score) + " ? o/n ")
        if rep_gard_de == "o":
            de_garde_array.append(de_array[i].score) 
            print("cool, suivant")
            i += 1
        elif rep_gard_de == "n":
            print("pas cool, next")
            i += 1
        else:
            print("PUT** c est OUI ou c est NON ????") 
    joujou.de_garde = de_garde_array
    print("Vous avez garde :")
    print(joujou.de_garde)
    return joujou.de_garde


def nb_de_lancer(Joueur):
    """calcule le nombre de de a lancer"""
    joujou = Joueur
    nb = 5 - len(joujou.de_garde)
    return nb

def grille_resultat(Joueur):
    """affiche la gille de résultat"""
    joujou = Joueur
    print("Choix n°",joujou.fiche.t_de_1[0]," ",joujou.fiche.t_de_1[1],"score : ",joujou.fiche.t_de_1[2])
    print("Choix n°",joujou.fiche.t_de_2[0]," ",joujou.fiche.t_de_2[1],"score : ",joujou.fiche.t_de_2[2])
    print("Choix n°",joujou.fiche.t_de_3[0]," ",joujou.fiche.t_de_3[1],"score : ",joujou.fiche.t_de_3[2])
    print("Choix n°",joujou.fiche.t_de_4[0]," ",joujou.fiche.t_de_4[1],"score : ",joujou.fiche.t_de_4[2])
    print("Choix n°",joujou.fiche.t_de_5[0]," ",joujou.fiche.t_de_5[1],"score : ",joujou.fiche.t_de_5[2])
    print("Choix n°",joujou.fiche.t_de_6[0]," ",joujou.fiche.t_de_6[1],"score : ",joujou.fiche.t_de_6[2])
    print(joujou.fiche.t_inter[1],"score : ",joujou.fiche.t_inter[2])
    print(joujou.fiche.bonus[1],"score : ",joujou.fiche.bonus[2])
    print(joujou.fiche.total_1[1]," : ",joujou.fiche.total_1[2])
    print("Choix n°",joujou.fiche.brelan[0]," ",joujou.fiche.brelan[1],"score : ",joujou.fiche.brelan[2])
    print("Choix n°",joujou.fiche.carre[0]," ",joujou.fiche.carre[1],"score : ",joujou.fiche.carre[2])
    print("Choix n°",joujou.fiche.full[0]," ",joujou.fiche.full[1],"score : ",joujou.fiche.full[2])
    print("Choix n°",joujou.fiche.ptt_suite[0]," ",joujou.fiche.ptt_suite[1],"score : ",joujou.fiche.ptt_suite[2])
    print("Choix n°",joujou.fiche.gd_suite[0]," ",joujou.fiche.gd_suite[1],"score : ",joujou.fiche.gd_suite[2])
    print("Choix n°",joujou.fiche.yams[0]," ",joujou.fiche.yams[1],"score : ",joujou.fiche.yams[2])
    print("Choix n°",joujou.fiche.chance[0]," ",joujou.fiche.chance[1],"score : ",joujou.fiche.chance[2])
    print(joujou.fiche.total_2[1]," : ",joujou.fiche.total_2[2])
    print(joujou.fiche.total_glob[1]," : ",joujou.fiche.total_glob[2])

def selection_case(Joueur):
    """ le joueur selectione la case a remplir"""
    joujou = Joueur
    case = 0
    case = input("quelle case voulez vous remplir ?")
    while case not in ('1','2','3','4','5','6','7','8','9','10','11','12','13'):
        case = input("veuillez entrer un choix valide, quelle case voulez vous remplir ?")
    
    for i in joujou.fiche.iter_attributes():
        if i[1][0] == int(case) and i[1][3] == True:
            i[1][3] = False
            break
        else:
            case = input("la case n'est pas disponible, quelle case voulez vous remplir ?")



joujou = Joueur()
selection_case(joujou)