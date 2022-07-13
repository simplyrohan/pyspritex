# pyspritex

> NOTE: This package is an unofficial extension to [pygame](https://www.pygame.org/) and all graphical capabilities are credited to pygame.
 
 <br>
pyspritex is a package to make desktop app production in Python more streamlined.

## Installation

For the latest version:
```bash
git clone https://github.com/simplyrohan/pyspritex.git
```

For the stable release
```
pip install pypritex
```

## Basic Usage

There are two fundamental classes that you will need; ```Game``` and ```GameObject```. The first is for managing the window and the running of the game. The latter to manage objects in the game.

Ex.
```python
from pyspritex import *

game = Game(background_color="blue", resizable=True) # Initilize a game object and define it's properties

shape = GameObject(game, background_color="red") # Initilize a shape and define it's properties

game.add_game_object(shape) # Add shape to game

if __name__ == "__main__":
    game.run() # 

```

For more check out the wiki!

## Contribute
This package is by no means complete, so feel free to make contributions or open issues!