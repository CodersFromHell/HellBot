import discord
import user

class Level()
	def __init__(self, user : CustomUser):
		self.parent = user
		self.level = 0
		self.xp = 0
		# this is used so the object can refer to the user that has this object

	@staticmethod
	# gets the total amount of XP required to level up from level n-1 to level n
	def getXpToLevelUpTo(level):
		return 100 + 20*(level-1)
		# we can change this later

	def checkForLevelUp(): # checks for level up, should be called on message sent
		pass
