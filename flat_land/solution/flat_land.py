#!/usr/bin/python3
import pygame
from obstacle_field_env import*
from search_path import BreadthFirstSearch
from env_utils import*
from time import sleep


def main():


     #Initialise pygame
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(COLOR_BLACK)
    pygame.display.set_caption("Flat Land "+ str(grid_width)+ " x "+ str(grid_width))

    #Generate grid N x N
    grid = Grid(screen, grid_width, grid_height, block_size, tetro)
    grid.getObstacles()
    grid.drawGrid()

    #TODO
    #call planner get path
    start_pos = (1,1)
    goal_pos = (grid.rows-1, grid.cols-1)

    #Display start and goal pos
    grid.displayPos(start_pos[0], start_pos[1], COLOR_GREEN)
    grid.displayPos(goal_pos[0], goal_pos[1], COLOR_RED)

    planner = BreadthFirstSearch(start_pos, goal_pos, grid) #TODO
    path = planner.findPath()
    path =  [(5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 14), (6, 15), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 14), (7, 15), (8, 5), (8, 6), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (9, 5), (9, 6), (9, 7), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 7), (13, 8), (13, 9), (13, 12), (13, 13), (13, 14), (13, 15), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 12), (14, 13), (14, 14), (14, 15), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)]

    #Declare clock to tick robot time steps
    clock = pygame.time.Clock()

    i = 0
    running = True
    while running:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # file_name = "./obstacle_field_%s_occupancy.jpg" % obstacle_occupancy_percent
                # pygame.image.save(screen, file_name)
                running = False

        if i < len(path):
            grid.displayPos(path[i][0], path[i][1], COLOR_AQUA)
            i = i+1
            sleep(0.5)    

if __name__ == '__main__':
        main()



