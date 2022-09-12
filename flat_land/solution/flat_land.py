from multiprocessing.spawn import import_main_path
import pygame
from obstacle_field_env import Grid
from search_path import*
from env_utils import*

pygame.init()



if __name__ == '__main__':

    
    screen = pygame.display.set_mode(( screen_width, screen_height))
    screen.fill(COLOR_BLACK)
    grid = Grid(screen, grid_width, grid_height, block_size, tetro)
    pygame.display.set_caption("Flat Land "+ str(grid.grid_width)+ " x "+ str(grid.grid_height))
    grid_env = grid.getGridEnv()
    grid.checkObstacles()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # file_name = "./obstacle_field_%s_occupancy.jpg" % obstacle_occupancy_percent
                # pygame.image.save(screen, file_name)
                running = False
        
       
        search_path = BreadthFirstSearch(source=[0,0], target=[5,5], grid_env=grid_env)
        search_path.findPath()
        
        grid.drawGrid()


        pygame.display.flip()
    
    pygame.quit()