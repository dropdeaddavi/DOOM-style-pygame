import pygame
import sys
from Settings import *
from map import *
from player import *

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("DOOM")

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

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
