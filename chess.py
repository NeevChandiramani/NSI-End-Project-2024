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
def grid():
    """Create a dictionary representing an 8x8 chessboard grid.

    The keys of the dictionary are the ASCII codes for the letters 'A' to 'H',
    and the values are lists representing the rows of the grid, with each
    element of the list representing a square.

    Returns:
        A dictionary with keys ranging from 65 to 72, inclusive, and values
        that are lists of length 8.
    """
    H8 = {}
    for i in range(8):
        H8[ord('A')+i] = [""]*8  # Create a new list of length 8
    return H8
#print(grid())
