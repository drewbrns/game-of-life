# /usr/bin/env python

from cell import Cell

class Torus(object):    
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self.grid = self.populate_grid()
        
    def populate_grid(self):
        # import random
        # Cell(False)
        return [[0 for x in range(self.rows)] for y in range(self.cols)]
        
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, rows):
        self._rows = rows
    
    @property
    def cols(self):
        return self._cols
        
    @cols.setter    
    def cols(self, cols):
        self._cols = cols
        
    def count_neighbours(self, x, y):
        '''
            Returns the number of neighbours of a cell which are alive.
            
            Parameters        
            :x ---- x position of cell in torus
            :y ---- y position of cell in torus
            
            Returns:
            :count_neighbours_alive ---- number of neighbours alive
        '''            
        neighbours = []
        append = neighbours.append
        
        x1 = self.rows-1 if x-1 < 0 else x
        append(self.grid[y][x1-1])
        
        x1 = 0 if x+1 > self.rows-1 else x
        append(self.grid[y][x1+1])
        
        y1 = self.cols-1 if y-1 < 0 else y        
        append(self.grid[y1-1][x])

        y1 = 0 if y+1 > self.cols-1 else y
        append(self.grid[y1+1][x])

        x1 = self.rows-1 if x-1 < 0 else x
        y1 = self.cols-1 if y-1 < 0 else y        
        append(self.grid[y1-1][x1-1])
        
        x1 = 0 if x+1 > self.rows-1 else x
        y1 = self.cols-1 if y-1 < 0 else y                
        append(self.grid[y1-1][x1+1])

        x1 = self.rows-1 if x-1 < 0 else x
        y1 = 0 if y+1 > self.cols-1 else y             
        append(self.grid[y1+1][x1-1])
        
        x1 = 0 if x+1 > self.rows-1 else x
        y1 = 0 if y+1 > self.cols-1 else y                     
        append(self.grid[y1+1][x1+1])
            
        count_neighbours_alive = len(filter(lambda x:x==True, neighbours))
                        
        return count_neighbours_alive
    
                
    def simulate_life(self):
        '''
        Returns a new grid which results when the rules of the game are 
        simultaneously applied to the old grid
        '''
        
        for generation in range(10):

            # new_grid = [[Cell(False) for x in range(self.rows)] for y in range(self.cols)]
            
            new_grid = self.populate_grid()
            
            for y, row in enumerate(self.grid):
                for x, c in enumerate(row):
                    neighbours_alive = self.count_neighbours(x,y)
                    previous_state = self.grid[y][x]
                    should_live = neighbours_alive == 3 or (neighbours_alive == 2 and previous_state == 1)
                    new_grid[y][x] = should_live

            self.grid = new_grid        
        
        
        
if __name__ == '__main__':
    t = Torus(5,5)
    import pprint

    pprint.pprint(t.grid)
    print 
    
    # import random
    # 
    # population = t.grid 
    # 
    # for row in population:
    #             
    #     k = int(0.4 * len(row))
    # 
    #     alive = random.sample(list(row), k)
    #                                         
    #     for c in alive:
    #         
    #         c.alive = True
    #         
    #     
    # t.grid = population
    # # pprint.pprint(t.grid)
    # 


    t.count_neighbours(4,4)
  
    t.simulate_life()
    