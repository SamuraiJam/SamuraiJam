'''
Created on Apr 4, 2012

@author: Matt Halpern
'''
import random

PROB_MINE = .05
PROB_ENEMY = .07
#sum of probs must be 1
#2=groupie, 3=cop, 4=lawyer
PROB_ENEMY_TYPE = [(2, 0.6), (3, 0.3), (4, 0.1)]
PROB_DOWN = .4
PROB_UP = .4
PROB_BRIDGE = .05
PROB_POWERUP = .005
MOVE_FREQ = 8
START_STRING = 2

SONGS = ["sexy", "tiktok", "firework"]

for song in SONGS:
    input = open("../../../data/" + song + "-times.txt", "r")
    output = open("../../../data/levels" + song + "-level.txt", "w")
    linenumber = 0
    lastindex = START_STRING
    
    for line in input:
        linenumber = linenumber + 1
        line = line.rstrip()
        if linenumber == 1:
            output.write(str(0.0) + "\t")
        else:
            output.write(line + "\t")
        if linenumber % MOVE_FREQ == 1:
            r = random.random()
            if r < PROB_DOWN:
                move = -1
            elif r < 1-PROB_UP:
                move = 0
            else:
                move = 1
            if (lastindex == 0 and move == -1) or (lastindex == 5 and move == 1) or (move == 0):
                newindex = lastindex
            else:
                newindex = lastindex + move     
        else:
            newindex = lastindex
        bridgeline = ""
        newline = ""
        minindex = min(lastindex, newindex)
        maxindex = max(lastindex, newindex)
        for i in range(0, minindex):
            r = random.random()
            if r < PROB_MINE:
                newline = newline + "1"
            elif r < 1-PROB_POWERUP:
                newline = newline + "0"
            else:
                newline = newline + "5"
            r = random.random()
            if r < PROB_BRIDGE:
                bridgeline = bridgeline + "1"
            else:
                bridgeline = bridgeline + "0"
        r = random.random()
        if newindex == lastindex:
            if r < PROB_ENEMY:
                r = random.random()
                cum = 0
                for type, prob in PROB_ENEMY_TYPE:
                    if cum <= r and r < cum + prob:
                        newline = newline + str(type)
                    cum = cum + prob
            else:
                newline = newline + "0"
        else:
            newline = newline + "00"
            bridgeline = bridgeline + "1"
        for i in range(0, 5-maxindex):
            r = random.random()
            if r < PROB_MINE:
                newline = newline + "1"
            elif r < 1-PROB_POWERUP:
                newline = newline + "0"
            else:
                newline = newline + "5"
            r = random.random()
            if r < PROB_BRIDGE:
                bridgeline = bridgeline + "1"
            else:
                bridgeline = bridgeline + "0"
        lastindex = newindex
        output.write(bridgeline + "\t")
        output.write(newline + "\n")
    input.close()
    output.close()