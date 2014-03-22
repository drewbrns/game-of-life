# /usr/bin/env python

class Torus(object):    
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self.grid = self.populate_grid()
        
    def populate_grid(self):
        return [[0 for x in xrange(self.rows)] for y in xrange(self.cols)]
        
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
        
    def is_alive(self, x, y):
        c = self.grid[x][y]
        return c
        
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
     