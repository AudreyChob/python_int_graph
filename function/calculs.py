import os
import sys
from random import randint
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur
from ficheResultats import FicheResultats


def calcul_t_1(Joueur):
    """
        calcul du total de 1 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_1 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 1: 
            score_t_1 +=1
        i +=1
    return score_t_1


def calcul_t_2(Joueur):
    """
        calcul du total de 2 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_2 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 2: 
            score_t_2 +=2
        i +=1
    return score_t_2

def calcul_t_3(Joueur):
    """
        calcul du total de 3 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_3 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 3: 
            score_t_3 +=3
        i +=1
    return score_t_3

def calcul_t_4(Joueur):
    """
        calcul du total de 4 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_4 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 4: 
            score_t_4 +=4
        i +=1
    return score_t_4

def calcul_t_5(Joueur):
    """
        calcul du total de 5 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_5 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 5: 
            score_t_5 +=5
        i +=1
    #print(score_t_5)
    return score_t_5

def calcul_t_6(Joueur):
    """
        calcul du total de 6 
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    score_t_6 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 6: 
            score_t_6 +=6
        i +=1
    return score_t_6

def total_intermediaire(Joueur):
    """
        calcul total intermediaire
    """
    joueur = Joueur
    scores = joueur.fiche
    score_inter = (scores.t_1[2] + scores.t_2[2] 
                   + scores.t_3[2] + scores.t_4[2] +
                   scores.t_5[2] + scores.t_6[2])
    #print(score_inter)
    return score_inter

def bonus(Joueur):
    """
        attribution bonus
    """
    joueur = Joueur
    score_inter = joueur.fiche.score_inter[2]
    bonus = 0
    if score_inter > 63:
        bonus = 35
    return bonus


def total_sup(Joueur):
    """
        calcul total partie supérieure
    """
    joueur = Joueur
    score_inter = joueur.fiche.score_inter[2]
    tot_bonus = joueur.fiche.bonus[2]
    total_sup = score_inter + tot_bonus
    return total_sup

def calcul_brelan(Joueur):
    """
        calcul score brelan
    """
    joueur = Joueur
    des_gardes = joueur.des_gardes
    total_brelan = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    # print(compte)
    for key, value in compte.items():
        # print(key , " ", value)
        #print(compte.values())
        if value >= 3:
            total_brelan = key*3
            # print(total_brelan)
    return total_brelan


def calcul_carre(Joueur):
    """
        calcul score carre
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    total_carre = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    # print(compte)
    for key, value in compte.items():
        # print(key , " ", value)
        #print(compte.values())
        if value >= 4:
            total_carre = key*4
            # print(total_carre)
    return total_carre


def calcul_full(Joueur):
    """
        calcul score full
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    total_full = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    # print(compte)
    for key, value in compte.items():
        #print(key , " ", value)
        #print(compte.values())
        if len(compte) != 2:
            total_full = 0
        else : 
            if value == 3 or value == 2:
                total_full = 25
        #print(total_full)
    return total_full
    

def calcul_p_suite(Joueur):
    """
        calcul score petite suite
    """
    joueur = Joueur
    total_p_suite = 0
    des_gardes = joueur.des_gardes
    des_gardes.sort()
    # print(des_gardes)
    if des_gardes == [1,2,3,4,5]:
        total_p_suite = 30
    # print(total_p_suite)
    return total_p_suite


def calcul_g_suite(Joueur):
    """
        calcul score grande suite
    """
    joueur = Joueur
    total_g_suite = 0
    des_gardes = joueur.des_gardes
    des_gardes.sort()
    # print(des_gardes)
    if des_gardes == [2,3,4,5,6]:
        total_g_suite = 40
    # print(total_g_suite)
    return total_g_suite


def calcul_yams(Joueur):
    """
        calcul score grande yams
    """
    joueur = Joueur
    i = 0
    des_gardes = joueur.des_gardes
    total_yams = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    # print(compte)
    for key, value in compte.items():
        # print(key , " ", value)
        #print(compte.values())
        if value >= 5:
            total_yams = 50
            # print(total_yams)
    return total_yams


def calcul_chance(Joueur):
    """
        calcul score chance
    """
    joueur = Joueur
    des_gardes = joueur.des_gardes   
    total_chance = 0
    for de in des_gardes:
        total_chance += de
        # print(total_chance)
    return total_chance


def total_inf(Joueur):
    """
        calcul total partie inférieure
    """
    joueur = Joueur
    scores = joueur.fiche
    
    total_inf = (scores.brelan[2] + scores.carre[2]+ scores.full[2] +scores.p_suite[2] + scores.g_suite[2] + scores.yams[2]+ scores.chance[2])
    return total_inf 


def totaux(Joueur):
    """
        calcul total du score final
    """
    joueur = Joueur
    scores = joueur.fiche

    totaux = scores.total1[2] + scores.total2[2]
    return totaux      

# calcul_t_5(Joueur)
# total_intermediaire(Joueur)
joueur = Joueur()
calcul_g_suite(joueur)