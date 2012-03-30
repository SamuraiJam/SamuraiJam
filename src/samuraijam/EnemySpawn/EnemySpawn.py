from Song import Song
from Note import Note
import random

NO_ENEMY = 0
MINE = 1
ENEMY_1 = 2
ENEMY_2 = 3

PROB_NONE = 0
PROB_MINE = .5
PROB_1 = .5
PROB_2 = .5

DIFF = 0
CHUNK = 2

class EnemySpawn:
	def __init__(self, song):
		self.chunk = (int)((60000/song.bpm)*CHUNK)
		self.end = max(song.notes[DIFF])
		#notes = {0: (False, False, False, False, False)}
		newnote = [False, False, False, False, False]
		self.enemies = {0: [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]}
		for time in range(self.chunk, self.end+self.chunk, self.chunk):
			#newnote = notes[time-chunk]
			for subtime in range(time-self.chunk+1, time):
				if subtime in song.notes[DIFF]:
					note = song.notes[DIFF][subtime]
					if (not note.type) and note.value == 0:
						newnote[0] = False
					if (not note.type) and note.value == 1:
						newnote[1] = False
					if (not note.type) and note.value == 2:
						newnote[2] = False
					if (not note.type) and note.value == 3:
						newnote[3] = False
					if (not note.type) and note.value == 4:
						newnote[4] = False
			for subtime in range (time-self.chunk+1, time):
				if subtime in song.notes[DIFF]:
					note = song.notes[DIFF][subtime]
					if note.type and note.value == 0:
						newnote[0] = True
					if note.type and note.value == 1:
						newnote[1] = True
					if note.type and note.value == 2:
						newnote[2] = True
					if note.type and note.value == 3:
						newnote[3] = True
					if note.type and note.value == 4:
						newnote[4] = True
			#notes[time] = newnote
			numTrue = 0
			trueIndex = None
			for i in range(0, 5):
				if newnote[i]:
					numTrue = numTrue + 1
					trueIndex = i
			if numTrue == 0:
				self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
			elif numTrue == 1:
				r = random.random()
				if r < PROB_NONE:
					self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
				else:
					if r < PROB_MINE:
						self.enemies[time] = [MINE, MINE, MINE, MINE, MINE]
						self.enemies[time][trueIndex] = NO_ENEMY
					else:
						r = random.random()
						trueIndex = int(5*(r-PROB_MINE)/PROB_MINE)
						if r < PROB_1:
							self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
							self.enemies[time][trueIndex] = ENEMY_1
						elif r < PROB_1+PROB_2:
							self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
							self.enemies[time][trueIndex] = ENEMY_2
			elif numTrue >= 2:
				r = random.random()
				if r < PROB_NONE:
					self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
				else:
					r = random.random()
					trueIndex = int(5*r)
					if r < PROB_1:
						self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
						self.enemies[time][trueIndex] = ENEMY_1
					elif r < PROB_1+PROB_2:
						self.enemies[time] = [NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY, NO_ENEMY]
						self.enemies[time][trueIndex] = ENEMY_2

				