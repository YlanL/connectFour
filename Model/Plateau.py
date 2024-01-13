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

def construirePlateau() -> list:
    """Fonction permettant de construire un pion

    :return: Retourne une liste de liste sur NB_LINES x NB_COLUMNS contenant des None
    """
    plat = []
    for i in range(const.NB_LINES):
        ligne = []
        for j in range(const.NB_COLUMNS):
            ligne.append(None)
        plat.append(ligne)
    return plat

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
    if numCol < 0 or numCol >= const.NB_COLUMNS :
        raise ValueError (f" placerPionPlateau : La valeur de la colonne {numCol} n’est pas correcte")
    while i<const.NB_LINES and not (type_pion(plateau[i][numCol])):
        numLigne = i
        i+=1
    print(numLigne)
    if numLigne > -1 :
        plateau[numLigne][numCol]=pion
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
            if plateau[ligne][i]!=None and plateau[ligne][i+1]!=None and plateau[ligne][i+2]!=None and plateau[ligne][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne][i+1]) == numCoul and getCouleurPion(plateau[ligne][i+2]) == numCoul and getCouleurPion(plateau[ligne][i+3]) == numCoul :
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
    Fonction qui retourne les 4 premiers pions d'une certaine couleur étant alignés verticalement pour chaques lignes
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
        for i in range(const.NB_COLUMNS-3) :
            if plateau[ligne][i]!=None and plateau[ligne+1][i+1]!=None and plateau[ligne+2][i+2]!=None and plateau[ligne+3][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne+1][i+1]) == numCoul and getCouleurPion(plateau[ligne+2][i+2]) == numCoul and getCouleurPion(plateau[ligne+3][i+3]) == numCoul and plateau[ligne][i] not in res and plateau[ligne+1][i+1] not in res and plateau[ligne+2][i+2] not in res and plateau[ligne+3][i+3] not in res:
                for u in range(4):
                    res.append(plateau[ligne+u][i+u])
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
        for i in range(const.NB_COLUMNS-3):
            if plateau[ligne][i]!=None and plateau[ligne-1][i+1]!=None and plateau[ligne-2][i+2]!=None and plateau[ligne-3][i+3]!=None and getCouleurPion(plateau[ligne][i]) == numCoul and getCouleurPion(plateau[ligne-1][i+1]) == numCoul and getCouleurPion(plateau[ligne-2][i+2]) == numCoul and getCouleurPion(plateau[ligne-3][i+3]) == numCoul and plateau[ligne][i] not in res and plateau[ligne-1][i+1] not in res and plateau[ligne-2][i+2] not in res and plateau[ligne-3][i+3] not in res:
                for u in range(4):
                    res.append(plateau[ligne-u][i+u])
            print(res)
    return res

#test 4 diagonalIndirecte
pion={const.COULEUR:const.ROUGE,const.ID:None}
#plat=[[None,None,None,pion,None,None,pion],[None, None,{const.COULEUR:const.ROUGE,const.ID:4},None,None,pion,None],[None,pion,pion,None,pion,None,None],[pion,None,None,pion,None,None,None],[None,None,pion,None,None,None,None],[None,None,None,None,None,None,None]]
#plat=[[None,None,None,None,{const.COULEUR:const.ROUGE,const.ID:1},{const.COULEUR:const.ROUGE,const.ID:10},None],[None,None,None,{const.COULEUR:const.ROUGE,const.ID:2},{const.COULEUR:const.ROUGE,const.ID:11},None,None],[None,None,{const.COULEUR:const.ROUGE,const.ID:3},{const.COULEUR:const.ROUGE,const.ID:12},None,None,None],[None,{const.COULEUR:const.ROUGE,const.ID:4},{const.COULEUR:const.ROUGE,const.ID:13},None,None,None,None],[{const.COULEUR:const.ROUGE,const.ID:5},{const.COULEUR:const.ROUGE,const.ID:14},None,None,None,None,None],[{const.COULEUR:const.ROUGE,const.ID:15},None,None,None,None,None,None]]
#print(len(detecter4diagonaleIndirectePlateau(plat,1)))
def getPionsGagnantsPlateau(plateau)->list:
    print(plateau,type_plateau(plateau))
    """
    Fonction qui détermine les pions qui ont une position de victoiresur le plateau
    :param plateau: le plateau de jeu
    :return:liste des pions
    """
    if not type_plateau(plateau):
        raise TypeError("getPionsGagnantsPlateau: Le premier paramètre ne correspond pas à un plateau")
    res=[]
    for coul in range(len(const.COULEURS)):
        res+=detecter4horizontalPlateau(plateau,coul)
        res+=detecter4verticalPlateau(plateau,coul)
        res+=detecter4diagonaleDirectePlateau(plateau,coul)
        res+=detecter4diagonaleIndirectePlateau(plateau,coul)
    return res
