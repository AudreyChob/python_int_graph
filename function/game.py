import os
import sys
from random import randint
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur
from ficheResultats import FicheResultats
sys.path.append("../python_int_graph/function")
from calculs import *



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
        print("score du dé : ",des_array[i].score)
        i += 1
    return des_array

def garder_des(des_array, Joueur, nb_relance):
    """
        permet de selectionner les des à garder
    """
    # print(len(des_array))
    # des_array = lance_des(nb_des)
    joueur = Joueur
    array_des_gardes = joueur.des_gardes
    # print(array_des_gardes)
    #nb_des_a_lancer = 5 -len(array_des_gardes)
    i =0
    
    if nb_relance == 1: 
        while i < len(des_array):
            array_des_gardes.append(des_array[i].score)
            i += 1
    else:       
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
            
    joueur.des_gardes = array_des_gardes
    print("Vous avez choisi de garder les dés suivant (liste des scores): ",joueur.des_gardes)
    return joueur.des_gardes


def nb_des_relancer(Joueur):
    """
        définir le nb de dès à relancer 
    """
    joueur = Joueur
    array_des_gardes =joueur.des_gardes
    # print(joueur.des_gardes)
    nb_des_a_relancer = 5 -len(array_des_gardes)
    # print('nb relance',nb_des_a_relancer)
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
    print("choix 13 : " +joueur.fiche.chance[1] + " score : " + str(joueur.fiche.chance[2]))
    print(joueur.fiche.total2[1] + " score : " + str(joueur.fiche.total2[2]))
    print(joueur.fiche.totaux[1] + " score : " + str(joueur.fiche.totaux[2]))


def selection_case(Joueur):
    """
        Selectionner case de score à remplir,
    """
    joueur = Joueur
    case = 0
    score = 0
    is_ok = False
    is_dispo = True
    while is_ok == False: 
        if is_dispo == False:
            case = input("Saisissez une case disponible!")
        else: 
            case = input("Quelle case souhaitez vous remplir ?")
        while case not in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
            case = input("Saisissez une case existante!")
        for i in joueur.fiche.iter_attributes():
            index = i[1][0]
            if index == int(case) and i[1][3] == True:
                is_ok = True  
                i[1][3] = False
                break
            is_dispo = False
        score = choix_calcul(joueur, index)
        i[1][2] = score
        # print(i)
        



def choix_calcul(Joueur, index_case):
    """
        Choix des la fonction de calcul du score
        correspondant à la case choisi
    """
    joueur = Joueur
    score = 0
    if index_case == 1:
        score = calcul_t_1(joueur)
    if index_case == 2:
        score = calcul_t_2(joueur)
    if index_case == 3:
        score = calcul_t_3(joueur)
    if index_case == 4:
        score = calcul_t_4(joueur)
    if index_case == 5:
        score = calcul_t_5(joueur)
    if index_case == 6:
        score = calcul_t_6(joueur)
    if index_case == 7:
        score = calcul_brelan(joueur)
    if index_case == 8:
        score = calcul_carre(joueur)
    if index_case == 9:
        score = calcul_full(joueur)
    if index_case == 10:
        score = calcul_p_suite(joueur)
    if index_case == 11:
        score = calcul_g_suite(joueur)
    if index_case == 12:
        score = calcul_yams(joueur)
    if index_case == 13:
        score = calcul_chance(joueur)
    print("score",score)
    return score


def calcul_totals(Joueur):
    """
        calcul des totals de la fiche de score 
    """
    joueur = Joueur
    fiche = joueur.fiche
    scores = joueur.fiche
    fiche.score_inter[2] = total_intermediaire(joueur)
    fiche.bonus[2] = bonus(joueur)
    fiche.total1[2] = total_sup(joueur)
    fiche.total2[2] = total_inf(joueur)
    fiche.totaux[2] = totaux(joueur)
    print("inter", fiche.score_inter[2], 'bonus',fiche.bonus[2], "total1",fiche.total1[2], "total2",fiche.total2[2], "totaux",fiche.totaux[2])


def vainqueur(joueur_array):
    """
        Definir le vainqueur de la partie
    """
    

# joueur= Joueur()
#start_game()  
# # lance_des(5)
# # garder_des(lance_des(5), Joueur)
# nb_des_relancer(Joueur)
# grille_result(Joueur)
# selection_case(joueur)
# calcul_totals(joueur)
