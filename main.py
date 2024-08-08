import pygame
from Constants import *
from player import *


class Main:
    def __init__(self, screen_0):
        self.screen = screen_0
        self.player = Player('Nils')
        self.background = pygame.image.load("png/background_2.jpg")
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.direction = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if event.key == pygame.K_s:
                    self.player.direction = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if event.key == pygame.K_a:
                    self.player.direction = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if event.key == pygame.K_w:
                    self.player.direction = UP
                    self.player.moving = [0, 0, 0, 1]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = 0
                if event.key == pygame.K_s:
                    self.player.moving[DOWN] = 0
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = 0
                if event.key == pygame.K_w:
                    self.player.moving[UP] = 0

    def render(self):
        # прорисовка всего-всего

        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        pygame.display.flip()

    def main_loop(self):
        # основной цыкл программы

        while self.running is True:
            self.player.move()
            self.render()
            self.handle_events()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Main(screen)
