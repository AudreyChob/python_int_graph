import os
import sys
from random import randint
sys.path.append("../python_int_graph/common")
from de import De
from joueur import Joueur
from ficheResultats import FicheResultats


def calcul_t_1(joueur):
    """
        calcul du total de 1 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_1 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 1: 
            score_t_1 +=1
        i +=1
    return score_t_1


def calcul_t_2(joueur):
    """
        calcul du total de 2 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_2 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 2: 
            score_t_2 +=2
        i +=1
    return score_t_2

def calcul_t_3(joueur):
    """
        calcul du total de 3 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_3 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 3: 
            score_t_3 +=3
        i +=1
    return score_t_3

def calcul_t_4(joueur):
    """
        calcul du total de 4 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_4 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 4: 
            score_t_4 +=4
        i +=1
    return score_t_4

def calcul_t_5(joueur):
    """
        calcul du total de 5 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_5 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 5: 
            score_t_5 +=5
        i +=1
    # print(score_t_5)
    return score_t_5

def calcul_t_6(joueur):
    """
        calcul du total de 6 
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    score_t_6 = 0
    while i < len(des_gardes):
        if des_gardes[i] == 6: 
            score_t_6 +=6
        i +=1
    return score_t_6

def total_intermediaire(joueur):
    """"
        calcul total intermediaire
    """
    joueur = Joueur()
    score_inter = (calcul_t_1(joueur) + calcul_t_2(joueur) + calcul_t_3(joueur)
                  + calcul_t_4(joueur) + calcul_t_5(joueur) + calcul_t_6(joueur))
    print(score_inter)
    return score_inter

def bonus(joueur):
    """"
        attribution bonus
    """
    joueur = Joueur()
    score_inter = total_intermediaire(joueur)
    bonus = 0
    if score_inter > 63:
        bonus = 35
    return bonus


def total_sup(joueur):
    """"
        calcul total partie supérieure
    """
    joueur = Joueur()
    score_inter = total_intermediaire(joueur)
    bonus = bonus(joueur)
    total_sup = score_inter + bonus
    return total_sup

def calcul_brelan(joueur):
    """"
        calcul score brelan
    """
    joueur = Joueur()
    des_gardes = joueur.des_gardes
    total_brelan = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
        print(key , " ", value)
        # print(compte.values())
        if value >= 3:
            total_brelan = key*3
            print(total_brelan)
    return total_brelan


def calcul_carre(joueur):
    """"
        calcul score carre
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    total_carre = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
        print(key , " ", value)
        # print(compte.values())
        if value >= 4:
            total_carre = key*4
            print(total_carre)
    return total_carre


def calcul_full(joueur):
    """"
        calcul score full
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    total_full = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
        print(key , " ", value)
        # print(compte.values())
        if len(compte) > 2:
            total_full = 0
        if value == 3 and 2:
            total_full = 25
            print(total_full)
    return total_full
    

def calcul_p_suite(joueur):
    """"
        calcul score petite suite
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes


def calcul_g_suite(joueur):
    """"
        calcul score grande suite
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes 

def calcul_yams(joueur):
    """"
        calcul score grande yams
    """
    joueur = Joueur()
    i = 0
    des_gardes = joueur.des_gardes
    total_yams = 0
    compte = {}.fromkeys(set(des_gardes),0)
    for valeur in des_gardes: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
        print(key , " ", value)
        # print(compte.values())
        if value >= 5:
            total_yams = key*5
            print(total_yams)
    return total_yams


def calcul_chance(joueur):
    """"
        calcul score chance
    """
    joueur = Joueur()
    des_gardes = joueur.des_gardes   
    total_chance = 0
    for de in des_gardes:
        total_chance += de
        print(total_chance)
    return total_chance


# calcul_t_5(Joueur)
# total_intermediaire(Joueur)
calcul_full(Joueur)