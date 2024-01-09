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

def placerPionPlateau(plateau : list, pion : dict, numCol :int) -> int :
    """
    fonction qui place un pion dans un plateau à une colonnes numCol
    :param plateau: le plateau de jeu
    :param pion: le pion à placer
    :param numCol: numéro de la colonne où lacher le pion
    :return: le numéro de la ligne où se situe le pion laché, -1 si impossible
    """
    print(numCol,plateau)
    numLigne=-1
    i=0
    if not type_plateau(plateau):
        raise TypeError ("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if not type_pion(pion):
        raise TypeError ("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(numCol)!=int :
        raise TypeError ("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if numCol < 0 or numCol > const.NB_COLUMNS :
        raise ValueError (f" placerPionPlateau : La valeur de la colonne {numCol} n’est pas correcte")
    while i<const.NB_LINES and not type_pion(plateau[i][numLigne]):
        i+=1
        numLigne=i-1
    print(numLigne)
    return numLigne

def detecter4horizontalPlateau(plateau, numCoul) -> list:
    """
    Fonction qui retourne les 4 premiers pions d'une certaine couleur étant alignés horizontalement pour chaques lignes
    :param plateau:le plateau de jeu
    :param numCoul: la couleur des pions dont l'alignement est à tester
    :return: une liste contenant les premiers pions alignés pour chaque lignes si ils éxistent
    """
    res=[]
    if not type_plateau(plateau):
        raise TypeError ("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(numCoul) != int :
        raise TypeError ("detecter4horizontalPlateau : le second paramètre n’est pas un entier")
    if numCoul != 0 and numCoul!=1 :
        raise ValueError ("détecter4horizontalPlateau : La valeur de la couleur ",numCoul," n’est pas correcte")
    for ligne in range(const.NB_LINES):
        aligne=False
        i=0
        while i < const.NB_COLUMNS-3 and aligne == False :
            if plateau[ligne][i]!=None and plateau[ligne][i+1]!=None and plateau[ligne][i+2]!=None and plateau[ligne][i+3]!=None and getCouleurPion(plateau[ligne][i+1]) == getCouleurPion(plateau[ligne][i]) and getCouleurPion(plateau[ligne][i+1]) == getCouleurPion(plateau[ligne][i+2]) and getCouleurPion(plateau[ligne][i+2]) == getCouleurPion(plateau[ligne][i+3]) and plateau[ligne][i][const.COULEUR] == numCoul :
                aligne=True
                for u in range (4):
                    res.append(plateau[ligne][i+u])
            i+=1
    return res

#test 4 horizontal
#plat=[[None,None,None,{const.COULEUR:const.JAUNE,const.ID:1},{const.COULEUR:const.JAUNE,const.ID:2},{const.COULEUR:const.JAUNE,const.ID:3},{const.COULEUR:const.JAUNE,const.ID:4}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:7}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:8}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:9}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:10}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:11}]]
#print(detecter4horizontalPlateau(plat,0))

def detecter4verticalPlateau(plateau:list, numCoul :int)-> list :
    """
    Fonction qui retourne les 4 premiers pions d'une certzinr couleur étant alignés verticalement pour chaques lignes
    :param plateau: le plateau de jeu
    :paramnumCoul: le numéro de la couleur des pions dont l'alignement est à tester
    :return: une liste contenant les premiers pions alignés pour chaque lignes si ils éxistent
    """
    res=[]
    if not type_plateau(plateau):
        raise TypeError ("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(numCoul) != int :
        raise TypeError ("detecter4verticalPlateau : le second paramètre n’est pas un entier")
    if numCoul != 0 and numCoul!=1 :
        raise ValueError ("detecter4verticalPlateau : La valeur de la couleur ",numCoul," n’est pas correcte")
    for col in range(const.NB_COLUMNS):
        i=0
        aligne=False
        while i<const.NB_LINES-3 and aligne==False:
            if plateau[i][col]!=None and plateau[i+1][col]!=None and plateau[i+2][col]!=None and plateau[i+3][col]!=None and getCouleurPion(plateau[i][col]) == numCoul and getCouleurPion(plateau[i+1][col]) == numCoul and getCouleurPion(plateau[i+2][col]) == numCoul and getCouleurPion(plateau[i+3][col]) == numCoul :
                aligne=True
                for u in range(4):
                    res.append(plateau[i+u][col])
            i+=1
    return res

#test 4 vertical
#plat=[[None,None,None,{const.COULEUR:const.JAUNE,const.ID:1},{const.COULEUR:const.JAUNE,const.ID:2},{const.COULEUR:const.JAUNE,const.ID:3},{const.COULEUR:const.JAUNE,const.ID:4}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:7}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:8}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:9}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:10}],[None,None,None,None,None,None,{const.COULEUR:const.JAUNE,const.ID:11}]]
#print(detecter4verticalPlateau(plat,0))

def detecter4diagonaleDirectePlateau(plateau,numCoul:int)->list:
    """
    Fonction qui détermine les pions d'une couleur aligné sur une diagonale direct
    :param plateau: le plateau de jeu
    :param numCoul:le numéro de la couleur des pions
    :return: une liste contenant les pions alignés selon une diagonale direct
    """
    res = []
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(numCoul) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : le second paramètre n’est pas un entier")
    if numCoul != 0 and numCoul != 1:
        raise ValueError("détecter4diagonaleDirectePlateau : La valeur de la couleur ", numCoul, " n’est pas correcte")
    for ligne in range(const.NB_LINES-3):
        i=0
        diag=False
        while i < const.NB_COLUMNS-3 and diag == False :
            if plateau[ligne][i]!=None and plateau[ligne+1][i+1]!=None and plateau[ligne+2][i+2]!=None and plateau[ligne+3][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne+1][i+1]) == numCoul and getCouleurPion(plateau[ligne+2][i+2]) == numCoul and getCouleurPion(plateau[ligne+3][i+3]) == numCoul :
                diag=True
                for u in range(4):
                    res.append(plateau[ligne+u][i+u])
            i+=1
    return res

#test 4 diagonaldirecte
#pion={const.COULEUR:const.ROUGE,const.ID:None}
#plat=[[pion,None,pion,None,None,None,None],[None, {const.COULEUR:const.ROUGE,const.ID:4},pion,pion,None,None,None],[None,None,pion,None,pion,None,None],[None,None,None,pion,None,pion,None],[None,None,None,None,pion,None,None],[None,None,None,None,None,None,None]]
#print(detecter4diagonaleDirectePlateau(plat,1))

def detecter4diagonaleIndirectePlateau(plateau,numCoul:int)->list:
    """
    Fonction qui détermine les pions d'une couleur aligné sur une diagonale indirect
    :param plateau: le plateau de jeu
    :param numCoul:le numéro de la couleur des pions
    :return: une liste contenant les pions alignés selon une diagonale indirect
    """
    res = []
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(numCoul) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : le second paramètre n’est pas un entier")
    if numCoul != 0 and numCoul != 1:
        raise ValueError("detecter4diagonaleIndirectePlateau : La valeur de la couleur ", numCoul, " n’est pas correcte")
    for ligne in range(3,const.NB_LINES):
        i=0
        diag=False
        while i < const.NB_COLUMNS-3 and diag == False :
            if plateau[ligne][i]!=None and plateau[ligne-1][i+1]!=None and plateau[ligne-2][i+2]!=None and plateau[ligne-3][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne-1][i+1]) == numCoul and getCouleurPion(plateau[ligne-2][i+2]) == numCoul and getCouleurPion(plateau[ligne-3][i+3]) == numCoul :
                diag = True
                for u in range(4):
                    res.append(plateau[ligne-u][i+u])
            i+=1
    return res

#test 4 diagonaldirecte
#pion={const.COULEUR:const.ROUGE,const.ID:None}
#plat=[[None,None,None,pion,None,None,pion],[None, None,{const.COULEUR:const.ROUGE,const.ID:4},None,None,pion,None],[None,pion,pion,None,pion,None,None],[pion,None,None,pion,None,None,None],[None,None,pion,None,None,None,None],[None,None,None,None,None,None,None]]
#print(detecter4diagonaleIndirectePlateau(plat,1))