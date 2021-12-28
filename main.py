"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def end_zero(lst):
        """
        move and put zeros in the end
        """
        lstz=[]
        for dummy_i in range(len(lst)) :

            if lst[dummy_i] != 0 :
                lstz.append(lst[dummy_i])
                
        for dummy_i in range(len(lst)):
            if len(lstz)<len(lst):
                lstz.append(0)
        return lstz

    def add_tile(lst):
        """
        add similar tiles
        """
        for dummy_i in range(0,len(lst)-1):
            if lst[dummy_i] == lst[dummy_i+1]:
                lst[dummy_i] = lst[dummy_i]*2
                lst[dummy_i+1] = 0
        return lst

    lst_1 = end_zero(line)
    lst_2 = add_tile(lst_1)
    lst_3 = end_zero(lst_2)
    return lst_3


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        #stuff for the move method
        up_list = [(0, col) for col in range(self._width)]
        down_list = [(self._height-1, col) for col in range(self._width)]
        left_list = [(row, 0) for row in range(self._height)]
        right_list = [(row, self._width-1) for row in range(self._height)]
        self._move_dict = {UP:up_list, DOWN:down_list, LEFT:left_list, RIGHT:right_list}
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self._grid = [[0 for dummy2 in range(self._width)] for dummy1 in range(self._height)]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direction_tiles = self._move_dict[direction]
        #print direction_tiles
        offset = list(OFFSETS[direction])
        
        times = 0
        if (direction == 1 or direction == 2):
            times = self._height
        elif (direction == 3 or direction == 4):
            times = self._width
        
        for current_tile in direction_tiles:
            tile = list(current_tile)
            temp_list = []
            temp_list.append(self.get_tile(tile[0], tile[1]))
            for dummy in range(times-1):
                tile[0] += offset[0]
                tile[1] += offset[1]
                temp_list.append(self.get_tile(tile[0], tile[1]))
            result = merge(temp_list)
            tile = list(current_tile)
            self.set_tile(tile[0], tile[1], result[0])
            for idx in range(1, times):
                tile[0] += offset[0]
                tile[1] += offset[1]
                self.set_tile(tile[0], tile[1], result[idx])
  
        self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #randomly select an empty square
        selected = False
        count = self._width * self._height
        while (selected != True and count != 0):
            row = random.randint(0, self._height-1)
            col = random.randint(0, self._width-1)
            if self.get_tile(row, col) == 0:
                selected = True
            if (selected == True):
                probable_value = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
                tile = random.choice(probable_value)
                self.set_tile(row, col, tile)
            count -= 1
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self._grid[row][col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """ 
        #print row, col
        return self._grid[row][col]
 


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))