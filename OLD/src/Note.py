
NOTE_ON = True
NOTE_OFF = False

class Note:
	
	def __init__(self, time, value, type, velocity, channel):
		self.time = time
		self.value = value
		self.type = type
		self.velocity = velocity
		self.channel = channel
