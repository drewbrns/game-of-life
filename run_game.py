# /usr/bin/env python
import random
from game.torus import Torus
from game.ui import GUI
from utility.config import Preferences

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
        self.board = Torus(self.size[0], self.size[1], self.ratio)        
        self._appstate = ''        
        self.setup_ui()
        self.seed()
        
    def setup_ui(self):
        self.ui = GUI()
        self.ui.master.title('''Drew's Game of Thrones''')
        self.ui.setup_screen(self.board)        
        self.ui.start_button.configure(command=self.start_game)
        self.ui.reset_button.configure(command=self.reset_game)
        self.ui.rows_text.set(self.size[0])
        self.ui.columns_text.set(self.size[1])
        self.ui.ratio_text.set(self.ratio)
        
    def apply_user_preferences(self):
        rows = int(self.ui.rows_text.get())
        columns = int(self.ui.columns_text.get())
        ratio = float(self.ui.ratio_text.get())                
        
        self.size = (rows, columns)
        self.ui.canvas.delete('all')        
        
        self.board = Torus(rows, columns, ratio)
        self.ui.setup_screen(self.board)
                    
        p = Preferences()
        config = {'rows':rows, 'columns':columns, 'ratio':ratio}
        p.save_config(config)                    

        self.ui.after(0, self.ui.update_screen,self.board)
        
    def seed(self):
        ''' 
            The initial pattern constitutes the seed of the system 
        '''
        self.board.populate_grid(self.ratio)
                 
    def tick(self):
        '''  
            The first generation is created by applying the above rules simultaneously 
            to every cell in the seed
            Returns a new grid which results when the rules of the game are 
            simultaneously applied to the old grid
        '''
        old_grid = self.board.grid            
        new_grid = self.board.populate_grid(self.ratio)
        
        for y, row in enumerate(old_grid):
            for x, c in enumerate(row):
                neighbours_alive = self.board.count_neighbours(x,y)
                previous_state = old_grid[y][x]
                should_live = neighbours_alive == 3 or (neighbours_alive == 2 and previous_state == 1)
                new_grid[y][x] = int(should_live)

        self.board.grid = new_grid       

    def animate(self):
        self.ui.update_screen(self.board)
        self.tick()
        self._appstate = self.ui.after(200, self.animate)

    def run(self):
        self.ui.mainloop()
        
    def start_game(self):
        '''
            Allows the user to start or pause the game.
        '''
        button_text = self.ui.start_button_text
                
        if button_text.get() == 'Start':
            # self.apply_user_preferences()            
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
        self.apply_user_preferences()                  
        
        
if __name__ == '__main__':
    p = Preferences()
    game_of_Thrones = GameOfThrones(p.rows, p.columns, p.ratio)
    game_of_Thrones.run()