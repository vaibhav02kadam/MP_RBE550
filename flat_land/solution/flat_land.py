#!/usr/bin/python3
import pygame
from obstacle_field_env import*
from search_path import BreadthFirstSearch, DepthFirstSearch, Dijkstra, RandomPlanner
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

    #call planner get path
    start_pos = (1,1)
    goal_pos = (grid.rows-2, grid.cols-3)
    grid.grid_env[1][1] = 0
    grid.grid_env[grid.rows-2][grid.cols-3] = 0

    #Display start and goal pos
    grid.displayPos(start_pos[0], start_pos[1], COLOR_GREEN)
    grid.displayPos(goal_pos[0], goal_pos[1], COLOR_RED)

    # planner = BreadthFirstSearch(start_pos, goal_pos, grid)
    planner = Dijkstra(start_pos, goal_pos, grid)
    path = planner.findPath()
    
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
                grid.displayPos(path[i-1][0], path[i-1][1], COLOR_YELLOW)
               
                i = i+1
                sleep(0.5)    

if __name__ == '__main__':
        main()



