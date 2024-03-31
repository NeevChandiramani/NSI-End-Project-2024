# import pygame
# import random --> IA with different difficulties

G = {"A" : ["" for i in range(8)],
"B" : ["" for i in range(8)],
"C" : ["" for i in range(8)],
"D" : ["" for i in range(8)],
"E" : ["" for i in range(8)],
"F" : ["" for i in range(8)],
"G" : ["" for i in range(8)],
"H" : ["" for i in range(8)],}

pion1 = ('blanc','cavalier')

prop = {'cavalier' : ('',''), 'pion' : ('','')}

#grid of 8x8 
def grid():
    H8 = []
    for i in range(8):
        H8.append([0,0,0,0,0,0,0,0])
    return(H8)
print(grid())