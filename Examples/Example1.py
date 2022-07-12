from pyspritex import *

game = Game(background_color="blue", physics=True, resizable=True)

shape = GameObject(game, background_color="red")

game.add_game_object(shape)


def on_update():
    shape.x += 1


game.on_update = on_update

game.run()
