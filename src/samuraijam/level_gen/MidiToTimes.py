'''
Created on Apr 19, 2012

@author: Matt Halpern
'''
from samuraijam.enemy_spawn.midi.MidiOutStream import MidiOutStream
from samuraijam.enemy_spawn.midi.MidiInFile import MidiInFile

INPUT = "katy_perry-firework.mid"
OUTPUT = "firework-times.txt"
#channel is one less than what anvil gives
CHANNEL = 3
BPM = 124

class MidiToTimes(MidiOutStream):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.output = open("../../../data/" + OUTPUT, "w")
        self.output.writelines("{0}\n".format(str(0)))
        self.prev_time = 0
        
    def note_on(self, channel=0, note=0x40, velocity=0x40):
        if channel == CHANNEL:
            time = self.abs_time()
            rel_time = time - self.prev_time
            self.prev_time = time
            if rel_time != 0:
                self.output.writelines("{0}\n".format(rel_time*self.SCALE))
                
                
    def eof(self):
        self.output.close()
        
    def header(self, format=0, nTracks=1, division=96):
        if division > 0:
            self.SCALE = ((60.0/BPM)/division)
        else:
            self.SCALE = (-1.0/division)
                
                           
if __name__ == '__main__':
    
    event_handler = MidiToTimes()

    infile = "../../../data/" + INPUT
    midi_in = MidiInFile(event_handler, infile)
    midi_in.read()

   