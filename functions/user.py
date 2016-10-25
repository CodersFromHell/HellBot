import discord
import levels, cookies

class CustomUser():
    @staticmethod
    def cUserFrom(server : discord.Server, member : discord.Member):
        # looks up member from database
        pass
    def __init__(self,member : discord.Member):
        self.member = member
        self.cookies = Cookie(self)
        self.level = Level(self)
        self.mute = Mute(self)
        customUsers[self.member] = self
