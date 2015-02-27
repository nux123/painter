import pygame
from brush import Brush
from pygame.locals import *
from brushColor import BrushColor
from sys import exit

class Painter():
    def __init__(self):
        self.screen = pygame.display.set_mode((680,480),0,32)
        self.time_passed = pygame.time.Clock()
        self.brush = Brush(self.screen)
        
        
    def run(self):
        self.screen.fill((255,255,255))
        a = BrushColor()
        a.brushBox(self.screen, [56,88,96], 1, 1)
        while True:
            self.time_passed.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type==KEYDOWN:
                    pass
                elif event.type==MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type==MOUSEBUTTONDOWN:
                    self.brush.start_draw(event.pos)
                elif event.type==MOUSEBUTTONUP:
                    self.brush.end_draw()
                
            pygame.display.update()