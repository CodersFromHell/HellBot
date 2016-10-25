import discord
import levels, cookies

class CustomUser():
    customUsers = {} # maps discord.Member back to CustomMember
    def __init__(self,member : discord.Member):
        self.member = member
        self.cookies = Cookie(self)
        self.level = Level(self)
        self.mute = Mute(self)
        customUsers[self.member] = self
