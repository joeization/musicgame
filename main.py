import pygame
import sys
import random
from spec import *
from particle import *
from parse import *
from node import *
from sys import exit

global size
size = (1440, 900)
black = (0, 0, 0)
white = (255, 255, 255)
title = "Pygame"

n_hit = [0]
n_all = [0]
combo = [0]
score = [0]
base = (size[0]-200)/2
pos = (base, base+50, base+100, base+150)
skey = ['d', 'f', 'j', 'k']


def add_particle(ParticleList, keyBuf, enemy, fbuf, sound):
    global n_hit, combo, score
    for i in xrange(4):
        if keyBuf[ord(skey[i])]:
            #sound.play()
            fbuf[i] = 100
            if len(enemy[i]) > 0:
                score[0] += int(30*(1+combo[0]/50))
                combo[0] += 1
                del enemy[i][0]
                n_hit[0] += 1
                #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                for k in xrange(4):
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    ParticleList.append(Particle(pos[i], size[1]-100, 20, color))
            keyBuf[ord(skey[i])] = False


def add_node(NodeList):
    k = random.randint(0, 3)
    color = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    NodeList.append(Node(pos[k]+50, color, k, 0))


def main():

    ParticleList = []
    NodeList = []
    enemy = [[] for x in xrange(4)]

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)

    global n_hit
    global n_all
    global combo
    global score

    keyBuf = [False] * 1024

    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    font = pygame.font.SysFont("monospace", 20)
    fade = pygame.image.load("fade.png").convert_alpha()
    bk = []
    bk.append(pygame.image.load("left.png").convert_alpha())
    bk.append(pygame.image.load("right.png").convert_alpha())
    fbuf = [0]*4

    total_time = 0
    now_index = 0

    p = Parse(0, 1)
    tmpNode = p.parse("bmap.txt")

    pygame.mixer.music.load(sys.argv[1])
    pygame.mixer.music.play(1)
    sound = pygame.mixer.Sound("ding.ogg")

    clock.tick(0)
    while True:
        tik = clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    total_time = 0
                    NodeList = []
                    now_index = 0
                    n_hit = [0]
                    n_all = [0]
                    combo = [0]
                    score = [0]
                    enemy = [[] for x in xrange(4)]
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(1)
                    print 'reset'
                keyBuf[event.key] = True
            if event.type == pygame.KEYUP:
                keyBuf[event.key] = False

        screen.fill(black)

        while now_index < len(tmpNode) and total_time >= tmpNode[now_index].time:
            NodeList.append(Node(tmpNode[now_index].x, tmpNode[now_index].color, tmpNode[now_index].ind,
                tmpNode[now_index].time))
            now_index += 1

        nx, ny = pygame.mouse.get_pos()

        add_particle(ParticleList, keyBuf, enemy, fbuf, sound)
        for x in xrange(4):
            screen.blit(bk[x % 2], (pos[x]-25, size[1]-600))
            if fbuf[x] > 0:
                fade.set_alpha(fbuf[x]/100)
                screen.blit(fade, (pos[x]-25, size[1]-200))
                fbuf[x] -= 10

        pygame.draw.line(screen, white, (0, size[1]-100), (size[0], size[1]-100), 3)
        showNode(screen, NodeList, enemy, combo, n_all, tik)
        showParticle(screen, ParticleList)

        if(n_all[0] != 0):
            rate = round(1.0*n_hit[0]/n_all[0], 4)
        else:
            rate = 0
        label = font.render(str(rate*100)+"%", 1, (255, 255, 0))
        screen.blit(label, (100, 100))

        if combo[0] > 10:
            label = font.render(str(combo[0])+"combo", 1, (255, 255, 0))
            screen.blit(label, (700, 100))

        label = font.render("Score: "+str(score[0]), 1, (255, 255, 0))
        screen.blit(label, (400, 100))

        label = font.render("FPS: "+str(int(clock.get_fps())), 1, (255, 255, 0))
        screen.blit(label, (100, 300))

        pygame.display.update()
        total_time += float(tik)/1000
        clock.tick(60)

if __name__ == "__main__":
    main()
