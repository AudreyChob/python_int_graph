import os
import sys
sys.path.append("../python_int_graph/common")
from joueur import Joueur
from de import De
from ficheresultat import Ficheresultat
from random import randint

def calcul_total_de_1(Joueur):
    """ calcul score total_de_1 """
    i = 0 
    joujou = Joueur
    tot1 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 1:
            tot1 += 1
        i += 1
    return tot1

def calcul_total_de_2(Joueur):
    """ calcul score total_de_2 """
    i = 0 
    joujou = Joueur
    tot2 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 2:
            tot2 += 2
        i += 1
    return tot2

def calcul_total_de_3(Joueur):
    """ calcul score total_de_3 """
    i = 0 
    joujou = Joueur
    tot3 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 3:
            tot3 += 3
        i += 1
    return tot3

def calcul_total_de_4(Joueur):
    """ calcul score total_de_4 """
    i = 0 
    joujou = Joueur
    tot4 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 4:
            tot4 += 4
        i += 1
    return tot4

def calcul_total_de_5(Joueur):
    """ calcul score total_de_5 """
    i = 0 
    joujou = Joueur
    tot5 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 5:
            tot5 += 5
        i += 1
    return tot5

def calcul_total_de_6(Joueur):
    """ calcul score total_de_6 """
    i = 0 
    joujou = Joueur
    tot6 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde == 6:
            tot6 += 1
        i += 6
    return tot6


def calcul_t_inter(Joueur):
    """ calcul score total intermediaire """
    joujou = Joueur
    t_inter = calcul_total_de_1(joujou)+calcul_total_de_2(joujou)
    +calcul_total_de_3(joujou)+calcul_total_de_4(joujou)
    +calcul_total_de_5(joujou)+calcul_total_de_6(joujou)
    return t_inter

def calcul_bonus(Joueur):
    """ calcul bonnus en cas de scor interm > 63 """
    joujou = Joueur
    t_inter = calcul_t_inter(joujou)
    bonus = 0
    if t_inter > 63:
        bonus = 35
    return bonus

def calcul_total_1(Joueur):
    """ calcul 1er sous total """
    joujou = Joueur
    t_inter = calcul_t_inter(joujou)
    bonus = calcul_bonus(joujou)
    total_1 = t_inter + bonus
    return total_1
    


def calcul_brelan(Joueur):
    """ calcul score brelan """
    joujou = Joueur
    total_brelan = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
            print(key , " ", value)
            if value >= 3:
                total_brelan = key*3
                print(total_brelan)
    return total_brelan



def calcul_carre(Joueur):
    """ calcul score carre """
    joujou = Joueur
    total_carre = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
            print(key , " ", value)
            if value >= 4:
                total_carre = key*3
                print(total_carre)
    return total_carre

def calcul_yams(Joueur):
    """ calcul score yams """
    joujou = Joueur
    total_yams = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
            print(key , " ", value)
            if value >= 5:
                total_yams = key*3
                print(total_yams)
    return total_yams


def calcul_chance(Joueur):
    """ calcul score chance """
    joujou = Joueur
    de_garde = joujou.de_garde
    total_chance = 0
    for d in de_garde:
        total_chance += d
    return total_chance


def calcul_full(Joueur):
    """ calcul score chance """
    joujou = Joueur
    total_full = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    print(compte)
    for key, value in compte.items():
            print(key , " ", value)
            if value >= 3:
                total_brelan = key*3
                print(total_brelan)
    return total_full




joujou=Joueur()
calcul_full(joujou)


