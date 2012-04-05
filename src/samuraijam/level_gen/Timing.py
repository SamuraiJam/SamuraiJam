'''
Created on Apr 3, 2012

@author: Matt Halpern
'''
import pygame
import os, sys
#from samuraijam.Control.HAL import HAL
import time
from Helpers import *
from pygame.locals import *
if not pygame.mixer: print 'Warning, sound disabled'

"""Initialize PyGame"""
pygame.init()

"""Joystick"""
joy = pygame.joystick.Joystick(0)
joy.init()

'''
buttonMap = {0 : HAL.GREEN, 1 : HAL.RED, 2 : HAL.BLUE, 3 : HAL.YELLOW, 4 : HAL.ORANGE, 6 : HAL.BACK, 7 : HAL.START}
axisMap = {4 : HAL.WHAMMY, 2 : HAL.EFFECT, 3 : HAL.TILT}
hatMap = {0 : HAL.STRUM}

axisDefault = {4 : -1.0}
hatDefault = {}

hal9000 = HAL(buttonMap, axisMap, hatMap, axisDefault, hatDefault)
'''

pygame.mixer.music.load("guitar.ogg")
pygame.mixer.music.play()

old_time = time.clock()

out = open("times.txt", "w")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            if joy.get_button(0)==1:
                new_time = time.clock()
                lapsed = new_time - old_time
                out.writelines("{0}\n".format(lapsed))
                old_time = new_time
            if joy.get_button(1)==1:
                out.close()