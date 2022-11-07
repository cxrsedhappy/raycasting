import math


class Window:
    width = 1280
    height = 720


class MiniMap:
    width = 100
    height = 100


class Colour:
    black = 0, 0, 0
    white = 255, 255, 255
    purple = 109, 35, 148
    laguna = 44, 86, 156
    red = 171, 22, 57


class Tile:
    w_size = Window.width // 16
    h_size = Window.height // 9


class Player:
    position = (Window.width / 2, Window.height / 2)
    angle = -90 * (math.pi / 180)
    rotation = 0.02

    speed = 2

    ray = 700

    pov = 90
    n_rays = 300
    angle_delta = (pov / n_rays) * (math.pi / 180)

    dist = n_rays / (2 * math.tan(pov / 2))
    projectile = 7 * dist * Tile.w_size
    scale = Window.width // n_rays


text_map = ["################",
            "#.........#....#",
            "#.#...#...#.#..#",
            "#.#...#...#.#..#",
            "#.#...#...#.#..#",
            "#######...#.####",
            "#.....#........#",
            "#.#.#......#.###",
            "################"]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "#":
            world_map.add((i * Tile.w_size, j * Tile.h_size))

