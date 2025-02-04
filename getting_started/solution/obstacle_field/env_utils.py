

#Grid params
grid_width = 128
grid_height = 128	
block_size = 8 

#Screen params
screen_width = grid_width*block_size
screen_height = grid_height*block_size

#Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (200, 200, 200)

obstacle_occupancy_percent = 70

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
