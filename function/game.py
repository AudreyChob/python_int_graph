import os
import sys
from random import randint
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur



def start_game():
    """
        enregistrement des joueurs 
        + nb joueur
    """
    joueurs_array = []
    nb_joueur = int(input("Combien y a t il de joueur?"))
    if nb_joueur <= 0: 
        print("il faut au moins un joueur pour débuter la partie")
    elif nb_joueur >6:
        print("le nombre maximum de joueurs est 6")
    else:
        i = 0
        while i < nb_joueur:
            j = Joueur()
            j.nom = input("Nom du joueur" + str(i+1) + ": ")
            joueurs_array.append(j)
            #print(joueurs_array[i].nom)
            i+= 1

def lance_des(nb_des):
    """
        simulation lancé de dés
    """
    des_array = []
    i = 0
    while i < nb_des:
        d = De()
        d.nom = "dès"+str(i+1)
        #print(d.nom)
        d.score = randint(1,6)
        #print(d.score)
        des_array.append(d)
        i += 1
    #print(des_array)
    return des_array

def garder_des(des_array, joueur):
    """
        permet de selectionner les des à garder
    """
    # print(len(des_array))
    # des_array = lance_des(nb_des)
    joueur = Joueur()
    array_des_gardes = joueur.des_gardes
    print(array_des_gardes)
    #nb_des_a_lancer = 5 -len(array_des_gardes)
    i =0
    while i < len(des_array):        
        rep_garde_des = input('Voulez vous garder le dés ' + str(i+1) + 
        " avec un score de " + str(des_array[i].score) + "? o/n")
        if rep_garde_des == "o":
            array_des_gardes.append(des_array[i].score)
            i += 1
        elif rep_garde_des == "n":
            print('dés remis en jeux')
            i += 1
        else: 
            print('Répondre par oui (o) ou non (n)')
    print("""Vous avez choisi de garder les dés
          suivant (liste des scores): """)
    joueur.des_gardes = array_des_gardes
    (print(joueur.des_gardes))


def nb_des_relancer(joueur):
    """
        définir le nb de dès à relancer 
    """
    joueur = Joueur()
    array_des_gardes =joueur.des_gardes
    print(joueur.des_gardes)
    nb_des_a_relancer = 5 -len(array_des_gardes)
    print(nb_des_a_relancer)
    return nb_des_a_relancer






# lance_des(5)
# garder_des(lance_des(5), Joueur)
nb_des_relancer(Joueur)


#startGame()  