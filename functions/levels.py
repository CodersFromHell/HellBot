import discord, time, random
import user

class Level():
	def __init__(self, user : CustomUser):
		self.parent = user
		self.level = 0
		self.xp = 0
		self.lastMinuteChatted = 0
		# this is used so the object can refer to the user that has this object

	@staticmethod
	# gets the total amount of XP required to level up from level n-1 to level n
	def getXpToLevelUpTo(level):
		return 100 + 20*(level-1)
		# we can change this later

	@staticmethod
	# gets the current time in minutes
	def currentTimeMinutes():
		return int(time.time() * 60)

	def onChat(self):
		if currentTimeMinutes() > self.lastMinuteChatted:
		self.xp += random.randint(7,12)

	def checkForLevelUp(self): # checks for level up, should be called on message sent
		while self.xp >= getXpToLevelUpTo(self.level + 1):
		self.xp -= getXpToLevelUpTo(self.level + 1)
		self.level += 1
		# send level up message
