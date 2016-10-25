import discord
import levels, cookies

class CustomUser():
	def __init__(self,member : discord.Member):
		self.member = member
		self.cookies = Cookie(self)
		self.level = Level(self)
		self.mute = Mute(self)