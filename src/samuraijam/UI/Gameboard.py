'''
Created on Apr 4, 2012

@author: jaywaldron
'''

from pygame import Surface, Rect

class Gameboard(object):
    '''
    classdocs
    '''


    def __init__(self, surface, width, height, song_file):
        '''
        Constructor
        '''
        self.windowSurface = surface
        self.gameSurface = Surface(width, height) # This will be drawn every frame to the window
        backgroundWidth = 10
        self.backgroundSurface = Surface(backgroundWidth, height)
        
        
    def draw(self):
        self.gameSurface.fill((0, 0, 0))        
        Surface.blit(self.backgroundSurface, self.gameSurface, Rect())
        #All other drawing
        Surface.blit(self.windowSurface, self.gameSurface)
        