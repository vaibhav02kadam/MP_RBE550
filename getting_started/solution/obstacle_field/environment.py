import os, sys
import pygame
from env_utils import*

#Initilising pygame module
pygame.init()

class Grid:

    def __init__(self, grid_width, grid_height, block_size, tetro):

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.block_size = block_size
        self.tetro = []
        self.grid_env = []

        self.screen_width = self.grid_width*self.block_size
        self.screen_height = self.grid_height*self.block_size

        print("Intiliasing Environment with Grid ")

    def drawGrid(self):

        for row in range(0, len(self.grid_env[0])):
            for col in range(0, len(self.grid_env)):
                x_cords = col*block_size
                y_cords = row*block_size
                rect = pygame.Rect(x_cords, y_cords, block_size, block_size)

                if self.isBlockOccupied(row, col):
                    color = COLOR_BLACK
                else:
                    color = COLOR_WHITE
                pygame.draw.rect(screen, color, rect, 0)

                

  

    def getGridEnv(self):
        
        #Create free space grid environment
        for _ in range(0, self.grid_height):
            row = []
            for _ in range(0, self.grid_width):
                row.append(0)
            self.grid_env.append(row)

        
    def isBlockOccupied(self, x, y) -> bool:
        if self.grid_env[x][y] == 1 :   
            return self.grid_env[x][y]
        else:
            return 0


'''
    def drawObstacle(self):


    def getObstacles(self):
'''




if __name__ == '__main__':

    grid = Grid(grid_width, grid_height, block_size, tetro)
    screen = pygame.display.set_mode(( grid.screen_width, grid.screen_height))
    screen.fill(COLOR_BLACK)
    pygame.display.set_caption("Obstacles field - Vaibhav Kadam")
    grid.getGridEnv()
    grid.grid_env[1][1] = 1
    print(grid.grid_env)




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        grid.drawGrid()

        pygame.display.flip()
    
    pygame.quit()


