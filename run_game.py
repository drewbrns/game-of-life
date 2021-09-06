# /usr/bin/env python
from game.ui import GameOfLife
from game.utility.config import Preferences


if __name__ == "__main__":
    p = Preferences()
    game_of_Thrones = GameOfLife(p.rows, p.columns, p.ratio)
    game_of_Thrones.run()
