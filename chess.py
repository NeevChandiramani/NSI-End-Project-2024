import pygame
# import random --> IA with different difficulties
pygame.init()

# Load the image
chessboard = pygame.image.load("chessboard.png")

# Set the display mode
screen = pygame.display.set_mode(chessboard.get_size())

# Update the display
screen.blit(chessboard, (0, 0))
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
pygame.init()


pion1 = ('blanc','cavalier')

prop = {'cavalier' : ('',''), 'pion' : ('','')}

#grid of 8x8 
#def grid():
#    H8 = {}
#    for i in range(8):
#        H8[ord(65)+i] = ["","","","","","","",""]
#    return(H8)
#print(grid())

