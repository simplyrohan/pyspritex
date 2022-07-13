from .constants import *
try:
    import pygame
except ModuleNotFoundError:
    raise PygameNotFound("Please install pygame, or make it accessible to pyspritex")
from typing import Union


class PhysicsGroup:
    def __init__(self, gravity=1, screen_size=None, enabled=True):
        self.gravity = gravity
        self.objects = []
        self.screen_size = screen_size
        self.enabled = enabled

    def add_game_object(self, game_object):
        self.objects.append(game_object)

    def update(self):
        if self.enabled:
            for game_obj in self.objects:
                if self.screen_size is not None:
                    if game_obj.y+game_obj.height < self.screen_size[1]:
                        game_obj.y += self.gravity
                else:
                    game_obj.y += self.gravity

    def check_pos(self, game_obj, x, y):
        success = True

        if x+game_obj.width > self.screen_size[0] and x < 0:
            x = False

        if y+game_obj.height > self.screen_size[1] and y < 0:
            y = False

        self.objects = [GameObject(Game())]

        for game_object in self.objects:
            if game_obj.rect.move(x, y).colliderect(game_object):
                success = False

        return not success


class Game:
    def __init__(self, width: int = 500, height: int = 500, resizable: bool = False,
                 background_color: Union[str, tuple] = "white", physics: bool = False, fps: Union[int, float] = 24):

        self.resizable = resizable

        if self.resizable:
            self.surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        else:
            self.surface = pygame.display.set_mode((width, height))

            self.raw_background_color = background_color

        if type(background_color) == tuple:
            self.background_color = background_color
        else:
            self.background_color = get_color(background_color)

        self.surface.fill(self.background_color)

        self.game_objects = []

        self.window_width, self.window_height = pygame.display.get_window_size()

        self.physics_groups = []

        self.default_physics_group = PhysicsGroup(gravity=1, screen_size=(self.window_width, self.window_height),
                                                  enabled=False)
        if physics:
            self.default_physics_group.enabled = True

        self.fps = fps

        self.running = False

        self.on_update = None

    def add_game_object(self, game_object):
        try:
            self.game_objects.index(game_object)
        except ValueError:
            self.game_objects.append(game_object)
            game_object.game = self
            if game_object.physics_group is None:

                game_object.physics_group = self.default_physics_group
            else:
                self.physics_groups.append(game_object.physics_group)


    def update(self):
        self.window_width, self.window_height = pygame.display.get_window_size()

        try:
            self.on_update()
        except TypeError:
            pass

        self.surface.fill(self.background_color)
        for game_object in self.game_objects:
            self.surface.blit(game_object.surface, game_object.pos)

        self.default_physics_group.update()
        self.default_physics_group.screen_size = self.window_width, self.window_height

        for physics_group in self.physics_groups:
            physics_group.update()
            physics_group.screen_size = self.window_width, self.window_height

        pygame.display.flip()

        pygame.time.wait(int(100/self.fps))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.update()


class GameObject:
    def __init__(self, height: Union[int, float] = 50, width: Union[int, float] = 50,
                 xy: Union[list, tuple] = (0, 0), background_color: Union[str, tuple] = "gray",
                 physics_group: PhysicsGroup = None):

        self.height, self.width = height, width
        assert len(xy) == 2
        self._x, self._y = xy[0], xy[1]
        self._pos = xy

        self.raw_background_color = background_color

        if type(background_color) == tuple:
            self.background_color = background_color
        else:
            self.background_color = get_color(background_color)

        self.surface = pygame.Surface((self.height, self.width))
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        self.surface.fill(background_color)

        self._physics_group = physics_group
        if self._physics_group is not None:
            self._physics_group.add_game_object(self)

        self.game = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if self.physics_group is not None:
            if self.physics_group.check_pos(self, (value, self.y)):
                self._x = value
                self.pos = self._x, self._y
            else:
                self.x = self.physics_group.screen_size[0]-self.width



    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if self.physics_group.check_pos(self, (self.x, value)):
            self._y = value
            self.pos = self._x, self._y
        else:
            self.y = self.physics_group.screen_size[1]-self.height

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value: tuple):
        self._pos = value
        self._x = value[0]
        self._y = value[1]

    @property
    def physics_group(self):
        return self._physics_group

    @physics_group.setter
    def physics_group(self, value: PhysicsGroup):
        self._physics_group = value
        self._physics_group.add_game_object(self)
