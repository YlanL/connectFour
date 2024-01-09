# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(numCouleur : int) -> dict:
    """
    Fonction qui construit un pion
    :param numCouleur: numéro de la couleur du pion
    :return:dictionnaire contenant les informations du pion
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(numCouleur) != int :
        raise TypeError ("construirePion : Le paramètre n’est pas de type entier")
    elif numCouleur!=0 and numCouleur!=1 :
        raise ValueError ("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")
    else:
        if numCouleur == 0 :
            pion ={const.COULEUR:const.JAUNE, const.ID:None }
        else :
            pion ={const.COULEUR:const.ROUGE, const.ID:None}
    return pion

def getCouleurPion(pion:dict)->int :
    """
    Fonction qui retourne la couleur du pion
    :param pion: dictionnaire correspondant à un pion
    :return: la couleur du pion
    """
    if not type_pion(pion):
        raise TypeError ("getCouleurPion : Le paramètre n’est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion:dict, numCouleur)->None:
    """
    Fonction qui retourne un pion de couleur associé à numCouleur
    :param pion: dictionnaire correspondant à un pion
    :param numCouleur: entier correspondant à la couleur du pion
    :return: None
    """
    if not type_pion(pion) :
        raise TypeError ("setCouleurPion : Le premier paramètre n’est pas un pion.")
    if type(numCouleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")
    if numCouleur != 0 and numCouleur != 1 :
        raise ValueError (" setCouleurPion : Le second paramètre ", numCouleur," n’est pas une couleur")
    else :
        if numCouleur == 0 :
            pion[const.COULEUR]=const.JAUNE
        else:
            pion[const.COULEUR]=const.ROUGE
    return None

def getIdPion(pion)->int:
    """
    Fonction qui retourne l'idenetifiant du pion
    :param pion: dictionnaire correspondant à un pion
    :return: l'indentifant du pion ou None si il n'en a pas
    """
    if not type_pion(pion) :
        raise TypeError ("getIdPion : Le paramètre n’est pas un pion.")
    return pion[const.ID]
def setIdPion (pion : dict,id : int) -> None :
    if not type_pion(pion) :
        raise TypeError ("setIdPion : Le premier paramètre n’est pas un pion.")
    if type(id) != int :
        raise TypeError (" setIdPion : Le second paramètre n’est pas un entier.")
    pion[const.ID] = id
    return None