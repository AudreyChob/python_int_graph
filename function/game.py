import os
import sys
from random import randint
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur
from ficheResultats import FicheResultats


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
            #print(joueurs_array[i].fiche)
            i+= 1
    return joueurs_array

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

def garder_des(des_array, Joueur):
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
    return joueur.des_gardes


def nb_des_relancer(Joueur):
    """
        définir le nb de dès à relancer 
    """
    joueur = Joueur
    array_des_gardes =joueur.des_gardes
    print(joueur.des_gardes)
    nb_des_a_relancer = 5 -len(array_des_gardes)
    print(nb_des_a_relancer)
    return nb_des_a_relancer


def grille_result(Joueur):
    """
        Afficher la grille + choix de la case à remplir 
        (avec le score)
    """
    joueur = Joueur
    print("choix 1 : " + joueur.fiche.t_1[1] + " score : " + str(joueur.fiche.t_1[2]))
    print("choix 2 : " +joueur.fiche.t_2[1] + " score : " + str(joueur.fiche.t_2[2]))
    print("choix 3 : " +joueur.fiche.t_3[1] + " score : " + str(joueur.fiche.t_3[2]))
    print("choix 4 : " +joueur.fiche.t_4[1] + " score : " + str(joueur.fiche.t_4[2]))
    print("choix 5 : " +joueur.fiche.t_5[1] + " score : " + str(joueur.fiche.t_5[2]))
    print("choix 6 : " +joueur.fiche.t_6[1] + " score : " + str(joueur.fiche.t_6[2]))
    print(joueur.fiche.score_inter[1] + " score : " + str(joueur.fiche.score_inter[2]))
    print(joueur.fiche.bonus[1] + " score : " + str(joueur.fiche.bonus[2]))
    print(joueur.fiche.total1[1] + " score : " + str(joueur.fiche.total1[2]))
    print("choix 7 : " +joueur.fiche.brelan[1] + " score : " + str(joueur.fiche.brelan[2]))
    print("choix 8 : " +joueur.fiche.carre[1] + " score : " + str(joueur.fiche.carre[2]))
    print("choix 9 : " +joueur.fiche.full[1] + " score : " + str(joueur.fiche.full[2]))
    print("choix 10 : " +joueur.fiche.p_suite[1] + " score : " + str(joueur.fiche.p_suite[2]))
    print("choix 11 : " +joueur.fiche.g_suite[1] + " score : " + str(joueur.fiche.g_suite[2]))
    print("choix 12 : " +joueur.fiche.yams[1] + " score : " + str(joueur.fiche.yams[2]))
    print("choix 13 : " +joueur.fiche.chance[1] + " score : " + str(joueur.fiche.total2[2]))
    print(joueur.fiche.total2[1] + " score : " + str(joueur.fiche.total2[2]))
    print(joueur.fiche.totaux[1] + " score : " + str(joueur.fiche.totaux[2]))


def selection_case(Joueur):
    """
        Selectionner case de score à remplir,
    """
    joueur = Joueur
    print(Joueur.fiche)
    case = 0
    # print(des_du_joueur)
    # print(FicheResultats)
    score = 0
    case = input("Quelle case souhaitez vous remplir ?")
    # while case not in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
    #     case = int(input("Saisissez une case existante!"))
    for i in joueur.fiche.iter_attributes():
        index = i[1][0]
        while case not in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
            case = input("Saisissez une case existante!")
        if index == int(case):
            print(type(case))
            print(index)
            print(i[1][3])
            if i[1][3] != True:
                case = input("Saisissez une case disponible!")
        i[1][3] = False



# def select_calculs

    


joueur= Joueur()
#start_game()  
# # lance_des(5)
# # garder_des(lance_des(5), Joueur)
# nb_des_relancer(Joueur)
# grille_result(Joueur)
selection_case(joueur)
