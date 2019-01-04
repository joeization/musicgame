import pygame
import random

hit_range = 30
size = (1440, 900)


class Node(object):

    def __init__(self, x, color, ind, time):
        self.x = x
        self.y = 0
        self.color = color
        self.ind = ind
        self.time = time
        self.has = random.randint(0, 1024)
        self.isin = False

    def move(self, enemy, n_all, tik):
        self.y += (size[1]-100-hit_range)*tik/1000
        if(self.y >= (size[1]-100-hit_range) and not self.isin):
            n_all[0] += 1
            enemy[self.ind].append(self.has)
            self.isin = True

    def die(self, enemy, combo):
        if(self.y >= (size[1]-100+hit_range)) and self.has in enemy[self.ind]:
            enemy[self.ind].remove(self.has)
            combo[0] = 0
        return self.y > size[1] or (self.y >= (size[1]-100-hit_range)) and not self.has in enemy[self.ind]

    def blit(self, screen):
        #pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 10)
        g = 255*self.y/(size[1])
        color = (255-g, g, 128)
        pygame.draw.rect(screen, color, (self.x-20, self.y-5, 40, 10), 0)
        #pygame.draw.rect(screen, self.color, (self.x-20, self.y-5, 40, 10), 0)


def showNode(screen, NodeList, enemy, combo, n_all, tik):
    index = 0
    while(index < len(NodeList)):
        NodeList[index].move(enemy, n_all, tik)
        if not NodeList[index].die(enemy, combo):
            NodeList[index].blit(screen)
            index += 1
        else:
            del NodeList[index]
