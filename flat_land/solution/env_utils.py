
import random
import math

#Grid params
grid_width = 8
grid_height = 8	
block_size = 50 

#Screen params
screen_width = grid_width*block_size
screen_height = grid_height*block_size

#Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 200, 0)
COLOR_RED = (200, 0, 0)
COLOR_AQUA = (0,255,255)
COLOR_LIGHTBLUE = (100,149,237)

obstacle_occupancy_percent = 10

# #Tetrominos
tetro = [
    
    #T
    [[1, 1, 1],
	 [0, 1, 0]	],
	
    #s
	[[0, 1, 1],
	 [1, 1, 0]],
	
    #z
	[[1, 1, 0],
	 [0, 1, 1]],
	
    #j
	[[1, 0, 0],
	 [1, 1, 1]],
	
    #l
	[[0, 0, 1],
	 [1, 1, 1]],
	
    #i
	[[1, 1, 1],
     [0, 0, 0]],
	
    #dot
	[[1, 1],
	 [1, 1]]

]

