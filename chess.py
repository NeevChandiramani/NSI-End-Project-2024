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

Echequier = {"A1":["tour","blanc"],     "A2":["pion","blanc"],  "A3":vide,  "A4":vide,  "A5":vide,  "A6":vide,  "A7":["pion","noir"],   "A8":["tour","noir"],
             "B1":["cavalier","blanc"], "B2":["pion","blanc"],  "B3":vide,  "B4":vide,  "B5":vide,  "B6":vide,  "B7":["pion","noir"],   "B8":["cavalier","noir"],
             "C1":["fou","blanc"],      "C2":["pion","blanc"],  "C3":vide,  "C4":vide,  "C5":vide,  "C6":vide,  "C7":["pion","noir"],   "C8":["fou","noir"],
             "D1":["reine","blanc"],    "D2":["pion","blanc"],  "D3":vide,  "D4":vide,  "D5":vide,  "D6":vide,  "D7":["pion","noir"],   "D8":["reine","noir"],
             "E1":["roi","blanc"],      "E2":["pion","blanc"],  "E3":vide,  "E4":vide,  "E5":vide,  "E6":vide,  "E7":["pion","noir"],   "E8":["roi","noir"],
             "F1":["fou","blanc"],      "F2":["pion","blanc"],  "F3":vide,  "F4":vide,  "F5":vide,  "F6":vide,  "F7":["pion","noir"],   "F8":["fou","noir"],
             "G1":["cavalier","blanc"], "G2":["pion","blanc"],  "G3":vide,  "G4":vide,  "G5":vide,  "G6":vide,  "G7":["pion","noir"],   "G8":["cavalier","noir"],
             "H1":["tour","blanc"],     "H2":["pion","blanc"],  "H3":vide,  "H4":vide,  "H5":vide,  "H6":vide,  "H7":["pion","noir"],   "H8":["tour","noir"]}



def colonne_num(case):
    return ord(case[0])-65
def colonne_chif(num):
    return chr(65+num)

def case_c_l(colonne,ligne):
    global Echequier
    return Echequier[colonne_chif(colonne)+str(ligne+1)]


def mouvement(de_la,vers_la):
    global Echequier
    Echequier[vers_la] = Echequier[de_la]
    Echequier[de_la] = vide

def deplas(s):
    r = []
    colonne = ord(s[0])-65
    ligne = int(s[1])-1
    (typ,couleur) = case_c_l(colonne,ligne)
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
                            continuer = False
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
    for i in Echequier.keys():
        if Echequier[i] == ("roi",couleur):
            case_roi = i
    for i in Echequier.keys():
        if Echequier[i][1] != couleur and Echequier[i][1] != "":
            for i in range(len(deplas(i))):
                if deplas(i)[i] == case_roi :
                    return True
    return False

def echec_et_mat(couleur):
    global Echequier
    for i in Echequier.keys():
        if Echequier[i] == ("roi",couleur):
            case_roi = i
    for i in range(len(deplas(case_roi))):
        if depla_possible(case_roi,deplas(case_roi)[i]):
            return False
    a = 0
    b = ""
    for i in Echequier.keys():
        for k in range(len(deplas(i))):
            if case_roi == deplas(i)[k]:
                a = a + 1
                b = i
                if a >= 2:
                    return True
    if a == 1:
        for i in Echequier.keys():
            for k in range(len(deplas(i))):
                if Echequier[i][1] != Echequier[b][1] and deplas(i)[k] == b and depla_possible(deplas(i)[k],b):
                    return False
        return True
                    
  #faudra voir si 1: il y a au moins 2 pièces adverses qui le menace 2: en se déplaçant ça change rien donc il faudra utiliser depla_possible

def depla_possible(case_dep,case_ari):
    global Echequier
    pion1 = Echequier[case_dep]
    pion2 = Echequier[case_ari]
    oui = False
    for i in range(len(deplas(case_dep))):
        if case_ari == deplas(case_dep)[i]:
            oui = True
    if oui:
        mouvement(case_dep,case_ari)
        if echec(pion1[1]):
            Echequier[case_dep] = pion1
            Echequier[case_ari] = pion2
            return False
        else:
            Echequier[case_dep] = pion1
            Echequier[case_ari] = pion2
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
start_button = pygame.Rect((text_rect.centerx - start_text.get_width() / 2, text_rect.centery - start_text.get_height()),((start_text.get_width()),(start_text.get_height())))
quit_button = pygame.Rect((text_rect.centerx - quit_text.get_width() / 2, text_rect.centery - quit_text.get_height()),(quit_text.get_width(),quit_text.get_height()))
#explain --> Pour un argument rect, faut 4 variables, les 2 premières sont les coordonnées du coin supérieur gauche et les 2 suivantes sont la largeur et la hauteur du rectangle séparés par les virgules
#Rect(left, top, width, height)


# Update the display
pygame.display.update()

# Function for the main loop
#def main_loop():
#    print("starting game")


 # Wait for the user to close the window or click on a button
 # loop for the menu
# Wait for the user to close the window or click on a button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print("starting game")
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
                #main_loop()
                ### LE IF DE START GAME NE FONCTIONNE PAS -- Je n'arrive pas à le faire marcher -- Essaie de le faire rouler