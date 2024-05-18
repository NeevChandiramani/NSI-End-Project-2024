import pygame
import webbrowser
import time
import sys

#webbrowser.open('http://chess.neevchandiramani.com')
#time.sleep(3)

taille_écran = (1920, 1080)
taille_case = 1080 / 8
positionx = 420
positiony = 1080 - 135

#Fini
Cases_echiquier = {"A1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A2": pygame.Rect((positionx + 135 * 1, positiony), (taille_case, taille_case)), "A3": pygame.Rect((positionx + 135 *2, positiony), (taille_case, taille_case)), 
                   "A4": pygame.Rect((positionx + 135 * 3, positiony), (taille_case, taille_case)), "A5": pygame.Rect((positionx + 135 * 4, positiony), (taille_case, taille_case)), "A6": pygame.Rect((positionx + 135 * 5, positiony), (taille_case, taille_case)), 
                   "A7": pygame.Rect((positionx + 135 * 6, positiony), (taille_case, taille_case)), "A8": pygame.Rect((positionx + 135 * 7, positiony), (taille_case, taille_case)),

                   "B1": pygame.Rect((positionx, positiony - 135 * 1 ), (taille_case, taille_case)), "B2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 1), (taille_case, taille_case)), "B3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 1), (taille_case, taille_case)), 
                   "B4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 1), (taille_case, taille_case)), "B5": pygame.Rect((positionx + 135 * 4, positiony + 135 - 1), (taille_case, taille_case)), "B6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 1), (taille_case, taille_case)), 
                   "B7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 1), (taille_case, taille_case)), "B8": pygame.Rect((positionx + 135 * 7, positiony + 135 - 1), (taille_case, taille_case)), 

                   "C1": pygame.Rect((positionx, positiony - 135 * 2), (taille_case, taille_case)), "C2": pygame.Rect((positionx + 135 * 1 , positiony - 135 * 2 ), (taille_case, taille_case)), "C3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 2), (taille_case, taille_case)), 
                   "C4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 2), (taille_case, taille_case)), "C5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 2), (taille_case, taille_case)), "C6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 2), (taille_case, taille_case)), 
                   "C7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 2), (taille_case, taille_case)), "C8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 2), (taille_case, taille_case)), 

                   "D1": pygame.Rect((positionx, positiony - 135 * 3), (taille_case, taille_case)), "D2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 3), (taille_case, taille_case)), "D3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 3), (taille_case, taille_case)), 
                   "D4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 3), (taille_case, taille_case)), "D5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 3), (taille_case, taille_case)), "D6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 3), (taille_case, taille_case)), 
                   "D7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 3), (taille_case, taille_case)), "D8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 3), (taille_case, taille_case)), 

                   "E1": pygame.Rect((positionx, positiony - 135 * 4), (taille_case, taille_case)), "E2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 4), (taille_case, taille_case)), "E3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 4), (taille_case, taille_case)), 
                   "E4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 4), (taille_case, taille_case)), "E5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 4), (taille_case, taille_case)), "E6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 4), (taille_case, taille_case)), 
                   "E7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 4), (taille_case, taille_case)), "E8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 4), (taille_case, taille_case)), 

                   "F1": pygame.Rect((positionx, positiony - 135 * 5), (taille_case, taille_case)), "F2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 5), (taille_case, taille_case)), "F3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 5), (taille_case, taille_case)), 
                   "F4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 5), (taille_case, taille_case)), "F5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 5), (taille_case, taille_case)), "F6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 5), (taille_case, taille_case)), 
                   "F7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 5), (taille_case, taille_case)), "F8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 5), (taille_case, taille_case)), 

                   "G1": pygame.Rect((positionx, positiony - 135 * 6), (taille_case, taille_case)), "G2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 6), (taille_case, taille_case)), "G3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 6), (taille_case, taille_case)), 
                   "G4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 6), (taille_case, taille_case)), "G5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 6), (taille_case, taille_case)), "G6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 6), (taille_case, taille_case)), 
                   "G7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 6), (taille_case, taille_case)), "G8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 6), (taille_case, taille_case)), 

                   "H1": pygame.Rect((positionx, positiony - 135 * 7), (taille_case, taille_case)), "H2": pygame.Rect((positionx + 135 * 1, positiony - 135 * 7), (taille_case, taille_case)), "H3": pygame.Rect((positionx + 135 * 2, positiony - 135 * 7), (taille_case, taille_case)), 
                   "H4": pygame.Rect((positionx + 135 * 3, positiony - 135 * 7), (taille_case, taille_case)), "H5": pygame.Rect((positionx + 135 * 4, positiony - 135 * 7), (taille_case, taille_case)), "H6": pygame.Rect((positionx + 135 * 5, positiony - 135 * 7), (taille_case, taille_case)), 
                   "H7": pygame.Rect((positionx + 135 * 6, positiony - 135 * 7), (taille_case, taille_case)), "H8": pygame.Rect((positionx + 135 * 7, positiony - 135 * 7), (taille_case, taille_case)),}

