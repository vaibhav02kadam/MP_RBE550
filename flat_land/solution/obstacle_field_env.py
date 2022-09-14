import os, sys
import pygame
import random as rnd
import math
from env_utils import*

class Grid:

    def __init__(self, screen, grid_width, grid_height, block_size, tetro):
        self.screen = screen
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.block_size = block_size
        self.tetro = tetro
        self.grid_env = []

        self.screen_width = self.grid_width*self.block_size
        self.screen_height = self.grid_height*self.block_size

        self.obstacle_occupancy = obstacle_occupancy_percent/100
        self.obstacles_required = round(self.obstacle_occupancy*(self.grid_width*self.grid_height))


        self.getGridEnv()
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
                pygame.draw.rect(self.screen, color, rect, 0)


    def getGridEnv(self):
        
        #Create free space grid environment
        for _ in range(0, self.grid_height):
            row = []
            for _ in range(0, self.grid_width):
                row.append(0)
            self.grid_env.append(row)

        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)

        return self.grid_env


    def getAdjacentNodes(self):
        adj_nodes = {}
        for i in range(self.rows):
            for j in range(self.cols):
                for delta in [1, -1]:
                    #Checking for North and South
                    if (i+delta) < self.rows or (i+delta) < self.cols:
                        if not self.isBlockOccupied(i+delta, j):
                            adj_nodes[(i, j)] = [(i+delta, j)] 

                    if (j+delta) < self.rows or (j+delta) < self.cols:
                        if not self.isBlockOccupied(i+delta, j):
                            adj_nodes[(i, j)] = [(i+delta, j)] 

        return adj_nodes    
        
    def isBlockOccupied(self, x, y) -> bool:
        if self.grid_env[x][y] == 1 :   
            return self.grid_env[x][y]
        else:
            return 0

    
    def getObstacles(self):
        obstacle_counter = 0
        obstacle_placed = 0

        while obstacle_counter < self.obstacles_required:

            rand_x_cord = rnd.randint(0, self.rows-2)
            rand_y_cord = rnd.randint(0, self.cols-2)

            random_tetro_shape = rnd.choice(self.tetro)

            shape_width = len(random_tetro_shape[0])
            shape_height = len(random_tetro_shape)

            for r_ in range(rand_x_cord, rand_x_cord+shape_height): 
                random_tetro_row = r_ - rand_x_cord
                for c_ in range(rand_y_cord, rand_y_cord+shape_width): 
                    random_tetro_col = c_ - rand_y_cord

                    if random_tetro_shape[random_tetro_row][random_tetro_col]:
                            if r_ < (self.rows-1) and c_ < (self.cols-1):
                                if not self.grid_env[r_][c_]:
                                    self.grid_env[r_][c_] = 1
                                    obstacle_counter += 1
                               
            obstacle_placed += 1
    

    def displayPos(self, x_, y_, color):
        rect = pygame.Rect(x_*block_size, y_*block_size, block_size, block_size)
        pygame.draw.rect(self.screen, color, rect, 0)



