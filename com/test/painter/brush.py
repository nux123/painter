import pygame
from pygame.locals import *
from sys import exit
import math

class Brush():
    def __init__(self,screen):
        self.screen = screen
        self.size = 1
        self.color = (0,0,0)
        self.drawing =False
        self.last_pos = None
        self.space = 1
        self.style = False
        self.brush = pygame.image.load("snow.gif").convert_alpha()
        self.brush_now = self.brush.subsurface((0,0), (1, 1))
    
    def set_brush_style(self,style):
        self.style=style;
    def get_brush_style(self):
        return self.style
    
    def set_size(self,size):
        if size<0.5: size = 0.5
        elif size>50: size = 50
        self.size = size
        self.brush_now = self.brush.subsurface((0,0), (size*2, size*2))
    def get_size(self):
        return self.size
    
    def start_draw(self,pos):
        self.last_pos = pos
        self.drawing=True
    def end_draw(self):
        self.drawing=False
    def get_point(self,pos):
        points = [ (self.last_pos[0], self.last_pos[1]) ]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in xrange(int(length)):
            points.append(
                    (points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x:(int(0.5+x[0]), int(0.5+x[1])), points)
        return list(set(points))
    
    def draw(self,pos):
        if self.drawing:
            for p in self.get_point(pos):
                if self.style ==False:
                    pygame.draw.circle(self.screen,self.color,p,self.size*2)
                else :
                    self.screen.blit(self.brush_now,p)
            self.last_pos = pos
