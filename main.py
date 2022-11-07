import pygame
from settings import *
from localplayer import LocalPlayer
from map import Map


class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Window.width, Window.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = LocalPlayer(self.screen)
        self.world = Map(self.screen)

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(Colour.black)

            self.world.update()
            self.player.update()

            pygame.display.flip()
            self.clock.tick()


def main():
    engine = Engine()
    engine.start()


if __name__ == '__main__':
    main()
