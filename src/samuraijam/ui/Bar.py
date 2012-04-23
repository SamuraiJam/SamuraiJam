import os, sys
import pygame
from samuraijam.util.Helpers import *
from pygame.locals import *

class Bar:

    def __init__(self, surface, frontColor, backColor, curValue, maxValue, width, height, x, y):
        self.surface = surface
        self.frontColor = frontColor
        self.backColor = backColor
        self.curValue = curValue
        self.maxValue = maxValue
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        self.maxRect = pygame.Rect(x, y, width, height)
        minWidth = int((float(curValue)/float(maxValue))*width)
        self.minRect = pygame.Rect(x, y, minWidth, height)
        
        self.draw()        
        
        
    def update(self, newCurValue):
        self.curValue = self.curValue + newCurValue
        if self.curValue > self.maxValue:
            self.curValue = self.maxValue
        minWidth = int((float(self.curValue)/float(self.maxValue))*self.width)
        self.minRect = pygame.Rect(self.x, self.y, minWidth, self.height)
        self.draw()
        
    def draw(self):
        pygame.draw.rect(self.surface, self.backColor, self.maxRect, 0)
        pygame.draw.rect(self.surface, self.frontColor, self.minRect, 0)