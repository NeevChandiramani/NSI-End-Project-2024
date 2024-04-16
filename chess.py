import pygame
#import random
#IA with different difficulties

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

cases_existantes = []

def case(s):
    global Echequier
    return Echequier[ord(s[0])-65][int(s[1])-1]


print(case("A2"))

def deplas(s):
    r = [""]
    colonne = s[0]
    ligne = s[1]
    a = case(s)
    ( tipe , couleur ) = a
    if tipe == "" :
        return []











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