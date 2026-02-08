'''
2026 Spencer Trumbore
GNU 3.0 License

This program implements coloring an N x M rectangular grid
with X unique colors:

1.  If X < 4, randomly select a color for each tile.
2.  If X == 4, color the grid so that no two tiles with the
    same color share an edge.
3.  If X >= 5, color the grid so that no two tiles with the
    same color share a corner.
'''

import string
import re
import random

colors = set()
grid_size = []

class Tile:
    def __init__(self, color=None):
        self.color = color
        
    def __str__(self):
        if self.color:
            return self.color
        else:
            return '\u25A0'

def set_number_of_colors():
    while True:
        x = input("Enter number of colors:\t").strip()
        try:
            x = int(x)
            if x > 0:
                return x
                break
            else:
                print("Invalid number of colors.")
                print("1 <= number of colors <=26")
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")

def set_colors(number_of_colors):
    global colors
    try:
        int(number_of_colors) > 0 and int(number_of_colors) <= 26
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}: {e}")
        print("number_of_colors not set properly.")
    return set(string.ascii_uppercase[:number_of_colors])
    
def set_grid_size():
    while True:
        mn = input("Enter grid size M,N:\t")
        mn = mn.strip()
        pattern = re.compile(r'^\d+,\s*\d+$')
        
        try:
            match_result = re.match(pattern, mn)
            if match_result is None:
                raise ValueError
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")
            print("Invalid format for grid size.")
        
        MN = mn.split(',')
        
        try:
           MN[0] = int(MN[0])
           MN[1] = int(MN[1].strip())
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")
            print("At least one number couldn't be parsed.")
             
        try:
            if (MN[0] > 0) and (MN[1] > 0):
                grid_size = MN
                return grid_size
            else:
                raise ValueError
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")
            print("Both Numbers must be positive integers.")

def print_grid(grid):
    for row in grid:
        for obj in row:
            print(obj,end=' ')
        print()

def main():
    
    number_of_colors = set_number_of_colors()
    colors = set_colors(number_of_colors)
    grid_size = set_grid_size()
    
    # initialize grid with uncolored Tiles
    color_grid = [[Tile() for j in range(grid_size[1])] for i in range(grid_size[0])]
    
    if number_of_colors < 4:
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                color_grid[i][j].color = random.choice(list(colors))
                
    elif number_of_colors == 4:
        
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                used_colors = set()
                row_idx = [i-1,i,i,i+1] # only checking
                col_idx = [j,j-1,j+1,j] # cardinal neighbors
                for r, c in zip(row_idx, col_idx):
                    if r in range(grid_size[0]) and c in range(grid_size[1]):
                        if color_grid[r][c] is not None and color_grid[r][c].color is not None:
                            used_colors.add(color_grid[r][c].color)
                possible_colors = colors - used_colors
                color_grid[i][j].color = random.choice(list(possible_colors))

    else:
        
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                used_colors = set()
                row_idx = [i-1,i-1,i-1,i,i,i+1,i+1,i+1] # checking
                col_idx = [j-1,j,j+1,j-1,j+1,j-1,j,j+1] # octodirectional neighbors
                for r, c in zip(row_idx, col_idx):
                    if r in range(grid_size[0]) and c in range(grid_size[1]):
                        if color_grid[r][c] is not None and color_grid[r][c].color is not None:
                            used_colors.add(color_grid[r][c].color)
                possible_colors = colors - used_colors
                color_grid[i][j].color = random.choice(list(possible_colors))
    
    print_grid(color_grid)
    
if __name__ == '__main__':
    main()