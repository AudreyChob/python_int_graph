import os
import sys
sys.path.append("../python_int_graph/common")
from joueur import Joueur
from de import De
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
    print(joujou.de_garde)

    print("Vous avez garde :")
    print(joujou.de_garde)

    


joujou = Joueur()
garder_de(lancer_de(2),joujou)

