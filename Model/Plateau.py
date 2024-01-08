from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau()->list :
    """
    Fonction qui construit le plateau de jeu
    :return:
    """
    tab=[]
    ligne=[]
    #le plateau possède un même nombre de ligne pour chaques colonnes
    for i in range(const.NB_COLUMNS):
        ligne.append(None)
    for i in range(const.NB_LINES):
        tab.append(ligne)
    return tab

def placerpinPlateau(plateau : list, pion : dict, numCol :int) -> int :
    """
    fonction qui place un pion dans un plateau à une colonnes numCol
    :param plateau: le plateau de jeu
    :param pion: le pion à placer
    :param numCol: numéro de la colonne où lacher le pion
    :return: le numéro de la ligne où se situe le pion laché, -1 si impossible
    """
    numLigne=-1
    i=0
    if type(plateau)!=list :
        raise TypeError ("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(pion)!=dict:
        raise TypeError ("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(numCol)!=int :
        raise TypeError ("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if numCol < 0 or numCol >const.NB_COLUMNS :
        raise ValueError (f" placerPionPlateau : La valeur de la colonne {numCol} n’est pas correcte")
    while const.NB_LINES-i >0 and numLigne == -1:
        if plateau[const.NB_LINES-i][numCol] == None:
            numLigne=const.NB_LINES-i
        i+=1
    return numLigne

def detecter4horizontalPlateau(plateau, numCoul) -> list:
    """

    :param plateau:
    :param numCoul:
    :return:
    """
    aligne = False
    i=0
    res=[]
    if type(plateau) != list :
        raise TypeError ("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(numCoul) != int :
        raise TypeError ("detecter4horizontalPlateau : le second paramètre n’est pas un entier")
    if numCoul != 0 and numCoul!=1 :
        raise ValueError ("détecter4horizontalPlateau : La valeur de la couleur ",numCoul," n’est pas correcte")
    for ligne in range(len(plateau)):
        aligne=False
        i=0
            if plateau[ligne][i]!=None and plateau[ligne][i+1]!=None and plateau[ligne][i+2]!=None and plateau[ligne][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne][i+1]) == getCouleurPion(plateau[ligne][i]) and getCouleurPion(plateau[ligne][i+1]) == getCouleurPion(plateau[ligne][i+2]) and getCouleurPion(plateau[ligne][i+2]) == getCouleurPion(plateau[ligne][i+3]):
                aligne=True
                for u in range (4):
                    res.append(plateau[ligne][i+u])
            i+=1
    return res

#test 4 horizontal
pion={'Couleur':const.JAUNE,'id':None}
plat=[[None,None,None,{'Couleur':const.JAUNE,'id':1},{'Couleur':const.JAUNE,'id':2},{'Couleur':const.JAUNE,'id':3},{'Couleur':const.JAUNE,'id':4}],[None,None,None,None,None,None,{'Couleur':const.JAUNE,'id':7}],[None,None,None,None,None,None,{'Couleur':const.JAUNE,'id':8}],[None,None,None,None,None,None,{'Couleur':const.JAUNE,'id':9}],[None,None,None,None,None,None,{'Couleur':const.JAUNE,'id':10}],[None,None,None,None,None,None,{'Couleur':const.JAUNE,'id':11}]]
print(detecter4horizontalPlateau(plat,0))






