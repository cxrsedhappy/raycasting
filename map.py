import pygame
from settings import *


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map = world_map

    def render(self):
        for x, y in world_map:
            pygame.draw.rect(self.screen, Colour.laguna, (x, y, Tile.w_size, Tile.h_size), 1, 1)

    def update(self):
        # self.render()
        pass
