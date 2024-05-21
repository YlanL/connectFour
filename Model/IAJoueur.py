from Model.Pion import *
from Model.Joueur import*
from Model.Constantes import *
from Model.Plateau import *
import copy
import random


def placerPionJoueurIA (joueur) -> int:
    """
    Fonction qui place un pion mais pas selon certains critères
    :param joueur: le joueur
    :return: la ligne où est placé le pion
    """
    res = -1
    coulAdversaire = (joueur[const.COULEUR]+1) % 2
    pionAdv = construirePion(coulAdversaire)
    pion = construirePion(joueur[const.COULEUR])
    tab = []
    tab2 = []
    tab1 = []
    col = 0
    while res == -1 and col < const.NB_COLUMNS-1:
        col2 = 0
        if not type_pion(joueur[const.PLATEAU][0][col]):
            tab = copy.deepcopy(joueur[const.PLATEAU])
            tab1 = copy.deepcopy(joueur[const.PLATEAU])
            if placerPionPlateau(tab, pion, col) > 0 and len(getPionsGagnantsPlateau(tab)) > 0:
                res = col
            else:
                if placerPionPlateau(tab1, pionAdv, col) > 0 and len(getPionsGagnantsPlateau(tab1)) > 0:
                    res = col
                else:
                    while res == -1 and col2 <= col:
                        tab2 = copy.deepcopy(tab1)
                        if placerPionPlateau(tab2, pionAdv, col2) > 0 and len(getPionsGagnantsPlateau(tab2)) > 0:
                            res = col
                            print("d")
                        col2 += 1
        col += 1
    while res == -1:
        alea = random.randint(0, const.NB_COLUMNS-1)
        if not type_pion(joueur[const.PLATEAU][0][alea]):
            res = alea
            print("e")
        alea = random.randint(0, const.NB_COLUMNS - 1)
    return res

