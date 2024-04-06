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

            # Create a dictionary for each box in the chessboard with the png file
            chessboard_boxes = {
                "a1": pygame.image.load("a1.png"),
                "a2": pygame.image.load("a2.png"),
                "a3": pygame.image.load("a3.png"),
                # ... continue for all boxes
            }

            # Replace the placeholder code with the following loop to display the chessboard boxes
            for box, image in chessboard_boxes.items():
                screen.blit(image, (0, 0))  # Replace (0, 0) with the appropriate coordinates for each box
            pygame.display.flip()