# import pygame
# import random --> IA with different difficulties

pion1 = ('blanc','cavalier')

prop = {'cavalier' : ('',''), 'pion' : ('','')}

#grid of 8x8 
def grid():
    H8 = {}
    for i in range(8):
        H8.append([0,0,0,0,0,0,0,0])
    return(H8)
print(grid())