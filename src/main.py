from game import Game

if __name__ == "__main__":
    game = Game(title='python-g', cells_x=20, cells_y=20)
    game.run(fps=7)
