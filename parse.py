from node import *
import random

'''
k = random.randint(0, 3)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
NodeList.append(Node(pos[k], color, k, 0))
'''
size = (1440, 900)
base = (size[0]-200)/2
pos = (base, base+50, base+100, base+150)


class Parse(object):

    def __init__(self, offset, width):
        self.offset = offset
        self.width = width

    def parse(self, path):
        buf = []
        bmpfile = open(path)
        for s in bmpfile:
            try:
                t, k = map(float, s.strip().split(' '))
                k = int(k)
                color = (random.randint(128, 255), random.randint(
                    128, 255), random.randint(128, 255))
                buf.append(Node(pos[k], color, k, t*self.width+self.offset))
            except:
                pass
        return buf
