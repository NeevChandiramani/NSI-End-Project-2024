import pygame
# import random --> IA with different difficulties

# Print the chessboard.png file with pygame

screen = pygame.display.set_mode((640,640))
chessboard = pygame.image.load("chessboard.png")
screen.blit(chessboard,(0,0))
pygame.display.flip() 



pion1 = ('blanc','cavalier')

prop = {'cavalier' : ('',''), 'pion' : ('','')}

#grid of 8x8 
#def grid():
#    H8 = {}
#    for i in range(8):
#        H8[ord(65)+i] = ["","","","","","","",""]
#    return(H8)
#print(grid())

