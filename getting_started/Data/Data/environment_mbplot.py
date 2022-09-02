import os, sys
from matplotlib.figure import Figure
import random as rnd
import math
from env_utils import*

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image, ImageDraw


#Initilising pygame module
# pygame.init()

class Grid:

    def __init__(self, grid_width, grid_height, block_size, tetro):

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.block_size = block_size
        self.tetro = tetro
        self.grid_env = []

        self.screen_width = self.grid_width*self.block_size
        self.screen_height = self.grid_height*self.block_size

        self.obstacle_occupancy = obstacle_occupancy_percent/100

        print("Intiliasing Environment with Grid ")

    def drawGrid(self):

        for row in range(0, len(self.grid_env[0])):
            for col in range(0, len(self.grid_env)):
                x_cords = col*block_size
                y_cords = row*block_size

                sq = patches.Rectangle((x_cords, y_cords), self.block_size,  self.block_size, fill=True, facecolor="b")
                ax.add_patch(sq)


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

    
    def getObstacles(self):
        obstacle_grids = round((self.grid_width * self.grid_height)*self.obstacle_occupancy)
        
        random_tetro_shape = rnd.choice(self.tetro)
        rand_x_cord = rnd.randint(0, len(self.grid_env[0]))
        rand_y_cord = rnd.randint(0, len(self.grid_env))
        print("rand shape and coords",random_tetro_shape, (rand_x_cord, rand_y_cord))

        random_rotation = rnd.choice([90, 180, 270,360])
        print("random rotation", random_rotation)


        for x_ in range(0, len(self.grid_env[0])):
            for y_ in range(0, len(self.grid_env)):
                if x_ == rand_x_cord and y_ == rand_y_cord:
                    self.grid_env[x_][y_] = 1
    
     


if __name__ == '__main__':

    grid = Grid(grid_width, grid_height, block_size, tetro)

    grid.getGridEnv()
    grid.grid_env[1][1] = 1
    grid.getObstacles()

    image = Image.new(mode="RGBA", size=(grid.screen_width, grid.screen_height), color="white")

    print("Grid", grid.grid_env)

    # fig, ax = plt.subplots(1)
    # ax.imshow(image)

    # grid.drawGrid()


    plt.axis('off')
    plt.savefig('test_env.png', dpi=100 )
    plt.show()