from random import randint, choice, random
from twisted.internet import reactor, defer

class FreeWill(object):
	def __init__(self):
		self.brain = [randint(0, 9) for i in range(40)] #Random noise
		self.preferences = {'left' : [8, 4], 'right' : [7, 4]} #No preference
		self.total = [0, 0]
		#INFO
		#Number 2 -> left | More likely to pick left than right | represented by 5
		#Number 3 -> right | Less likely to pick right than left | represented by 4
	def log(self, info, message):
		print "[%s]: %s" % (info, message)

	def generateNoise(self,*args):
		self.brain = [randint(0, 9) for i in range(40)]
		self.makeDecision()
		reactor.callLater(2, freewill.generateNoise)

	def makeDecision(self):
		l, r = self.preferences['left'][1], self.preferences['right'][1]
		self.log("PREFS", "L = %s, R = %s" % (l, r))
		self.log("INFO", str(self.brain))
		while l + r > 0:
			if random() > .5:
				index = randint(0, len(self.brain) - 1)
				self.brain[index] = self.preferences['left'][0]
				l -= 1
			else:
				index = randint(0, len(self.brain) - 1)
				self.brain[index] = self.preferences['right'][0]
				r -= 1				
		l, r = self.brain.count(self.preferences['left'][0]), self.brain.count(self.preferences['right'][0])
		self.decisionMade(l, r)

	def decisionMade(self, l, r):
		if l > r:
			self.total[0] +=1
			self.log("PICKED", "Left")
		elif l < r:
			self.total[1] +=1
			self.log("PICKED", "Right")
		else:
			self.log("PICKED", "Neither")
		self.log("TOTAL", "Left picked %s and right picked %s" % (self.total[0], self.total[1]))

	def loop(self, d=None):
	    if not d:
	        d = defer.Deferred()
	    else:
	        d.callback()
	    reactor.callLater(1, self.generateNoise, d)	        
	    return d

freewill = FreeWill()
deferred = freewill.loop()
reactor.callLater(2, freewill.generateNoise)
reactor.run()
