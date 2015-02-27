import pygame
from pygame.locals import *

class BrushColor:
    def __init__(self):
        self.rect = None
        

    def brushBox(self,screen,color,x,y):
        rect = pygame.draw.rect(screen, color,Rect(x,y,30,30))
        return rect