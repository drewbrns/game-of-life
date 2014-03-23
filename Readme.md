#Game of Life

John Conway, a mathematician from Cambridge, invented the “Game of Life” in 1970. The game plays on a torus populated by cells that are either living or dead. The initial population is 60:40 (i.e. 40% living cells). After each round, the new population is determined following these rules:

##Rules of the Game
	1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
	2. Any live cell with two or three live neighbours lives on to the next generation.
	3. Any live cell with more than three live neighbours dies, as if by overcrowding.
	4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

##Features
	- Implement the logic of the game of life. Choose appropriate data structures.
	- Come up with a graphic user interface (GUI) that allows the user to start, pause and reset the simulation. You must use TkInter for implementing the GUI.
	- Allow the user to adjust the additional population ratio (default is 60:40) as well as the size of the torus (width and height).
	
##Advanced Features
	- Implement a "next" button that allows the user to step through the simulation at their own pace.
	- Implement a "previous" button that allows the user to go back to the n (e.g. 10) previous simulation steps.
	
	
##Known Issues
	- Only square sized torus (eg. 50 x 50) are currently supported.
	- Torus of size above 100 x 100 has not been tested, for best performance use torus of size of 60 x 60 and below.	

#To play the game
	- This game uses only python standard modules
	- To begin playing, run the script > python run_game.py
