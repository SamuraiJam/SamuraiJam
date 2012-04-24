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
from samuraijam.enemies.Enemy import Enemy
from samuraijam.enemies.MaleGroupie import MaleGroupie
from samuraijam.enemies.Lawyer import Lawyer
from samuraijam.enemies.Explosion import Explosion
from samuraijam.powerups.Healthpack import Healthpack
from samuraijam.player.attacks import *

PATH_HEIGHT = 72

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
        self.pixels_per_second = float(song_file.readline())
        self.level_filename = song_file.readline()
        self.pixel_offset = 0
        self.last_frame_time = -1
        self.frac_scroll = 0
#        print "{0}[{1}] : {2}".format(self.song_name, self.song_length, self.pixels_per_second)
        
#        self.background_width = (self.pixels_per_second * self.song_length) + width
        self.background_width = width + 96  # Jank scroll edition!
        background_size = (self.background_width, height)
        self.backgroundSurface = Surface(background_size)
        self.__render_background()
        
        self.backgroundSurface.set_colorkey((0,0,0),pygame.RLEACCEL)
        #self.backgroundSurface.set_colorkey((217,62,245),pygame.RLEACCEL)
        #self.backgroundSurface.set_alpha(100,pygame.RLEACCEL)
        
        self.mainScreenBackground,self.mainScreenBackgroundRect = load_image("sexy_background.png")
        
        #self.backgroundSurface.blit(mainScreenBackground, (0,0))
        #self.__render_background()
        
        possible_samurai_positions = []
        
        for i in range(0, 6):
            possible_samurai_positions.append(PATH_HEIGHT * i + 15)
        
        self.samurai = Samurai(possible_samurai_positions)
        self.samurai_sprite_group = Group(self.samurai)
        
        self.bridge_group = OrderedUpdates()
        self.mine_group = OrderedUpdates()
        self.enemy_group = OrderedUpdates()
        self.attack_group = OrderedUpdates()
        self.healthpack_group = OrderedUpdates()
        self.explosion_group = OrderedUpdates()
        
#        tempSprite = self.samurai_sprite_group.sprites()
#        tempRect = tempSprite[0].get_rect()
#        self.testSword = VerticalSlash(tempRect.centerx,tempRect.centery, self.remove_attack)
#        self.attack_group.add(self.testSword)
        
        if sys.platform == "win32":
            # On Windows, the best timer is time.clock()
            self.default_timer = time.clock
        else:
            # On most other platforms, the best timer is time.time()
            self.default_timer = time.time
            
        
        
    def draw(self):
        self.gameSurface.fill((0,0,0))
        #self.gameSurface.fill((217,62,245))
        origin = (0, 0)
#        this_scroll = 0
        self.scroll_amount = 0
        if self.last_frame_time > 0:
            cur_time = self.default_timer()
            self.gap_time = cur_time - self.last_frame_time
#            print "Pixels per second: {0}\nGap Time: {1}\nScrollAmount: {2}".format(self.pixels_per_second, self.gap_time, this_scroll)
            self.last_frame_time = cur_time
        else:
            self.gap_time = 0
            self.last_frame_time = self.default_timer()
            
        this_scroll = self.pixels_per_second * self.gap_time
    
        self.frac_scroll += this_scroll
        if self.frac_scroll >= 1:
            self.scroll_amount = math.floor(self.frac_scroll)
            self.pixel_offset += self.scroll_amount
#            print "Now scrolling {0} pixel(s)".format(whole_part)
            self.frac_scroll -= self.scroll_amount

        if self.pixel_offset > 96:
            self.pixel_offset = self.pixel_offset - 96
            if self.pixel_offset < 0:
                self.pixel_offset = 0
                     
        self.gameSurface.blit(self.mainScreenBackground, origin)
        
        window_rect = Rect(self.pixel_offset, 0, self.gameSurface.get_width(), self.gameSurface.get_height()) 
#        print window_rect
        self.gameSurface.blit(self.backgroundSurface, origin, window_rect)
        
        #All other drawing
        self.bridge_group.update(self.scroll_amount)
        self.bridge_group.draw(self.gameSurface)
        
        self.mine_group.update(self.scroll_amount)
        self.mine_group.draw(self.gameSurface)
        
        self.enemy_group.update(self.scroll_amount)
        self.enemy_group.draw(self.gameSurface)
        
        self.samurai_sprite_group.update()
        self.samurai_sprite_group.draw(self.gameSurface) 
        
        self.healthpack_group.update(self.scroll_amount)
        self.healthpack_group.draw(self.gameSurface)
        
        #self.testSword = VerticalSlash(400,400)
        #self.attack_group.add(self.testSword)
        self.attack_group.update()
        self.attack_group.draw(self.gameSurface)
        
        self.explosion_group.update()
        self.explosion_group.draw(self.gameSurface)
        
#        self.testSword.draw(self.gameSurface)
        
        
        
        for bridge in self.bridge_group.sprites():
            if bridge.rect.left < 0:
                self.bridge_group.remove(bridge)
            
        
        #Annnnd blast it back to the screen
        window_origin = (0, 60)
        self.windowSurface.blit(self.gameSurface, window_origin)
        
        
    def add_bridge(self, bridge_num):
#        print "FAKE BRIDGE"
        
        new_bridge = Bridge(1101, bridge_num * PATH_HEIGHT + 39)
        self.bridge_group.add(new_bridge)
        
    def add_mine(self, string_num):
#        print "CREATE ZE LANDMINE"
        new_mine = Mine(1101, PATH_HEIGHT * string_num + 42)
        self.mine_group.add(new_mine)
    
    def add_healthpack(self, string_num):
#        print "such a healthy young man!"
        new_healthpack = Healthpack(1101, PATH_HEIGHT * string_num + 42)
        self.healthpack_group.add(new_healthpack)
        
    def add_enemy(self, string_num):
        new_enemy = Enemy(1111, PATH_HEIGHT * string_num + 42)
        self.enemy_group.add(new_enemy)
        
    def add_male_groupie(self, string_num):
        new_enemy = MaleGroupie(1111, PATH_HEIGHT * string_num + 15)
        self.enemy_group.add(new_enemy)
        
    def add_lawyer(self, string_num):
        new_lawyer = Lawyer(1111, PATH_HEIGHT * string_num + 15)
        self.enemy_group.add(new_lawyer)
        
    def remove_attack(self, attack):
        self.attack_group.remove(attack)
        
    def add_attack(self, attack):
        self.attack_group.add(attack)
        
    def add_explosion(self, y_val):
        new_explosion = Explosion(20, y_val, self.explosion_group)
        
        
    def __render_background(self):
        # Jank implementation that just uses that one sprite over and over again!
        # Jay's jank dirtBlockThingy is 96x48 pixels
        num_blocks = int(math.ceil(self.background_width / 96.0))
        cur_width = 0
        for bI in range(0, num_blocks):
            for hI in range(0, 6):
                my_location = (cur_width, (PATH_HEIGHT * hI + 35))
                dp = DirtPath(my_location)
#                print "DirtPath at {0}".format(my_location)
                self.backgroundSurface.blit(dp.image, my_location)
            cur_width += 96
        
        