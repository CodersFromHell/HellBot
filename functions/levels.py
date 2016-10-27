import json, random

class Level:
    def __init__(self):
        self.path = "functions/conf/levels.json"
        self.cooldown = 5
        self.timestamps = {}
        try:
            self.__load_json()
        except Exception:
            self.prepare = {}
            self.__prepare_json()
            self.__load_json()

    def __load_json(self):
        file = open(self.path, "r")
        self.users = json.load(file)
        file.close()

    def __prepare_json(self):
        file = open(self.path, "w+")
        file.write(json.dumps(self.prepare))
        file.close()

    def __update_json(self):
        file = open(self.path, "w+")
        file.write(json.dumps(self.users))
        file.close()

    async def on_message(self, bot, msg):
        user = msg.author
        args = msg.content.split()
        try:
            self.users[user.id]
        except Exception:
            self.users[user.id] = {"xp":0, "lvl":1}
        try:
            self.timestamps[user.id]
        except:
            self.timestamps[user.id] = msg.timestamp

        if args[0] == "$lvl":
            await self.send_level(bot, msg, args)
            return
        elif args[0] == "$xp":
            await self.send_xp(bot, msg, args)
            return
        elif args[0] == "$cooldown":
            await self.send_timestamp(bot, msg, args)
            return
        elif (msg.timestamp - self.timestamps[user.id]).total_seconds() > self.cooldown:
            self.add_xp(user, random.randint(2, 5))
            self.timestamps[user.id] = msg.timestamp

        while self.users[user.id]["xp"] > self.xp_for_levelup(self.users[user.id]["lvl"]):
            self.levelup(user)
            bot.send_message(msg.channel, "{} just leveled up to level {}".format(user.mention, self.users[user.id]["lvl"]))
        self.__update_json()

    async def send_xp(self, bot, msg, args):
        await bot.send_message(msg.channel, "{} has {} xp".format(msg.author.mention, self.users[msg.author.id]["xp"]))

    async def send_level(self, bot, msg, args):
        await bot.send_message(msg.channel, "{} is level {}".format(msg.author.mention, self.users[msg.author.id]["lvl"]))

    async def send_timestamp(self, bot, msg, args):
        await bot.send_message(msg.channel, "{} needs to wait for {}".format(msg.author.mention, (msg.timestamp - self.timestamps[msg.author.id]).total_seconds()))

    def xp_for_levelup(self, lvl):
        return 50 + 5 * (lvl - 1)

    def add_xp(self, user, amount):
        self.users[user.id]['xp'] += amount

    def remove_xp(self, user, amount):
        self.users[user.id]['xp'] -= amount

    def levelup(self, user):
        self.users[user.id]['lvl'] += 1
        self.remove_xp(user, self.xp_for_levelup(self.users[user.id]['lvl']))

    def get_current_xp(self, user):
        return self.users[user.id]['xp']

    def get_current_level(self, user):
        return self.users[user.id]['lvl']

    def set_current_xp(self, user, amount):
        self.users[user.id]['xp'] = amount

    def set_current_level(self, user, amount):
        self.users[user.id]['lvl'] = amount