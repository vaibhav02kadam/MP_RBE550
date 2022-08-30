import os, sys
import pygame
from env_utils import*

#Initilising pygame module
pygame.init()

class Grid:

    def __init__(self):
        print("Intiliasing Environment with Grid ")

    def drawGrid(self):

        for x in range(0, screen_width, block_size):
            for y in range(0, screen_height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, COLOR_WHITE, rect, 1)

'''
    def drawObstacle(self):


    def getObstacles(self):
'''


if __name__ == '__main__':

    grid = Grid()
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Obstacles field - Vaibhav Kadam")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid.drawGrid()
        pygame.display.flip()


    pygame.quit()


