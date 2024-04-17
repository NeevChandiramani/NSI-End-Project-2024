import pygame
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


Echequier = [[t_b_1,c_b_1,f_b_1,q_b,k_b,f_b_2,c_b_2,t_b_2],
             [p_b_1,p_b_2,p_b_3,p_b_4,p_b_5,p_b_6,p_b_7,p_b_8],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [vide,vide,vide,vide,vide,vide,vide,vide],
             [p_n_1,p_n_2,p_n_3,p_n_4,p_n_5,p_n_6,p_n_7,p_n_8],
             [t_n_1,c_n_1,f_n_1,q_n,k_n,f_n_2,c_n_2,t_n_2]]

def case(s):
    global Echequier
    return Echequier[int(s[1])-1][ord(s[0])-65]

def case_c_l(colonne,ligne):
    global Echequier
    return Echequier[ligne][colonne]

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
                
            else:
                if case_c_l(colonne,ligne-1) == vide:
                    r.append(chr(colonne+65)+str(ligne))

        elif typ == "tour":
            if couleur == "blanc":
                continuer = True
                i = 1
                while continuer :
                    if colonne + i >= 8:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne)[1] == "blanc":
                            continuer = False
                        else:
                            if case_c_l(colonne+i,ligne)[1] == "noir":
                                continuer = False
                            r.append(chr(colonne+i+65)+str(ligne+1))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if colonne - i < 0:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne)[1] == "blanc":
                            continuer = False
                        else:
                            if case_c_l(colonne-i,ligne)[1] == "noir":
                                continuer = False
                            r.append(chr(colonne-i+65)+str(ligne+1))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if ligne - i < 0:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne-i)[1] == "blanc":
                            continuer = False
                        else:
                            if case_c_l(colonne,ligne-i)[1] == "noir":
                                continuer = False
                            r.append(chr(colonne+65)+str(ligne+1-i))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if ligne + i >= 8:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne+i)[1] == "blanc":
                            continuer = False
                        else:
                            if case_c_l(colonne,ligne+i)[1] == "noir":
                                continuer = False
                            r.append(chr(colonne+65)+str(ligne+1+i))
                            i = i + 1
            else:
                continuer = True
                i = 1
                while continuer :
                    if colonne + i >= 8:
                        continuer = False
                    else:
                        if case_c_l(colonne+i,ligne)[1] == "noir":
                            continuer = False
                        else:
                            if case_c_l(colonne+i,ligne)[1] == "blanc":
                                continuer = False
                            r.append(chr(colonne+i+65)+str(ligne+1))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if colonne - i < 0:
                        continuer = False
                    else:
                        if case_c_l(colonne-i,ligne)[1] == "noir":
                            continuer = False
                        else:
                            if case_c_l(colonne-i,ligne)[1] == "blanc":
                                continuer = False
                            r.append(chr(colonne-i+65)+str(ligne+1))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if ligne - i < 0:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne-i)[1] == "noir":
                            continuer = False
                        else:
                            if case_c_l(colonne,ligne-i)[1] == "blanc":
                                continuer = False
                            r.append(chr(colonne+65)+str(ligne+1-i))
                            i = i + 1
                continuer = True
                i = 1
                while continuer :
                    if ligne + i >= 8:
                        continuer = False
                    else:
                        if case_c_l(colonne,ligne+i)[1] == "noir":
                            continuer = False
                        else:
                            if case_c_l(colonne,ligne+i)[1] == "blanc":
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
            print()
        elif typ == "reine":
            print()
        elif typ == "roi":
            print()
        return r
            



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