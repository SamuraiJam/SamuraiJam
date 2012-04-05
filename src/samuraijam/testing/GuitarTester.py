'''
Created on Mar 31, 2012

@author: Dave Lee
'''

import pygame
import sys
from samuraijam.control.HAL import HAL

"""Initialize PyGame"""
pygame.init()

"""Joystick"""
joy = pygame.joystick.Joystick(0)
joy.init()

buttonMap = {0 : HAL.GREEN, 1 : HAL.RED, 2 : HAL.BLUE, 3 : HAL.YELLOW, 4 : HAL.ORANGE, 6 : HAL.BACK, 7 : HAL.START}
axisMap = {4 : HAL.WHAMMY, 2 : HAL.EFFECT, 3 : HAL.TILT}
hatMap = {0 : { (0, -1) : HAL.STRUM_DOWN, (0, 1) : HAL.STRUM_UP} }

axisDefault = {4 : -1.0}
hatDefault = {}

hal9000 = HAL(buttonMap, axisMap, hatMap, axisDefault, hatDefault)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            guitarState = hal9000.parseButton(joy)
            for key, value in guitarState.iteritems():
                print "{0} is {1}".format(key, value)
        elif event.type == pygame.JOYAXISMOTION:
            guitarState = hal9000.parseAxis(joy)
            for key, value in guitarState.iteritems():
                print "{0} is {1}".format(key, value)
        elif event.type == pygame.JOYHATMOTION:
            guitarState = hal9000.parseHat(joy)
            for key, value in guitarState.iteritems():
                print "{0} is {1}".format(key, value)
            
                