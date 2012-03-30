from midi.MidiOutStream import MidiOutStream
from midi.MidiInFile import MidiInFile

AMAZING_DIFFICULTY      = "Amazing" #0
MEDIUM_DIFFICULTY       = "Medium" #1
EASY_DIFFICULTY         = "Easy" #2
SUPAEASY_DIFFICULTY     = "ULTRAEASY" #3

noteMap = {     # difficulty, note
  0x60: (AMAZING_DIFFICULTY,  0),
  0x61: (AMAZING_DIFFICULTY,  1),
  0x62: (AMAZING_DIFFICULTY,  2),
  0x63: (AMAZING_DIFFICULTY,  3),
  0x64: (AMAZING_DIFFICULTY,  4),
  0x54: (MEDIUM_DIFFICULTY,   0),
  0x55: (MEDIUM_DIFFICULTY,   1),
  0x56: (MEDIUM_DIFFICULTY,   2),
  0x57: (MEDIUM_DIFFICULTY,   3),
  0x58: (MEDIUM_DIFFICULTY,   4),
  0x48: (EASY_DIFFICULTY,     0),
  0x49: (EASY_DIFFICULTY,     1),
  0x4a: (EASY_DIFFICULTY,     2),
  0x4b: (EASY_DIFFICULTY,     3),
  0x4c: (EASY_DIFFICULTY,     4),
  0x3c: (SUPAEASY_DIFFICULTY, 0),
  0x3d: (SUPAEASY_DIFFICULTY, 1),
  0x3e: (SUPAEASY_DIFFICULTY, 2),
  0x3f: (SUPAEASY_DIFFICULTY, 3),
  0x40: (SUPAEASY_DIFFICULTY, 4),
}


class NotePrinter(MidiOutStream):
	"prints all note_on and note_off events"
	
	def tempo(self, value):
		bpm = 60.0 * 10.0**6 / value
		print "Tempo", value, "BPM", bpm
	
	def note_on(self, channel=0, note=0x40, velocity=0x40):
		print "On", channel, noteMap[note], velocity, self.abs_time()
			
	def note_off(self, channel=0, note=0x40, velocity=0x40):
		print "Off", channel, noteMap[note], velocity, self.abs_time()
			

event_handler = NotePrinter()

infile = "notes.mid"
midi_in = MidiInFile(event_handler, infile)
midi_in.read()

print "End of Line."