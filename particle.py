import pygame
import random


class Particle(object):

    def __init__(self, x, y, rem, color):
        self.x = x
        self.y = y
        self.rem = rem
        self.color = color

    def die(self):
        return self.rem < 0

    def move(self):
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.rem -= 1

    def blit(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rem, 0)


def showParticle(screen, ParticleList):
    index = 0
    while(index < len(ParticleList)):
        ParticleList[index].move()
        if not ParticleList[index].die():
            ParticleList[index].blit(screen)
            index += 1
        else:
            del ParticleList[index]
