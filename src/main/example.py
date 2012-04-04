#! /usr/bin/python

## \file  example.py
#  \brief A example of using the menu system
#  \author Scott Barlow
#  \date 2009
#  \version 1.0.0
#
#  An example script to create a window and explore some of the features of the
#  menu class I've created.
#
#  Of particular interest may be 'Menu 3' which has the buttons 'Rand Colors'
#  and 'Rand Config'.  Play with these buttons to truly see the power of this
#  menu class.  You can dynamically change things, add buttons, remove buttons,
#  etc.
#
#  Follow the prompts at the buttom of the screen.  Keep in mind that this
#  example has all image buttons just go to the next menu screen.  Use enter
#  to select a button and the arrow keys to move around a menu.  Pressing the
#  'Exit' button when available or pressed Esc will exit the program.  Press 'r'
#  on a button and it will be removed from the menu (one 'button' must remain
#  though).
#
#  Small 'button' images are from SpriteLib by Ari Feldman, available at:
#  <http://www.flyingyogi.com>
#
#  The background image is from "Nasa/courtesy of nasaimages.org."
#  <http://www.nasaimages.org/>
#
#
#       Copyright 2009 Scott Barlow
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA or see <http://www.gnu.org/licenses/>.
#
#
#  Changelog
#     V1.0.0 - Initial Release
#     V1.0.1 - Mac OS compatibility change
#     V1.0.2 - No change to this file
#     V1.0.3 - No change to this file
#


#-------------------------------------------------------------------------------
#---[ Imports ]-----------------------------------------------------------------
#-------------------------------------------------------------------------------
import sys, pygame, random
from menu import *
from image import *


