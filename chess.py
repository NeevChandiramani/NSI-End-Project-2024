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
            # User input
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()