#! /usr/bin/env/python 

import Tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None, game=None):
        tk.Frame.__init__(self, master)
        self.grid() 
        self.create_widgets()
        
    def create_widgets(self):
        
        self.life_grid = tk.Frame(None,height=300,width=500)
        self.life_grid.grid(row=0, column=0)
        
        self.canvas = tk.Canvas(self.life_grid,height=270,width=490, borderwidth=1)
        self.canvas.grid(row=0, column=0,padx=5,pady=5)      
        
        self.options_pane = tk.Frame(None, height=30, width=500)
        self.options_pane.grid(row=1, column=0,pady=5)
        
        self.label_1 = tk.Label(self.options_pane, text='Size')
        self.label_1.grid(row=0,column=0)
        
        self.size_e = tk.StringVar()
        self.size_entry = tk.Entry(self.options_pane,width=5,textvariable=self.size_e)
        self.size_entry.grid(row=0,column=1)
        # self.size_e.set(self.config['size'])
        self.size_e.set(10)
        
        self.label_2 = tk.Label(self.options_pane, text='Ratio')        
        self.label_2.grid(row=0,column=2)                
        
        self.ratio_e = tk.StringVar()
        self.ratio_entry = tk.Entry(self.options_pane,width=5, textvariable=self.ratio_e)
        self.ratio_entry.grid(row=0,column=3)    
        # self.ratio_e.set(self.config['ratio'])            
        self.ratio_e.set(0.4)           
        
        self.start_button_e = tk.StringVar()
        self.start_button_e.set('Play')
        self.start_button = tk.Button(self.options_pane, textvariable=self.start_button_e, command=self.play_game)
        self.start_button.grid(row=0, column=4,padx=50)
        
        
    def play_game(self):
        pass
  
                        
    
    def setup_game(self, board):
        
        for x in xrange(board.rows):
            for y in xrange(board.cols):
                
                alive = board.is_alive(x,y)
                color = ''
                if alive:
                    color = 'white'
                else:
                    color = 'black'
        
                x0,y0 = x,y
                x0 *=10
                y0 *=10
                x1, y1 = x0+10, y0+10
                tag = '{},{}'.format(x,y)
                
                self.canvas.create_rectangle(y0, x0, y1, x1, fill=color,tags=tag)
                
                
                
    
    def update_screen(self, board):        
        '''
            Updates the canvas to show the current state of the game.
            
            Parameters:
            :board ---- 
        '''
        for x in xrange(board.rows):
            for y in xrange(board.cols):
                alive = board.is_alive(x,y)
                color = ""
                if alive:
                    color = "white"
                else:
                    color = "black"
              
                tag = '{},{}'.format(x,y)
                self.canvas.itemconfigure(tag, fill=color)
        
        
        # print 'update_screen'
        
        # self.canvas.delete('all')
        # 
        # for row in population:
        #     
        #     for cell in row:
        #     
        #         x0,y0 = cell.position
        #         x0 *=10
        #         y0 *=10
        #         x1, y1 = x0+10, y0+10
        #         
        #         if cell.alive:
        #             self.canvas.create_rectangle(x0, y0, x1, y1, fill='#000000')
        #         else:
        #             self.canvas.create_rectangle(x0, y0, x1, y1, fill='#FFFFFF')
                    
        
    def load_config(self):
        try:
            with open(r'config.json','r') as f:
                return json.load(f)
        except ValueError:
            return {'size':100, 'ratio':0.6}
        except IOError:
            pass
        
    def save_config(self, config):        
        with open('config.json','w') as f:
            json.dumps(config,f)
            f.write(json.dumps(config,f))
        

        
        
