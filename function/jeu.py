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


def nb_de_lancer(Joueur):
    """calcule le nombre de de a lancer"""
    joujou = Joueur
    nb = 5 - len(joujou.de_garde)
    return nb

def grille_resultat(Joueur):
    """affiche la gille de résultat"""
    joujou = Joueur
    print(joujou.fiche.t_de_1[0],"score : ",joujou.fiche.t_de_1[1])
    print(joujou.fiche.t_de_2[0],"score : ",joujou.fiche.t_de_2[1])
    print(joujou.fiche.t_de_3[0],"score : ",joujou.fiche.t_de_3[1])
    print(joujou.fiche.t_de_4[0],"score : ",joujou.fiche.t_de_4[1])
    print(joujou.fiche.t_de_5[0],"score : ",joujou.fiche.t_de_5[1])
    print(joujou.fiche.t_de_6[0],"score : ",joujou.fiche.t_de_6[1])
    print(joujou.fiche.t_inter[0],"score : ",joujou.fiche.t_inter[1])
    print(joujou.fiche.bonus[0],"score : ",joujou.fiche.bonus[1])
    print(joujou.fiche.total_1[0]," : ",joujou.fiche.total_1[1])
    print(joujou.fiche.brelan[0],"score : ",joujou.fiche.brelan[1])
    print(joujou.fiche.carre[0],"score : ",joujou.fiche.carre[1])
    print(joujou.fiche.full[0],"score : ",joujou.fiche.full[1])
    print(joujou.fiche.ptt_suite[0],"score : ",joujou.fiche.ptt_suite[1])
    print(joujou.fiche.gd_suite[0],"score : ",joujou.fiche.gd_suite[1])
    print(joujou.fiche.yams[0],"score : ",joujou.fiche.yams[1])
    print(joujou.fiche.chance[0],"score : ",joujou.fiche.chance[1])
    print(joujou.fiche.total_2[0]," : ",joujou.fiche.total_2[1])
    print(joujou.fiche.total_glob[0]," : ",joujou.fiche.total_glob[1])




joujou = Joueur()
