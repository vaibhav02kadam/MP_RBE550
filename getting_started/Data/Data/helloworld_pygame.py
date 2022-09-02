import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Obstacles field - Vaibhav Kadam")

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initializing Color
    color = (48, 141, 70)

    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()