#test 4 diagonaldirecte
#pion={const.COULEUR:const.ROUGE,const.ID:None}
#plat=[[None,None,None,pion,None,None,pion],[None, None,{const.COULEUR:const.ROUGE,const.ID:4},None,None,pion,None],[None,pion,pion,None,pion,None,None],[pion,None,None,pion,None,None,None],[None,None,pion,None,None,None,None],[None,None,None,None,None,None,None]]
#print(getPionsGagnantsPlateau(plat))

def isRempliPlateau(plateau)->bool :
    """
    Fonction qui détermine si le plateau est rempli de pion ou non
    :param plateau: le plateau de jeu
    :return: un booléen selon si le plateau est rempli (True) ou si il ne l'est pas "False"
    """
    if not type_plateau(plateau):
        raise TypeError(" isRempliPlateau : Le paramètre n’est pas un plateau ")
    rempli = True
    i=0
    while i < const.NB_LINES and rempli == True :
        u=0
        while u < const.NB_COLUMNS and rempli == True :
            if not type_pion(plateau[i][u]) :
                rempli = False
            u+=1
        i+=1
    return rempli
#test rempli
#pion={const.COULEUR:const.ROUGE,const.ID:None}
#l=[pion,pion,pion,pion,pion,pion,pion]
#plat=[l,l,l,l,l,l]
#plat2=[l,l,l,l,l,[None,None,None,None,None,None,None]]
#print(isRempliPlateau(plat),isRempliPlateau(plat2))

def placerPionLignePlateau(plateau : list, pion :dict , numLigne , left : bool) -> tuple :
    """
    Fonction qui place un pion sur une extrémité de ligne
    :param plateau: le plateau de jeu
    :param pion: le pions à placer sur le plateau
    :param numLigne:le numéro de la ligne où placer le pion
    :left: un booléen qui correspond au coté où le pion est inséré
    :return: les pions qui ont été poussés
    """
    caseVide=const.NB_COLUMNS
    i=0
    res=[]
    last=None
    ligne=[]
    res = res + [pion]
    if left :
        while i<const.NB_COLUMNS and caseVide == const.NB_COLUMNS :
            if not type_pion(plateau[numLigne][i]):
                caseVide=i
            i+=1
        for u in range(caseVide):
            res = res + [plateau[numLigne][u]]
        if numLigne != 0 and not type_pion(plateau[numLigne - 1][i-1]) and type_pion(plateau[numLigne][0]) and i < const.NB_COLUMNS:
            last = (placerPionPlateau(plateau, plateau[numLigne][caseVide - 1], caseVide))
        elif caseVide == const.NB_COLUMNS:
            last = const.NB_LINES
        for u in range(const.NB_COLUMNS):
            if u >= len(res):
                ligne += [None]
            else :
                ligne += [res[u]]
        plateau[numLigne] = ligne
    else:
        while const.NB_COLUMNS-i-1>=0 and caseVide == const.NB_COLUMNS :
            if not type_pion(plateau[numLigne][const.NB_COLUMNS-i-1]):
                caseVide=i
            i+=1
        for u in range (caseVide):
            res = res + [plateau[numLigne][const.NB_COLUMNS-1-u]]
        if numLigne!=const.NB_LINES-1 and not type_pion(plateau[numLigne-1][const.NB_COLUMNS-i-1-1]) and type_pion(plateau[numLigne][const.NB_COLUMNS-1]) and i < const.NB_COLUMNS:
            last = placerPionPlateau(plateau,plateau[numLigne][const.NB_COLUMNS-caseVide],caseVide)
        elif caseVide == const.NB_COLUMNS:
            last = const.NB_LINES
        print(caseVide)
        for u in range (const.NB_COLUMNS-1,-1,-1):
            if u >= len(res):
                ligne += [None]
            else :
                ligne += [res[u]]
    plateau[numLigne] = ligne
    return (res,last)

def encoderPlateau(plateau)->str:
    """
    Fonction qui encode un plateau en forme textuel
    :param plateau: plateau
    :return: le plateau encodé
    """
    if not type_plateau(plateau):
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau.")
    res=""
    for i in range(const.NB_COLUMNS):
        for u in range(const.NB_LINES):
            if not type_pion(plateau[i][u]):
                res+="_"
            else:
                if getCouleurPion(plateau[i][u])==0:
                    res += "J"
                else :
                    res += "R"
    return res


