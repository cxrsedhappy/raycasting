import cmath
import uu

import pygame
import math
from settings import *


class LocalPlayer:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = Player.position
        self.angle = Player.angle
        self.speed = Player.speed

    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
        if keys[pygame.K_d]:
            self.y += self.speed * math.cos(self.angle)
            self.x -= self.speed * math.sin(self.angle)
        if keys[pygame.K_a]:
            self.y -= self.speed * math.cos(self.angle)
            self.x += self.speed * math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x -= self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle)

        if keys[pygame.K_LEFT]:
            self.angle -= Player.rotation
        if keys[pygame.K_RIGHT]:
            self.angle += Player.rotation

    def render(self):
        pygame.draw.circle(self.screen, Colour.purple, (self.x, self.y), 12)
        cos_distance = Player.ray * math.cos(self.angle)
        sin_distance = Player.ray * math.sin(self.angle)
        pygame.draw.line(self.screen, Colour.red, self.pos(), [self.x + cos_distance, self.y + sin_distance], 1)

    def mapping(self, x, y):
        return (x // Tile.w_size) * Tile.w_size, (y // Tile.h_size) * Tile.h_size

    def ray_casting(self):
        start_angle = (self.angle - (Player.pov / 2) * (math.pi / 180))

        px, py = self.mapping(self.x, self.y)
        h_depth, v_depth = 0, 0

        for ray in range(Player.n_rays):
            current_angle = start_angle + ray * Player.angle_delta
            cos_a = math.cos(current_angle)
            sin_a = math.sin(current_angle)

            # vertical
            x, dx = (px + Tile.w_size, 1) if cos_a >= 0 else (px, -1)
            for _ in range(0, Window.width, Tile.w_size):
                v_depth = (x - self.x) / cos_a
                y = self.y + v_depth * sin_a
                if self.mapping(x + dx, y) in world_map:
                    break
                x += dx * Tile.w_size

            # horizontal
            y, dy = (py + Tile.h_size, 1) if sin_a >= 0 else (py, -1)
            for _ in range(0, Window.height, Tile.h_size):
                h_depth = (y - self.y) / sin_a
                x = self.x + h_depth * cos_a
                if self.mapping(x, y + dy) in world_map:
                    break
                y += dy * Tile.h_size

            depth = min(v_depth, h_depth)
            # depth = min(v_depth, h_depth, Player.ray)
            # pygame.draw.line(self.screen, Colour.white, self.pos(),
            #                  [self.x + depth * cos_a,
            #                  self.y + depth * sin_a],
            #                  1)

            depth *= math.cos(self.angle - current_angle)
            projectile_height = Player.projectile / depth
            col = 255 / (1 + depth * depth * .00001)
            pygame.draw.rect(self.screen, (col, col, col),
                             (ray * Player.scale, Window.height // 2 - projectile_height // 2,
                              Player.scale, projectile_height))

    def update(self):
        self.movement()
        self.ray_casting()
        # self.render()
