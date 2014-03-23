#! /usr/bin/env/python 

import Tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid() 
        self.create_widgets()
        
    def create_widgets(self):
        self.life_grid = tk.Frame(None, height=300, width=500)
        self.life_grid.grid(row=0, column=0)
        
        self.canvas = tk.Canvas(self.life_grid,height=275, width=490, borderwidth=1)
        self.canvas.grid(row=0, column=0, padx=2, pady=2)      
        
        self.toolbar = tk.Frame(None, height=30, width=500)
        self.toolbar.grid(row=1, column=0, pady=5)
        
        self.label_1 = tk.Label(self.toolbar, text='Size')
        self.label_1.grid(row=0, column=0)
        
        self.rows_text = tk.StringVar()
        self.rows_entry = tk.Entry(self.toolbar,width=5,textvariable=self.rows_text)
        self.rows_entry.grid(row=0, column=1)
        
        self.label_2 = tk.Label(self.toolbar, text='x', padx=5)
        self.label_2.grid(row=0, column=2)        
        
        self.columns_text = tk.StringVar()
        self.columns_entry = tk.Entry(self.toolbar,width=5,textvariable=self.columns_text)
        self.columns_entry.grid(row=0, column=3)
        
        spacer = tk.Frame(self.toolbar, height=30, width=3)
        spacer.grid(row=0, column=4, padx=5)        
        
        self.label_3 = tk.Label(self.toolbar, text='Ratio')        
        self.label_3.grid(row=0, column=5)                
        
        self.ratio_text = tk.StringVar()
        self.ratio_entry = tk.Entry(self.toolbar, width=5, textvariable=self.ratio_text)
        self.ratio_entry.grid(row=0,column=6)    
        
        self.reset_button = tk.Button(self.toolbar, text='Reset')
        self.reset_button.grid(row=0, column=7, padx=8)          
        
        spacer = tk.Frame(self.toolbar, height=30, width=85)
        spacer.grid(row=0, column=8, padx=2)
        
        self.start_button_text = tk.StringVar()
        self.start_button = tk.Button(self.toolbar, textvariable=self.start_button_text)
        self.start_button.grid(row=0, column=9, padx=2)
        self.start_button_text.set('Start')
        
    def setup_screen(self, board):
        '''
            Display initial state of grid on the screen 
        '''
        for x in xrange(board.rows):
            for y in xrange(board.cols):
                
                alive = board.is_alive(x,y)
                color = ''
                if alive:
                    color = 'black'
                else:
                    color = 'white'
        
                x0,y0 = x,y
                x0 *=10
                y0 *=10
                x1, y1 = x0+10, y0+10
                
                tag = '{},{}'.format(x,y)
                self.canvas.create_rectangle(y0, x0, y1, x1, fill=color,tags=tag)
                
    def update_screen(self, board):        
        '''
            Updates the canvas to show the current state of the grid.
            
            Parameters:
            :board ---- 
        '''
        for x in xrange(board.rows):
            for y in xrange(board.cols):
                alive = board.is_alive(x,y)
                color = ""
                if alive:
                    color = "black"
                else:
                    color = "white"
              
                tag = '{},{}'.format(x,y)
                self.canvas.itemconfigure(tag, fill=color)