vide = ["",""]

Echequier = [[["tour","blanc"],["cavalier","blanc"],["fou","blanc"],["reine","blanc"],["roi","blanc"],["fou","blanc"],["cavalier","blanc"],["tour","blanc"]],
             [["pion","blanc"],["pion","blanc"],["pion","blanc"],["pion","blanc"],["pion","blanc"],["pion","blanc"],["pion","blanc"],["pion","blanc"]],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [["pion","noir"],["pion","noir"],["pion","noir"],["pion","noir"],["pion","noir"],["pion","noir"],["pion","noir"],["pion","noir"]],
             [["tour","noir"],["cavalier","noir"],["fou","noir"],["reine","noir"],["roi","noir"],["fou","noir"],["cavalier","noir"],["tour","noir"]]]

#On doit trouver un moyen de relier mon dictionnaire à la liste des pions
Echiquierfinal = {}

def case(s):
    global Echequier
#????
    return Echequier[int(s[1])-1][ord(s[0])-65]

def case_c_l(colonne,ligne):
    global Echequier
    return Echequier[ligne][colonne]

def mouvement(de_la,vers_la):
    global Echequier
    #Explique un peu ça
    co1 = (int(de_la[1]),ord(de_la[0])-65)
    co2 = (int(vers_la[1]),ord(vers_la[0])-65)
    Echequier[co2[0]][co2[1]] = Echequier[co1[0]][co1[1]]
    Echequier[co1[0]][co1[1]] = vide

