"""
module for testing guitar hero controller
used to debug and log button mappings
"""
import pygame

pygame.init()

joy=pygame.joystick.Joystick(0)
joy.init()

numbutton = joy.get_numbuttons()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            for i in range(0, numbutton):
                if joy.get_button(i)==1:
                    print "Button {0} reads {1}".format(i, joy.get_button(i))