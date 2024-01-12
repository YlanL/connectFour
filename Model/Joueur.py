from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
import random



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(numCoul : int) -> dict :
    """
    Fonction qui créé un joueur avec ses attributs
    :param numCoul:numéro de la couleur des pions du joueur
    :return: un dictionnaire contenant les attibuts du joueur
    """
    joueur={}
    if type(numCoul) != int :
        raise TypeError ("construireJoueur : Le paramètre n’est pas un entier")
    if numCoul > 1 or numCoul < 0 :
        raise ValueError (" construireJoueur : L’entier donné ",numCoul," n’est pas une couleur. ")
    joueur={const.COULEUR : numCoul, const.PLATEAU : None, const.PLACER_PION : None}
    return joueur

def getCouleurJoueur(joueur)->int :
    """
    Fonction qui renvoie la couleur des pions du joueur
    :param joueur: le joueur dont on cherche la couleur
    :return: le numéro de la couleur des pions du joueurs
    """
    if not type_joueur(joueur) :
        raise TypeError ("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur)->list :
    """
    Fonction qui renvoie le plateau de jeu
    :param joueur: le joueur
    :return: la liste 2D contenant le plateau
    """
    if not type_joueur(joueur):
        raise TypeError ("getPlateauJoueur : le paramètre ne correspond pas à un joueur ")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur):
    """
    Fonction qui renvoie la fonction
    :param joueur: le joueur
    :return:la fonction const.PLACER_PION du joueur
    """
    if not type_joueur(joueur):
        raise TypeError ("getPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]


def getPionJoueur(joueur):
    """
    Fonction qui créé un pion en fonction de la couleur du joueur
    :param joueur: le joueur
    :return: le pion
    """
    if not type_joueur(joueur) :
        raise TypeError ("getPionJoueur : Le paramètre ne correspond pas à un joueur")
    return construirePion(joueur[const.COULEUR])

def setPlateauJoueur(joueur,plateau) -> None:
    """
    fonction qui affecte au joueur le plateau passé en paramètre
    :param joueur: le joueur
    :param plateau: le plateau
    :return: None
    """
    if not type_joueur(joueur) :
        raise TypeError ("setPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    if not type_plateau(plateau):
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU]=plateau
    return None

def setPlacerPionJoueur(joueur, fonct) -> None:
    print(type(fonct))
    if not type_joueur(joueur) :
        raise TypeError ("setplacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    if not callable(fonct) :
        raise TypeError ("setPlacerPionJoueur : le second paramètre n’est pas une fonction ")
    joueur[const.PLACER_PION]=fonct
    return None

def _placerPionJoueur(joueur)->int:
    alea=round((const.NB_COLUMNS-1)*random.random())
    bon=False
    while bon == False :
        if joueur[const.PLATEAU][0][alea] == None :
            bon = True
        alea=round((const.NB_COLUMNS-1)*random.random())
    return alea

def initialiserIAJoueur(joueur,booleen:bool)->None:
    setPlacerPionJoueur(joueur,_placerPionJoueur)
    return None

