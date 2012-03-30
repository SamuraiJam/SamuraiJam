import pygame

pygame.init()

joy = pygame.joystick.Joystick(0)
joy.init()

print "Found a joystick: {0}".format(joy.get_name())

numaxes = joy.get_numaxes()
numbutton = joy.get_numbuttons()

try:
	while True :
		pygame.event.pump()
		for i in range(0, numaxes):
			roundAxis = round(joy.get_axis(i), 5)

			if roundAxis != 0.0:
				print "Axis {0} reads {1}".format(i, joy.get_axis(i))
		for i in range(0, numbutton):
			if joy.get_button(i) != 0:
				print "Button {0} reads {1}".format(i, joy.get_button(i))
except KeyboardInterrupt :
	joy.quit()
	print "Shutting down everything"