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
        if joujou.de_garde[i] == 1:
            tot1 += 1
        i += 1
    return tot1

def calcul_total_de_2(Joueur):
    """ calcul score total_de_2 """
    i = 0 
    joujou = Joueur
    tot2 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde[i] == 2:
            tot2 += 2
        i += 1
    return tot2

def calcul_total_de_3(Joueur):
    """ calcul score total_de_3 """
    i = 0 
    joujou = Joueur
    tot3 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde[i] == 3:
            tot3 += 3
        i += 1
    return tot3

def calcul_total_de_4(Joueur):
    """ calcul score total_de_4 """
    i = 0 
    joujou = Joueur
    tot4 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde[i] == 4:
            tot4 += 4
        i += 1
    return tot4

def calcul_total_de_5(Joueur):
    """ calcul score total_de_5 """
    i = 0 
    joujou = Joueur
    tot5 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde[i] == 5:
            tot5 += 5
        i += 1
    return tot5

def calcul_total_de_6(Joueur):
    """ calcul score total_de_6 """
    i = 0 
    joujou = Joueur
    tot6 = 0
    while i < len(joujou.de_garde):
        if joujou.de_garde[i] == 6:
            tot6 += 6
        i += 1
    return tot6


def calcul_t_inter(Joueur):
    """ calcul score total intermediaire """
    joujou = Joueur
    t_inter = (joujou.fiche.t_de_1[2] + joujou.fiche.t_de_2[2] 
    + joujou.fiche.t_de_3[2] + joujou.fiche.t_de_4[2] +
    joujou.fiche.t_de_5[2] + joujou.fiche.t_de_6[2])
    return t_inter

def calcul_bonus(Joueur):
    """ calcul bonnus en cas de score interm > 63 """
    joujou = Joueur
    t_inter = joujou.fiche.t_inter[2]
    bonus = 0
    if t_inter > 63:
        bonus = 35
    return bonus

def calcul_total_1(Joueur):
    """ calcul 1er sous total """
    joujou = Joueur
    t_inter = joujou.fiche.t_inter[2]
    bonus = joujou.fiche.bonus[2]
    total_1 = t_inter + bonus
    return total_1
    


def calcul_brelan(Joueur):
    """ calcul score brelan """
    joujou = Joueur
    total_brelan = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    for key, value in compte.items():
            if value >= 3:
                total_brelan = key*3
    return total_brelan



def calcul_carre(Joueur):
    """ calcul score carre """
    joujou = Joueur
    total_carre = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    for key, value in compte.items():
            if value >= 4:
                total_carre = key*4
    return total_carre

def calcul_yams(Joueur):
    """ calcul score yams """
    joujou = Joueur
    total_yams = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    for key, value in compte.items():
            if value >= 5:
                total_yams = 50
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
    """ calcul score full """
    joujou = Joueur
    total_full = 0
    compte = {}.fromkeys(set(joujou.de_garde),0)
    for valeur in joujou.de_garde: 
        compte[valeur] += 1
    if len(compte) != 2:
        total_full = 0
    else:
        for key, value in compte.items():
            if value == 2 or value == 3:
                total_full = 25
    return total_full
                

def calcul_ptt_suite(Joueur):
    """ calcul score petite suite """
    joujou = Joueur
    total_ptt_suite = 0
    suite = joujou.de_garde
    suite.sort()
    if suite == [1,2,3,4,5]:
        total_ptt_suite = 30
    return total_ptt_suite

def calcul_gd_suite(Joueur):
    """ calcul score gde suite """
    joujou = Joueur
    total_gd_suite = 0
    suite = joujou.de_garde
    suite.sort()
    if suite == [2,3,4,5,6]:
        total_gd_suite = 40
    return total_gd_suite

def calcul_total_2(Joueur):
    """ calcul 2e sous total """
    joujou = Joueur
    total_2 = (joujou.fiche.brelan[2] + joujou.fiche.carre[2] 
    + joujou.fiche.full[2] + joujou.fiche.yams[2] +
    joujou.fiche.ptt_suite[2] + joujou.fiche.gd_suite[2])
    return total_2

def calcul_total_glob(Joueur):
    """ calcul score global """
    joujou = Joueur
    total_glob = (joujou.fiche.total_1[2] + joujou.fiche.total_2[2])
    return total_glob


