#!/usr/bin/env python3
#TODO
#	colour options
#	transparency
#	filters
#	rotate
#	flip
#	Use different characters depending on the image
from PIL import Image, ImageSequence
import time, os

if os.name == 'nt':
	os.system("") # hack to get \x1b escape codes working on windows

class gif:
	def __playonce(self, speed: int): #play the selected gif once
		try:
			for frame in ImageSequence.Iterator(Image.open(self.filename)): # go through each frame
				frame = frame.resize((self.width, self.height), Image.NEAREST) # you can use Image.BICUBIC or others
				pixels = frame.convert('RGB')
				width, height = frame.size
				img = ''

				for h in range(height): # make this into a generator, cuz faster
					for w in range(width):
						img += '\x1b[38;2;' + ';'.join(list(map(str, pixels.getpixel((w, h))))) + 'm' + self.char
					img += '\n'
				print(img)

				#NOTE sometimes duration is not found by PIL, handle this better
				sleep = frame.info['duration'] / 1_000 if 'duration' in frame.info else 30
				time.sleep(sleep / speed)
				self.clear(height + 1)
		except KeyboardInterrupt:
			return

	def play(self, count: int or bool, speed = 1):
		playType = type(count)

		if playType == bool:
			while playType:
				self.__playonce(speed)

		elif playType == int: #
			for i in range(count):
				self.__playonce(speed)
		else:
			raise TypeError('Count must be of type `bool` or `int`!')

	def __init__(self, filename: str, width = 100, height = 50, char = '@'):
		self.clear = lambda amount: print('\x1b[1A\x1b[2K' * amount, end = '') # translates to go up one line in cli and delete said line
		self.end = '\x1b[0m' # stop colours

		self.filename = filename
		self.width = width
		self.height = height
		self.char = char

gif('b2.gif', char = '█', width = 130).play(3)
gif('missile.gif', char = '█', width = 130).play(1, speed = 5)
gif('missiles.gif', char = '█', width = 130).play(1, speed = 5)
gif('iran.gif', char = '█', width = 130).play(1, speed = 5)
gif('missile2.gif', char = '█', width = 130).play(1, speed = 5)
gif('missiles2.gif', char = '█', width = 130).play(1, speed = 4)
gif('missile3.gif', char = '█', width = 130).play(1, speed = 4)
gif('icbm2.gif', char = '█', width = 130).play(1, speed = 4)
gif('explode2.gif', char = '█', width = 130).play(1)
gif('explode.gif', char = '█', width = 130).play(1)
#newGif.play(True) # play until interrupted
#newGif.play(2) # play twice
