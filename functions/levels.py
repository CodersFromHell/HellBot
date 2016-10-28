import json, random

class Level:
    def __init__(self):
        self.path = "functions/conf/levels.json"
        self.cooldown = 5
        self.timestamps = {}
        self.adminable = 0  #set this to 1 and
        self.adminCode = 0  #this to "random.randint(100000, 999999)" and
        self.codePermLevel = 0 #this to whatever level you want to get and
        #print(adminCode)   #uncomment this to generate an admin code
        try:
            self.__load_json(self.path)
        except Exception:
            self.prepare = {}
            self.__prepare_json(self.path)
            self.__load_json(self.path)

    def __load_json(self, path):
        file = open(path, "r")
        self.users = json.load(file)
        file.close()

    def __prepare_json(self, path):
        file = open(path, "w+")
        file.write(json.dumps(self.prepare))
        file.close()

    def __update_json(self, path):
        file = open(path, "w+")
        file.write(json.dumps(self.users))
        file.close()

    async def on_message(self, bot, msg):
        user = msg.author
        args = msg.content.split()
        try:
            self.users[user.id]
        except Exception:
            self.users[user.id] = {"xp":0, "lvl":1, "perm":0}
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
        elif args[0] == "$givexp" and self.users[user.id]["perm"] >= 10:
            try:
                if args[2] == msg.mentions[0].mention:
                    user = msg.mentions[0]
                else:
                    user = msg.author
            except:
                user = msg.author
            try:
                self.add_xp(user, int(args[1])+0)
                await bot.send_message(msg.channel, "{} received {}xp".format(user.mention, args[1]))
            except:
                bot.send_message(msg.channel, "Invaild syntax")
                return
        elif args[0] == "$removexp" and self.users[user.id]["perm"] >= 10:
            try:
                if args[2] == msg.mentions[0].mention:
                    user = msg.mentions[0]
                else:
                    user = msg.author
            except:
                user = msg.author
            try:
                self.remove_xp(user, int(args[1])+0)
                await bot.send_message(msg.channel, "{} got {}xp taken from him".format(user.mention, args[1]))
            except:
                bot.send_message(msg.channel, "Invaild syntax")
                return
        elif args[0] == "$setlvl" and self.users[user.id]["perm"] >= 10:
            try:
                if args[2] == msg.mentions[0].mention:
                    user = msg.mentions[0]
                else:
                    user = msg.author
            except:
                user = msg.author
            try:
                self.set_lvl(user, int(args[1])+0)
                await bot.send_message(msg.channel, "{}s level was set to {}".format(user.mention, args[1]))
            except:
                bot.send_message(msg.channel, "Invaild syntax")
                return
        elif args[0] == "$setperm" and self.users[user.id]["perm"] >= int(args[1]):
            if args[2] == msg.mentions[0].mention and self.users[msg.mentions[0].id]["perm"] <= self.users[user.id]["perm"]:
                self.set_perm(msg.mentions[0], int(args[1]))
                await bot.send_message(msg.channel, "{}s perm level was set to {} by ".format(msg.mentions[0].mention, args[1], user.mention))
            else:
                return
        elif args[0] == "$gencode" and self.users[user.id]["perm"] >= int(args[1]):
            self.adminable = 1
            self.codePermLevel = int(args[1])+0
            self.adminCode = random.randint(100000, 999999)
            print(self.adminCode)
        elif args[0] == "$" + str(self.adminCode) and self.adminable == 1:
            await bot.send_message(msg.channel, "{} is now has a perm level of {}".format(user.mention, self.codePermLevel))
            self.adminable = 0
            self.users[user.id]["perm"] = self.codePermLevel
            self.codePermLevel = 0
            self.adminCode = 0
        elif (msg.timestamp - self.timestamps[user.id]).total_seconds() > self.cooldown:
            self.add_xp(user, random.randint(2, 5))
            self.timestamps[user.id] = msg.timestamp

        while self.users[user.id]["xp"] > self.xp_for_levelup(user):
            await self.levelup(user, bot, msg)
        self.__update_json(self.path)

    async def send_xp(self, bot, msg, args):
        try:
            if args[1] == msg.mentions[0].mention:
                user = msg.mentions[0]
            else:
                return
        except:
            user = msg.author
        await bot.send_message(msg.channel, "{} has {}xp of {}xp".format(user.mention, self.users[user.id]["xp"], self.xp_for_levelup(user)))

    async def send_level(self, bot, msg, args):
        try:
            if args[1] == msg.mentions[0].mention:
                user = msg.mentions[0]
            else:
                return
        except:
            user = msg.author
        await bot.send_message(msg.channel, "{} is level {}".format(user.mention, self.users[user.id]["lvl"]))

    async def send_timestamp(self, bot, msg, args):
        await bot.send_message(msg.channel, "{} needs to wait for {}".format(msg.author.mention, (self.cooldown - (msg.timestamp - self.timestamps[msg.author.id]).total_seconds())))

    def xp_for_levelup(self, user):
        return 50 + 5 * (self.users[user.id]['lvl'] - 1)

    def add_xp(self, user, amount):
        self.users[user.id]['xp'] += amount

    def remove_xp(self, user, amount):
        self.users[user.id]['xp'] -= amount

    def add_lvl(self, user, amount):
        self.users[user.id]['lvl'] += amount

    def remove_lvl(self, user, amount):
        self.users[user.id]['lvl'] -= amount

    async def levelup(self, user, bot, msg):
        print(user.name + " leveled to: " + str(self.users[user.id]['lvl']+1) + " with xp: " + str(self.users[user.id]['xp']) + " of " + str(self.xp_for_levelup(user)))
        await bot.send_message(msg.channel, "{} just leveled up to level {}".format(user.mention, self.users[user.id]["lvl"]))
        self.remove_xp(user, self.xp_for_levelup(user))
        self.users[user.id]['lvl'] += 1

    def get_xp(self, user):
        return self.users[user.id]['xp']

    def get_lvl(self, user):
        return self.users[user.id]['lvl']

    def get_perm(self, user):
        return self.users[user.id]['perm']

    def set_xp(self, user, amount):
        self.users[user.id]['xp'] = amount

    def set_lvl(self, user, amount):
        self.users[user.id]['lvl'] = amount

    def set_perm(self, user, amount):
        self.users[user.id]['perm'] = amount