## ---[ main ]------------------------------------------------------------------
#  This function runs the entire screen and contains the main while loop
#
def main():
   # Uncomment this to center the window on the computer screen
   os.environ['SDL_VIDEO_CENTERED'] = '1'

   # Uncomment this to position the screen x_ and y_ pixels from the top left
   # corner of the monitor/screen
   #x_ = 560
   #y_ = 100
   #if os.name != 'mac':
   #   os.environ['SDL_VIDEO_WINDOW_POS'] = str(x_) + "," + str(y_)

   # Initialize Pygame
   pygame.init()

   # Create a window of 800x600 pixels
   screen = pygame.display.set_mode((800, 600))

   # Set the window caption
   pygame.display.set_caption("Menu Example - (c) Scott Barlow")

   # Load some images to use for sample buttons
   image1  = load_image('1.png', 'images')
   image2  = load_image('2.png', 'images')
   image3  = load_image('3.png', 'images')
   image4  = load_image('4.png', 'images')
   image5  = load_image('5.png', 'images')
   bkg = load_image('bkg.jpg', 'images')

   # Set a background image - this is to show that the buttons will be
   # transparent around the text/image so it is safe to use this menu over a
   # picture - just make sure that the picture it will be written to is on the
   # screen that you pass into as the background for the menu when it is
   # created.  We must draw everything we want onto the surface before creating
   # the button if we want the background to be applied correctly.
   screen.blit(bkg, (0, 0))
   pygame.display.flip()

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu0 = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
                [('Next Menu',      1, None),
                 ('Next Menu',      1, None),
                 ('Next Menu',      1, None),
                 ('Menu 1 (Next)',  1, None),
                 ('Menu 2',         2, None),
                 ('Menu 3',         3, None),
                 ('Next Menu',      1, None),
                 ('Exit',           9, None)])

   menu1 = cMenu(20, 400, 20, 5, 'horizontal', 4, screen,
                [('Previous Menu',  0, None),
                 ('Next Menu',      2, None),
                 ('Menu 0',         0, None),
                 ('Menu 2 (Next)',  2, None),
                 ('Menu 3',         3, None),
                 ('Next Menu',      2, None),
                 ('Next Menu',      2, None),
                 ('Exit',           9, None)])

   menu2 = cMenu(0, 0, 5, 5, 'horizontal', 7, screen,
                [('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2),
                 ('Next Menu', 3, image3),
                 ('Next Menu', 3, image4),
                 ('Next Menu', 3, image5),
                 ('Next Menu', 3, image1),
                 ('Next Menu', 3, image2)])

   menu3 = cMenu(25, 15, 20, 5, 'vertical', 7, screen,
                [('Prev Menu',          2, None),
                 ('Add',                4, None),
                 ('Center',             5, None),
                 ('Set (0, 0)',         6, None),
                 ('Rand Colors',        7, None),
                 ('Rand Config',        8, None),
                 ('Next Menu',          0, None),
                 ('Image',              0, image1),
                 ('Image',              0, image2),
                 ('Image',              0, image3),
                 ('Image',              0, image4),
                 ('Image',              0, image5),
                 ('Next Menu',          1, None),
                 ('Exit',               9, None)])

   # Center menu2 at the center of the draw_surface (the entire screen here)
   menu2.set_center(True, True)

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # seen the random number generator (used here for choosing random colors
   # in one of the menu when that button is selected)
   random.seed()

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

         if state in [0, 1, 2, 3]:
            # Reset the screen before going to the next menu.  Also, put a
            # caption at the bottom to tell the user what is going one
            screen.blit(bkg, (0, 0))
            screen.blit(TEXT[state][0], (15, 530))
            screen.blit(TEXT[state][1], (15, 550))
            screen.blit(TEXT[state][2], (15, 570))
            pygame.display.flip()

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
         if state == 0:
            rect_list, state = menu0.update(e, state)
         elif state == 1:
            rect_list, state = menu1.update(e, state)
         elif state == 2:
            rect_list, state = menu2.update(e, state)
         elif state == 3:
            rect_list, state = menu3.update(e, state)
         elif state == 4:
            menu3.add_buttons([('A-Nothing!', 3, None),
                               ('A-Menu 0',   0, None),
                               ('A-Exit',     9, None)])
            state = 3
         elif state == 5:
            menu3.set_center(True, True)
            state = 3
         elif state == 6:
            menu3.set_center(False, False)
            menu3.set_position(0, 0)
            state = 3
         elif state == 7:
            RGB_available_colors = xrange(0,255)

            new_color = (random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors))
            menu3.set_unselected_color(new_color)
            print 'New Unselected Color = ', new_color

            new_color = (random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors))
            menu3.set_selected_color(new_color)
            print 'New Selected Color = ', new_color

            new_color = (random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors),
                         random.choice(RGB_available_colors))
            menu3.set_image_highlight_color(new_color)
            print 'New Image Highlight Color = ', new_color

            print ' '
            state = 3
         elif state == 8:
            new_thickness = random.choice((1, 2, 3, 4, 5, 6, 7, 8))
            menu3.set_image_highlight_thickness(new_thickness)
            print 'New Image Highlight Thickness = ', new_thickness

            new_h_pad = random.choice(xrange(0, 20))
            new_v_pad = random.choice(xrange(0, 20))
            menu3.set_padding(new_h_pad, new_v_pad)
            print 'New Horizontal Padding = ', new_h_pad
            print 'New Vertical Padding = ', new_v_pad

            new_orientation = random.choice(('vertical', 'horizontal'))
            menu3.set_orientation(new_orientation)
            if new_orientation == 'vertical':
               new_change_number = random.choice(xrange(5, 12))
            elif new_orientation == 'horizontal':
               new_change_number = random.choice(xrange(2, 5))
            print 'New Orientation = ', new_orientation

            menu3.set_change_number(new_change_number)
            print 'New Change Number = ', new_change_number

            new_v_alignment = random.choice(('top', 'center', 'bottom'))
            new_h_alignment = random.choice(('left', 'center', 'right'))
            menu3.set_alignment(new_v_alignment, new_h_alignment)
            print 'New Vertical Alignment = ',   new_v_alignment
            print 'New Horizontal Alignment = ', new_h_alignment


            print ' '
            state = 3
         else:
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if e.type == pygame.KEYDOWN:
         if e.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

      # Update the screen
      pygame.display.update(rect_list)


## ---[ The python script starts here! ]----------------------------------------
# Run the script
if __name__ == "__main__":
   main()


#---[ END OF FILE ]-------------------------------------------------------------
