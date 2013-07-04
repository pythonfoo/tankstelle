import os 
import time
import random
import sys
class generator(object):
	def generatorA(runde, lastPrice):
		return lastPrice - 10
	def generatorB(runde, lastPrice):
		if lastPrice >= 50:
			return random.choice(range(1,51))
		if lastPrice >= 25 and lastPrice < 50:
			return random.choice(range(1,26))
		if lastPrice < 25:
			return random.choice(range(1,13))
	def generatorC(runde, lastPrice):
		return int(100-runde)
	def getAuthor():
		return 'dodo'