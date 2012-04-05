'''
Created on Apr 4, 2012

@author: jaywaldron
'''

from pygame import Surface, Rect
from pygame.sprite import Sprite, Group, OrderedUpdates
import math, time, sys

from samuraijam.spriteParts import DirtPath, Bridge
from samuraijam.player import Samurai
from samuraijam.enemies.Mine import Mine

class Gameboard(object):
    '''
    classdocs
    '''

    def __init__(self, surface, width, height, song_filename):
        '''
        Constructor
        '''
        self.windowSurface = surface
        self.width = width
        self.height = height
        self.song_filename = song_filename
        board_size = (width, height)
        self.gameSurface = Surface(board_size) # This will be drawn every frame to the window
        
        song_file = open(song_filename)
        self.song_name = song_file.readline()
        self.song_length = float(song_file.readline())
        self.pixels_per_second = float(song_file.readline())
        self.pixel_offset = 0
        self.last_frame_time = -1
        self.frac_scroll = 0
#        print "{0}[{1}] : {2}".format(self.song_name, self.song_length, self.pixels_per_second)
        
        self.background_width = (self.pixels_per_second * self.song_length) + width
        background_size = (self.background_width, height)
        self.backgroundSurface = Surface(background_size)
        self.__render_background()
        
        possible_samurai_positions = []
        
        for i in range(0, 6):
            possible_samurai_positions.append(48 * i + 5)
        
        self.samurai = Samurai(possible_samurai_positions)
        self.samurai_sprite_group = Group(self.samurai)
        
        self.bridge_group = OrderedUpdates()
        self.mine_group = OrderedUpdates()
        
        if sys.platform == "win32":
            # On Windows, the best timer is time.clock()
            self.default_timer = time.clock
        else:
            # On most other platforms, the best timer is time.time()
            self.default_timer = time.time
        
        
    def draw(self):
        self.gameSurface.fill((0, 0, 0))
        origin = (0, 0)
        this_scroll = 0
        self.scroll_amount = 0
        if self.last_frame_time > 0:
            cur_time = self.default_timer()
            gap_time = cur_time - self.last_frame_time
            this_scroll = self.pixels_per_second * gap_time
#            print "Pixels per second: {0}\nGap Time: {1}\nScrollAmount: {2}".format(self.pixels_per_second, gap_time, this_scroll)
            self.last_frame_time = cur_time
        else:
            self.last_frame_time = self.default_timer()
        self.frac_scroll += this_scroll
        if self.frac_scroll >= 1:
            self.scroll_amount = math.floor(self.frac_scroll)
            self.pixel_offset += self.scroll_amount
#            print "Now scrolling {0} pixel(s)".format(whole_part)
            self.frac_scroll -= self.scroll_amount
                     
        window_rect = Rect(self.pixel_offset, 0, self.gameSurface.get_width(), self.gameSurface.get_height()) 
#        print window_rect
        self.gameSurface.blit(self.backgroundSurface, origin, window_rect)
        
        #All other drawing
        self.bridge_group.update(self.scroll_amount)
        self.bridge_group.draw(self.gameSurface)
        
        self.mine_group.update(self.scroll_amount)
        self.mine_group.draw(self.gameSurface)
        
        self.samurai_sprite_group.update()
        self.samurai_sprite_group.draw(self.gameSurface)  
        
        
        for bridge in self.bridge_group.sprites():
            if bridge.rect.left < 0:
                self.bridge_group.remove(bridge)
            
        
        #Annnnd blast it back to the screen
        window_origin = (0, 60)
        self.windowSurface.blit(self.gameSurface, window_origin)
        
        
    def add_bridge(self):
#        print "FAKE BRIDGE"
        new_bridge = Bridge(1101, 0)
        self.bridge_group.add(new_bridge)
        
    def add_mine(self, string_num):
#        print "CREATE ZE LANDMINE"
        new_mine = Mine(1101, 48 * (string_num + 1))
        self.mine_group.add(new_mine)
        
        
        
    def __render_background(self):
        # Jank implementation that just uses that one sprite over and over again!
        # Jay's jank dirtBlockThingy is 96x48 pixels
        num_blocks = int(math.ceil(self.background_width / 96.0))
        cur_width = 0
        for bI in range(0, num_blocks):
            for hI in range(0, 6):
                my_location = (cur_width, (48 * hI + 35))
                dp = DirtPath(my_location)
#                print "DirtPath at {0}".format(my_location)
                self.backgroundSurface.blit(dp.image, my_location)
            cur_width += 96
        
        