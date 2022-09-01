import pygame
import env_utils as env
import  random

pygame.init()
screen = pygame.display.set_mode((env.arena_width, env.arena_height))
pygame.display.set_caption("Obstacles field - Vaibhav Kadam")

# Run until the user asks to quit
running = True
while running:


    blockSize = 10 #Set the size of the grid block
    for x in range(0, env.arena_width, blockSize):
        for y in range(0, env.arena_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, env.clr_white, rect, 1)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    pygame.draw.rect(screen, env.clr_white, pygame.Rect(0, 0, 10, 10), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()