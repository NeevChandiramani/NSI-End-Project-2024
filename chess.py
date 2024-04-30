import pygame
import webbrowser
import time

webbrowser.open('http://chess.neevchandiramani.com')
time.sleep(10)

#Les deux lignes suivantes sont issues d'un forum : https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame et elles permettent
#de trouver la résolution de l'écran ainsi que de créer un objet écran de la résolution de celui-ci
#infoObject = pygame.display.Info()
#screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#taille_case = infoObject.current_h * 8
# ligne 8 à 10 font tout buger, t'as fait quoi ayoub?!

#import random

p_b_1 = ("pion","blanc")
p_b_2 = ("pion","blanc")
p_b_3 = ("pion","blanc")
p_b_4 = ("pion","blanc")
p_b_5 = ("pion","blanc")
p_b_6 = ("pion","blanc")
p_b_7 = ("pion","blanc")
p_b_8 = ("pion","blanc")

t_b_1 = ("tour","blanc")
t_b_2 = ("tour","blanc")

c_b_1 = ("cavalier","blanc")
c_b_2 = ("cavalier","blanc")

f_b_1 = ("fou","blanc")
f_b_2 = ("fou","blanc")

k_b = ("roi","blanc")
q_b = ("reine","blanc")



p_n_1 = ("pion","noir")
p_n_2 = ("pion","noir")
p_n_3 = ("pion","noir")
p_n_4 = ("pion","noir")
p_n_5 = ("pion","noir")
p_n_6 = ("pion","noir")
p_n_7 = ("pion","noir")
p_n_8 = ("pion","noir")

t_n_1 = ("tour","noir")
t_n_2 = ("tour","noir")

c_n_1 = ("cavalier","noir")
c_n_2 = ("cavalier","noir")

f_n_1 = ("fou","noir")
f_n_2 = ("fou","noir")

k_n = ("roi","noir")
q_n = ("reine","noir")


vide = ("","")

#j'ai besoin d'aide pour les positions --> bah ça marche pas donc j'ai tout commenté
#Cases_echiquier = {"A1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "A4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "A7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "A8": pygame.Rect((positionx, positiony), (taille_case, taille_case)),
#
#                   "B1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "B2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "B3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "B4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "B5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "B6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "B7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "B8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#
#                   "C1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "C2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "C3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "C4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "C5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "C6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "C7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "C8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#
#                   "D1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "D2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "D3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "D4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "D5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "D6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "D7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "D8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#
#                   "E1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "E2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "E3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "E4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "E5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "E6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "E7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "E8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#
#                   "F1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "F2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "F3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "F4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "F5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "F6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "F7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "F8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#
#                   "G1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "G2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "G3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "G4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "G5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "G6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
#                   "G7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "G8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 

 #                  "H1": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "H2": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "H3": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
 #                  "H4": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "H5": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "H6": pygame.Rect((positionx, positiony), (taille_case, taille_case)), 
 #                  "H7": pygame.Rect((positionx, positiony), (taille_case, taille_case)), "H8": pygame.Rect((positionx, positiony), (taille_case, taille_case)), }


Echequier = [[t_b_1,c_b_1,f_b_1,q_b,k_b,f_b_2,c_b_2,t_b_2],
             [p_b_1,p_b_2,p_b_3,p_b_4,p_b_5,p_b_6,p_b_7,p_b_8],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [p_n_1,p_n_2,p_n_3,p_n_4,p_n_5,p_n_6,p_n_7,p_n_8],
             [t_n_1,c_n_1,f_n_1,q_n,k_n,f_n_2,c_n_2,t_n_2]]

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
            else:
                if case_c_l(colonne,ligne-1) == vide:
                    r.append(chr(colonne+65)+str(ligne))
                if colonne-1 >= 0 and ligne-1 >=0 and case_c_l(colonne-1,ligne-1)[1] == "blanc":
                    r.append(chr(colonne-1+65)+str(ligne+1-1))
                if colonne+1 < 8 and ligne-1 >=0 and case_c_l(colonne+1,ligne-1)[1] == "blanc":
                    r.append(chr(colonne+1+65)+str(ligne+1-1))
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
chessboard = pygame.image.load("chessboard.png")

# Set the display mode
screen = pygame.display.set_mode(chessboard.get_size())

# Il faudrait enlever la partie avec le noir en dessous de l'image (j'ai pas réussi à le faire)

# Set the title of the window 
pygame.display.set_caption("Chess")

# Blit the image on the screen
screen.blit(chessboard, (0, 0))

# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # User input
        if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()