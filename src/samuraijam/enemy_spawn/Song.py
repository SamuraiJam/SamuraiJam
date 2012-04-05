#import Note

AMAZING_DIFFICULTY      = 0
MEDIUM_DIFFICULTY       = 1
EASY_DIFFICULTY         = 2
SUPAEASY_DIFFICULTY     = 3

class Song:
	def __init__(self):
		self.bpm = 0
		self.notes = {
			0: {},
			1: {},
			2: {},
			3: {}
		}
	
	
	def set_bpm(self, bpm):
		self.bpm = bpm
	
	def add_note(self, difficulty, note):
		self.notes[difficulty][note.time] = note
