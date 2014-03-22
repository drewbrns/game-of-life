#   /usr/bin/env python
import random
from game.torus import Torus
from game.ui import GUI


class GameOfLife(object):
    
    '''
    Game of Grid
    
        1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    '''    
    
    def __init__(self, rows, columns, ratio=0.4):
        self.ratio = ratio
        self.size = (rows, columns)
        self.board = Torus(self.size[0], self.size[0])        
        
        self.ui = GUI()
        self.ui.master.title('''Conway's Game of Life''')
        self.ui.setup_game(self.board)        
        self.seed()
        
    def seed(self):
        ''' 
            The initial pattern constitutes the seed of the system 
        '''
        population = self.board.grid 
        k = int(self.ratio * self.size[0])
        
        for x in xrange(k):
            population[x] = [1] * self.size[0]
            
        self.board.grid = population                  
                 
    def tick(self):
        '''  
            The first generation is created by applying the above rules simultaneously 
            to every cell in the seed
            Returns a new grid which results when the rules of the game are 
            simultaneously applied to the old grid
        '''
        old_grid = self.board.grid            
        new_grid = self.board.populate_grid()
        
        for y, row in enumerate(old_grid):
            for x, c in enumerate(row):
                neighbours_alive = self.board.count_neighbours(x,y)
                previous_state = old_grid[y][x]
                should_live = neighbours_alive == 3 or (neighbours_alive == 2 and previous_state == 1)
                new_grid[y][x] = should_live

        self.board.grid = new_grid       

    def animate(self):
        self.ui.update_screen(self.board)
        self.tick()
        self.ui.after(200, self.animate)


    def run(self):
        '''
            
        '''      
        self.animate()  
        self.ui.mainloop()            
        




if __name__ == '__main__':
    goL = GameOfLife(100,100)
    goL.run()
    
