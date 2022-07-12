from pyspritex import *

game = Game(background_color="blue", resizable=True)

shape = GameObject(game, background_color="red")

game.add_game_object(shape)

if __name__ == "__main__":
    game.run()
