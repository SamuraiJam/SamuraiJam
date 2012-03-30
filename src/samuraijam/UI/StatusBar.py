import os, sys
import pygame
from Helpers import *
from pygame.locals import *
from Bar import *

class StatusBar:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self,surface,color,width,height,x,y):
        self.surface = surface
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, 0)
        
        
        #sub bars
        self.barHeight = height*.5 #factor of how large the bar is. 1 = 100%
        self.barY = (height-self.barHeight)/2
        
        
        font = pygame.font.Font(None, 26)
        # Display some hpText and Bar
        hpPos = 400
        hpText = font.render("HP:", 1, (10, 10, 10))
        hpTextPos = hpText.get_rect()
        hpTextPos.centerx = hpPos - 20
        hpTextPos.centery = self.barY+hpText.get_rect().height
        surface.blit(hpText, hpTextPos)
        self.healthBar = Bar(surface=self.surface, frontColor=(255,0,0), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=hpPos, y=self.barY)

        # Display some mpText and Bar
        mpPos = 600
        mpText = font.render("Ki:", 1, (10, 10, 10))
        mpTextPos = mpText.get_rect()
        mpTextPos.centerx = mpPos - 20
        mpTextPos.centery = self.barY+mpText.get_rect().height
        surface.blit(mpText, mpTextPos)
        self.kiBar = Bar(surface=self.surface, frontColor=(0,0,255), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=mpPos, y=self.barY)
        
        # Display some expText and Bar
        expPos = 800
        expText = font.render("Rep:", 1, (10, 10, 10))
        expTextPos = expText.get_rect()
        expTextPos.centerx = expPos - 20
        expTextPos.centery = self.barY+expText.get_rect().height
        surface.blit(expText, expTextPos)
        self.kiBar = Bar(surface=self.surface, frontColor=(0,255,0), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=expPos, y=self.barY)

