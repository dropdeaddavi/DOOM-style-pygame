import pygame
import sys
from Settings import *
from map import *
from player import *
from object_renderer import *
from raycasting import *

icon = pygame.image.load("gargoyle.png")
pygame.display.set_icon(icon)

class Game:

    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("DOOM-STYLE")

    def draw(self):
        # self.screen.fill("black")
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.checkEvent()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
