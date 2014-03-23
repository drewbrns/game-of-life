#   /usr/bin/env python
import random
from game.torus import Torus
from game.ui import GUI


class GameOfThrones(object):
    
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
        self.ui.setup_screen(self.board)        
        self.ui.start_button.configure(command=self.start_game)
        self.ui.reset_button.configure(command=self.reset_game)
        self._appstate = ''        
        # self.seed()
        
    def seed(self):
        ''' 
            The initial pattern constitutes the seed of the system 
        '''
        population = self.board.grid 
        k = int(self.ratio * self.size[0])

        
        for row in population:
            
            # print row
            # print
                       
            for x in xrange(0,k+2,2):
                row[x] =  1
                
            # print row
                    
                    
            
        random.shuffle(population)
            
        self.board.grid = population                  
        
        
        
        
        # from pprint import pprint
        # pprint(self.board.grid)
        
                 
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
                new_grid[y][x] = int(should_live)

        self.board.grid = new_grid       

    def animate(self):
        '''
        '''
        self.ui.update_screen(self.board)
        self.tick()
        self._appstate = self.ui.after(200, self.animate)

    def run(self):
        '''
            
        '''      
        self.ui.mainloop()
        
    def start_game(self):
        '''
            Allows the user to start or pause the game.
        '''
        button_text = self.ui.start_button_text
        
        if button_text.get() == 'Start':
            self.animate()
            button_text.set('Pause')
        else:
            button_text.set('Start')
            self.ui.after_cancel(self._appstate)
            
        
    def reset_game(self):
        '''
            Allows the user to stop the game and reset it to it's initial state.
        '''
        button_text = self.ui.start_button_text
        button_text.set('Start')        
        self.ui.after_cancel(self._appstate)
        self.seed() 
        self.ui.after(0,self.ui.update_screen,self.board)
        
        
if __name__ == '__main__':
    goT = GameOfThrones(60,60)
    goT.run()
    
