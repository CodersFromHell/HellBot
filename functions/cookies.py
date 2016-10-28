import discord
import json


class Cookie:

    """
    Error Codes
    These are Enums for different Error Codes (It doesn't return True/False! It returns an Error Code)
    ERR - An different error occurred while trying to finish the process. The number is -1
    SUCCESS - Everything is fine! The number is 0
    NO_COOKIES - The User has no Cookies! He need more COOKIES! The number is 1
    NO_USER - The User was not found in the Cookie DB! (cookies.json) The number is 2
    KILL_YOURSELF - Don't use it! Just don't use it!
    """

    ERR = -1
    SUCCESS = 0
    NO_COOKIES = 1
    NO_USER = 2
    KILL_YOURSELF = "Kill Yourself!"

    def __load_json(self):
        file = open(self.path, "r")
        self.cfg = json.load(file)
        file.close()
        return True

    def __update_json(self):
        file = open(self.path, "w+")
        file.write(json.dumps(self.cfg))
        file.close()
        return self.__load_json()

    def _start_cookies(self, user):
        self.cfg[user.id] = self.startValue
        return self.__update_json()

    def __init__(self, bot):
        self.bot = bot
        self.path = "conf/cookies.json"
        self.__load_json()
        self.startValue = 10

    def get_cookies(self, user):
        try:
            if self.cfg[user.id] == -1:
                return 999999
            return self.cfg[user.id]
        except KeyError:
            self._start_cookies(user)
            return self.cfg[user.id]

    def rem_cookies(self, user, amout=1):
        self.get_cookies(user)
        if self.cfg[user.id] == -1:
            return self.SUCCESS
        if self.get_cookies(user) >= amout:
            self.cfg[user.id] -= amout
            if self.__update_json():
                return self.SUCCESS
            else:
                return self.ERR
        else:
            return self.NO_COOKIES

    def add_cookies(self, user, amout=1):
        self.get_cookies(user)
        if self.cfg[user.id] == -1:
            return self.SUCCESS
        self.cfg[user.id] += amout
        if self.__update_json():
            return self.SUCCESS
        else:
            return self.ERR

    def give_cookies(self, user, to, amout=1):
        if self.get_cookies(user) >= amout:
            self.rem_cookies(user, amout)
            self.add_cookies(to, amout)
            if self.__update_json():
                return self.SUCCESS
            else:
                return self.ERR
        else:
            return self.NO_COOKIES

    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        args = msg.content.split()
        print("[{}:{}] ({}) {}>>> {}".format(msg.timestamp, msg.server.name, msg.channel.name, msg.author.name,
                                             msg.content))
        if args[0] == "$cookies":
            await self.bot.send_message(msg.channel, "{} you have {} :cookie:".format(msg.author.mention,
                                                                                      self.get_cookies(msg.author)))
            return

        if args[0] == "$give":
            if len(args) < 2:
                await self.bot.send_message(msg.channel,
                                            "{} you didn't mention a user! `$give (User) [Amout, default 1]`".format(
                                                msg.author.mention))
                return
            if len(args) >= 2:
                to = msg.mentions[0]
                amout = 1
                try:
                    amout = int(args[2])
                except IndexError:
                    pass
                if to == self.bot.user:
                    await self.bot.send_message(msg.channel,
                                                "{} i'm not allowed to take Cookies! http://ripme.xyz/HellBot".format(
                                                    msg.author.mention))
                    return
                if isinstance(to, discord.Member):
                    if self.give_cookies(msg.author, to, amout) == self.SUCCESS:
                        await self.bot.send_message(msg.channel,
                                                    "{} gives you {} cookies! {}".format(msg.author.mention, amout,
                                                                                        to.mention))
                    else:
                        await self.bot.send_message(msg.channel,
                                                    "{} Whoops! You don't have enough cookies!".format(
                                                        msg.user.mention))
                    return
                else:
                    await self.bot.send_message(msg.channel, "{} the user wasn't found!".format(msg.author.mention))
                    return

        for emoji in msg.content.lower().split(" "):
            if emoji == "cookie" or emoji == "🍪":
                if self.rem_cookies(msg.author) == self.NO_COOKIES:
                    await self.bot.delete_message(msg)
                    return
                print("Removed a Cookie from {}".format(msg.author))

