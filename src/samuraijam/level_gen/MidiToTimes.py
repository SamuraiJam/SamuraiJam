'''
Created on Apr 19, 2012

@author: Matt Halpern
'''
from samuraijam.enemy_spawn.midi.MidiOutStream import MidiOutStream
from samuraijam.enemy_spawn.midi.MidiInFile import MidiInFile

class MidiToTimes(MidiOutStream):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.output = open("../../../data/midi-times.txt", "w")
        self.sum = 0.0
        self.output.writelines("{0}\n".format(str(0)))
        self.prev_time = 0
        
    def note_on(self, channel=0, note=0x40, velocity=0x40):
        if channel == 0:
            time = self.abs_time()
            rel_time = time - self.prev_time
            self.prev_time = time
            if time != 0:
                self.sum = self.sum + rel_time
                if self.sum > 0:
                    self.output.writelines("{0}\n".format(self.sum/500.0))
                    self.sum = 0.0
                
                           
if __name__ == '__main__':
    
    event_handler = MidiToTimes()

    infile = "../../../data/lmfao-sexy_and_i_know_it_v2.mid"
    midi_in = MidiInFile(event_handler, infile)
    midi_in.read()

   