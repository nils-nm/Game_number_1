import pygame
from Game_number_1.Constants import *


def render(screen):
    screen.blit()

    pass


class Player:
    def __init__(self, name):
        self.state = ALIVE
        self.direction = RIGHT
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ['kosmanaft.2.0.jpg']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 196, 196))
            i.append(temp.subsurface(196, 0, 196, 196))
            i.append(temp.subsurface(392, 0, 196, 196))
            i.append(temp.subsurface(588, 0, 196, 196))
            i.append(temp.subsurface(784, 0, 196, 196))
            self.images.append(i)

        self.moving = [0, 0, 0, 0]

    def move(self):
        pass

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):

        pass

