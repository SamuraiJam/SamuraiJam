'''
Created on Apr 4, 2012

@author: Matt Halpern
'''
import random
import math

PROB_MINE = .5
PROB_ENEMY = .4
PROB_DOWN = .4
PROB_UP = .4
BRIDGE_FREQ = 4

input = open("times.txt", "r")
output = open("level.txt", "w")
linenumber = 0
lastindex = 2
for line in input:
    linenumber = linenumber + 1
    line = line.rstrip()
    output.write(line + "\t")
    if linenumber % BRIDGE_FREQ == 1:
        output.write("1\t")
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
        output.write("0\t")
        newindex = lastindex
    newline = ""
    minindex = min(lastindex, newindex)
    maxindex = max(lastindex, newindex)
    for i in range(0, minindex):
        r = random.random()
        if r < PROB_MINE:
            newline = newline + "1"
        else:
            newline = newline + "0"
    r = random.random()
    if newindex == lastindex:
        if r < PROB_ENEMY:
            newline = newline + "2"
        else:
            newline = newline + "0"
    else:
        newline = newline + "00"
    for i in range(0, 5-maxindex):
        r = random.random()
        if r < PROB_MINE:
            newline = newline + "1"
        else:
            newline = newline + "0"
    lastindex = newindex
    output.write(newline + "\n")
    