def deplas(s):
    r = []
    (typ,couleur) = case(s)
    colonne = ord(s[0])-65
    ligne = int(s[1])-1
    if typ == "":
        return r
    else :
        if typ == "pion":
            if couleur == "blanc":
                if case_c_l(colonne,ligne+1) == vide:
                    r.append(chr(colonne+65)+str(ligne+2))
                if colonne-1 >= 0 and ligne+1 < 8 and case_c_l(colonne-1,ligne+1)[1] == "noir":
                    r.append(chr(colonne-1+65)+str(ligne+1+1))
                if colonne+1 < 8 and ligne+1 < 8 and case_c_l(colonne+1,ligne+1)[1] == "noir":
                    r.append(chr(colonne+1+65)+str(ligne+1+1))
                if ligne == 1 and case_c_l(colonne,ligne+2) == vide:
                    r.append(chr(colonne+65)+str(ligne+2+1))
            else:
                if case_c_l(colonne,ligne-1) == vide:
                    r.append(chr(colonne+65)+str(ligne))
                if colonne-1 >= 0 and ligne-1 >=0 and case_c_l(colonne-1,ligne-1)[1] == "blanc":
                    r.append(chr(colonne-1+65)+str(ligne+1-1))
                if colonne+1 < 8 and ligne-1 >=0 and case_c_l(colonne+1,ligne-1)[1] == "blanc":
                    r.append(chr(colonne+1+65)+str(ligne+1-1))
                if ligne == 7 and case_c_l(colonne,ligne-2) == vide:
                    r.append(chr(colonne+65)+str(ligne-2+1))
        elif typ == "tour":
            continuer = True
            i = 1
            while continuer :
                if colonne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne)[1] != couleur and case_c_l(colonne+i,ligne)[1] != "":
                            continuer = False
                        r.append(chr(colonne+i+65)+str(ligne+1))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if colonne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne)[1] != couleur and case_c_l(colonne-i,ligne)[1] != "":
                            continuer = False
                        r.append(chr(colonne-i+65)+str(ligne+1))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne-i)[1] != couleur and case_c_l(colonne,ligne-i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65)+str(ligne+1-i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne+i)[1] != couleur and case_c_l(colonne,ligne+i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65)+str(ligne+1+i))
                        i = i + 1
        elif typ == "cavalier":
            if colonne+2 < 8 and ligne+1 < 8 and case_c_l(colonne+2,ligne+1)[1] != couleur:
                r.append(chr(colonne+2+65)+str(ligne+1+1))
            if colonne+1 < 8 and ligne+2 < 8 and case_c_l(colonne+1,ligne+2)[1] != couleur:
                r.append(chr(colonne+1+65)+str(ligne+1+2))
            if colonne-2 >= 0 and ligne+1 < 8 and case_c_l(colonne-2,ligne+1)[1] != couleur:
                r.append(chr(colonne-2+65)+str(ligne+1+1))
            if colonne-1 >= 0 and ligne+2 < 8 and case_c_l(colonne-1,ligne+2)[1] != couleur:
                r.append(chr(colonne-1+65)+str(ligne+1+2))
            if colonne+2 < 8 and ligne-1 >= 0 and case_c_l(colonne+2,ligne-1)[1] != couleur:
                r.append(chr(colonne+2+65)+str(ligne+1-1))
            if colonne+1 < 8 and ligne-2 >= 0 and case_c_l(colonne+1,ligne-2)[1] != couleur:
                r.append(chr(colonne+1+65)+str(ligne+1-2))
            if colonne-1 >= 0 and ligne-2 >= 0 and case_c_l(colonne-1,ligne-2)[1] != couleur:
                r.append(chr(colonne-1+65)+str(ligne+1-2))
            if colonne-2 >= 0 and ligne-1 >= 0 and case_c_l(colonne-2,ligne-1)[1] != couleur:
                r.append(chr(colonne-2+65)+str(ligne+1-1))
        elif typ ==  "fou":
            continuer = True
            i = 1
            while continuer :
                if colonne + i >= 8 or ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne+i)[1] != couleur and case_c_l(colonne+i,ligne+i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+i+65)+str(ligne+1+i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if colonne - i < 0 or ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne+i)[1] != couleur and case_c_l(colonne-i,ligne+i)[1] != "":
                            continuer = False
                        r.append(chr(colonne-i+65)+str(ligne+1+i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0 or colonne + i >=8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne-i)[1] != couleur and case_c_l(colonne+i,ligne-i)[1] != "":
                            ontinuer = False
                        r.append(chr(colonne+65+i)+str(ligne+1-i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0 or colonne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne-i)[1] != couleur and case_c_l(colonne-i,ligne-i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65-i)+str(ligne+1-i))
                        i = i + 1
        elif typ == "reine":
            continuer = True
            i = 1
            while continuer :
                if colonne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne)[1] != couleur and case_c_l(colonne+i,ligne)[1] != "":
                            continuer = False
                        r.append(chr(colonne+i+65)+str(ligne+1))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if colonne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne)[1] != couleur and case_c_l(colonne-i,ligne)[1] != "":
                            continuer = False
                        r.append(chr(colonne-i+65)+str(ligne+1))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne-i)[1] != couleur and case_c_l(colonne,ligne-i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65)+str(ligne+1-i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne+i)[1] != couleur and case_c_l(colonne,ligne+i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65)+str(ligne+1+i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if colonne + i >= 8 or ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne+i)[1] != couleur and case_c_l(colonne+i,ligne+i)[1] !="":
                            continuer = False
                        r.append(chr(colonne+i+65)+str(ligne+1+i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if colonne - i < 0 or ligne + i >= 8:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne+i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne+i)[1] != couleur and case_c_l(colonne-i,ligne+i)[1] != "":
                            continuer = False
                        r.append(chr(colonne-i+65)+str(ligne+1+i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0 or colonne + i >=8:
                    continuer = False
                else:
                    if case_c_l(colonne+i,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne-i)[1] != couleur and case_c_l(colonne+i,ligne-i)[1] != "":
                            ontinuer = False
                        r.append(chr(colonne+65+i)+str(ligne+1-i))
                        i = i + 1
            continuer = True
            i = 1
            while continuer :
                if ligne - i < 0 or colonne - i < 0:
                    continuer = False
                else:
                    if case_c_l(colonne-i,ligne-i)[1] == couleur:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne-i)[1] != couleur and case_c_l(colonne-i,ligne-i)[1] != "":
                            continuer = False
                        r.append(chr(colonne+65-i)+str(ligne+1-i))
                        i = i + 1
        elif typ == "roi":
            if colonne+1 < 8 and ligne+1 < 8 and case_c_l(colonne+1,ligne+1)[1] != couleur:
                r.append(chr(colonne+1+65)+str(ligne+1+1))
            if colonne < 8 and ligne+1 < 8 and case_c_l(colonne,ligne+1)[1] != couleur:
                r.append(chr(colonne+65)+str(ligne+1+1))
            if colonne+1 < 8 and ligne < 8 and case_c_l(colonne+1,ligne)[1] != couleur:
                r.append(chr(colonne+1+65)+str(ligne+1))
            if colonne-1 >= 0 and ligne-1 >= 0 and case_c_l(colonne-1,ligne-1)[1] != couleur:
                r.append(chr(colonne-1+65)+str(ligne+1-1))
            if colonne < 8 and ligne-1 >= 0 and case_c_l(colonne,ligne-1)[1] != couleur:
                r.append(chr(colonne+65)+str(ligne+1-1))
            if colonne-1 >= 0 and ligne >= 0 and case_c_l(colonne-1,ligne)[1] != couleur:
                r.append(chr(colonne-1+65)+str(ligne+1))
            if colonne-1 >= 0 and ligne+1 < 8 and case_c_l(colonne-1,ligne+1)[1] != couleur:
                r.append(chr(colonne-1+65)+str(ligne+1+1))
            if colonne+1 <8 and ligne-1 >= 0 and case_c_l(colonne+1,ligne-1)[1] != couleur:
                r.append(chr(colonne+1+65)+str(ligne+1-1))
        return r

def echec(couleur):
    global Echequier
    for i in range(8):
        for j in range(8):
            if case(chr(i+65)+str(j)) == ("roi",couleur):
                c = chr(i+65)+str(j)
    for i in range(8):
        for j in range(8):
            a = chr(i+65)+str(j)
            if case(a)[1] != couleur and case(a)[1] != "":
                for i in range(len(deplas(a))):
                    if deplas(a)[i] == c :
                        return True
    return False

def echec_et_mat(couleur):
    global Echequier
    for i in range(8):
        for j in range(8):
            if case(chr(i+65)+str(j)) == ("roi",couleur):
                c = chr(i+65)+str(j)
    for i in range(len(deplas(c))):
        if depla_possible(c,deplas(c)[i]):
            return True
    a = 0
    b = ""
    for i in range(8):
        for j in range(8):
            for k in range(len(deplas(chr(i+65)+str(j)))):
                if c == deplas(chr(i+65)+str(j))[k]:
                    a = a + 1
                    b = chr(i+65)+str(j)
                    if a >= 2:
                        return True
    if a == 1:
        for i in range(8):
            for j in range(8):
                for k in range(len(deplas(chr(i+65)+str(j)))):
                    if case(chr(i+65)+str(j))[1] != case(b)[1] and deplas(chr(i+65)+str(j))[k] == b and depla_possible(deplas(chr(i+65)+str(j))[k],b):
                        return False
        return True
                    
  #faudra voir si 1: il y a au moins 2 pièces adverses qui le menace 2: en se déplaçant ça change rien donc il faudra utiliser depla_possible

def depla_possible(case_dep,case_ari):
    global Echequier
    pion1 = case(case_dep)
    pion2 = case(case_ari)
    oui = False
    for i in range(len(deplas(case_dep))):
        if case_ari == deplas(case_dep)[i]:
            oui = True
    if oui:
        mouvement(case_dep,case_ari)
        if echec(pion1[1]):
            Echequier[int(case_dep[1])-1][ord(case_dep[0])-65] = pion1
            Echequier[int(case_ari[1])-1][ord(case_ari[0])-65] = pion2
            return False
        else:
            Echequier[int(case_dep[1])-1][ord(case_dep[0])-65] = pion1
            Echequier[int(case_ari[1])-1][ord(case_ari[0])-65] = pion2
            return True
    else:
        return False


## Pygame

pygame.init()

# Load the image
menu = pygame.image.load("menu_img.jpg")

# Set the display mode
screen = pygame.display.set_mode(menu.get_size())

# Set the title of the window
pygame.display.set_caption("Menu")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.SysFont(None, 40)

# Define button dimensions and positions
image_rect = menu.get_rect()
text_rect = pygame.Rect((0, 0), (200, 50))
text_rect.center = image_rect.center

# Define text
start_text = font.render("Start Game", True, WHITE)
quit_text = font.render("Quit", True, WHITE)

# Blit the image and buttons on the screen
screen.blit(menu, (0, 0))
screen.blit(start_text, (text_rect.centerx - start_text.get_width() / 2, text_rect.centery - start_text.get_height()))
text_rect.move_ip(0, 70)  # Adjusted vertical position
screen.blit(quit_text, (text_rect.centerx - quit_text.get_width() / 2, text_rect.centery - quit_text.get_height()))
# explain

# define buttons positions
start_button = pygame.Rect((text_rect.centerx - start_text.get_width() / 2, text_rect.centery - start_text.get_height()),start_text.get_size)
quit_button = pygame.Rect(text_rect.centerx - quit_text.get_width() / 2, text_rect.centery - quit_text.get_height())

# Update the display
pygame.display.update()

 # Wait for the user to close the window or click on a button
 # Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.collidepoint(event.pos):
                # L'utilisateur a cliqué sur le bouton de quitter
                pygame.quit()
                sys.exit()
            if start_button.collidepoint(event.pos):
                # L'utilisateur a cliqué sur le bouton de démarrage
                print("starting game")
                #main_loop()
                ### LE IF DE START GAME NE FONCTIONNE PAS -- Je n'arrive pas à le faire marcher
                
                
def main_loop():
    print("starting game")
    