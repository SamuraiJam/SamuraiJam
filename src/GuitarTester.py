'''
Created on Mar 31, 2012

@author: Dave Lee
'''

import pygame
import sys

"""Initialize PyGame"""
pygame.init()

"""Joystick"""
joy = pygame.joystick.Joystick(0)
joy.init()
numbutton = joy.get_numbuttons()
numaxis = joy.get_numaxes()
numhat = joy.get_numhats()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            for iB in range(0, numbutton):
                if(joy.get_button(iB)):
                    print "\n\n~~~Button down: {0}\n\n".format(iB)
                    
        elif event.type == pygame.JOYAXISMOTION:
            for iA in range(0, numaxis):
                if(joy.get_axis(iA) != 0.0):
                    print "\n\n@@@Axis #{0} now reads {1}".format(iA, joy.get_axis(iA))
                    
        elif event.type == pygame.JOYHATMOTION:
            for iH in range(0, numhat):
                if(joy.get_hat(iH) != 0.0):
                    print "\n\n###Hat #{0} now reads {1}".format(iH, joy.get_hat(iH))
