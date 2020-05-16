import pygame
from Game_number_1.Constants import *
from Game_number_1.player import *


class Main:
    def __init__(self, screen_0):
        self.screen = screen_0
        self.player = Player('Nils')
        self.background = pygame.image.load("png/background_2.jpg")
        self.running = True
        self.main_loop()

    def handle_events(self):
        pass

    def render(self):
        # прорисовка всего-всего

        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        pygame.display.flip()

    def main_loop(self):
        # основной цыкл программы

        while self.running is True:
            self.render()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Main(screen)
