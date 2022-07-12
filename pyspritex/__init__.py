from .constants import *
try:
    import pygame
except ModuleNotFoundError:
    raise PygameNotFound("Please install pygame, or make it accessible to pyspritex")

else:
    from .objects import *
