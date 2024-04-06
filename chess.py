import pygame
# import random
#IA with different difficulties

pygame.init()

# Load the image
chessboard = pygame.image.load("chessboard.png")

# Set the display mode
screen = pygame.display.set_mode(chessboard.get_size())

# Set the title of the window 
pygame.display.set_caption("Chess")

# Blit the image on the screen
screen.blit(chessboard, (0, 0))

# Update the display
pygame.display.flip()

 

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