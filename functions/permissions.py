import discord, json


class Perms:

    def __init__(self, parent):
        self.parent = parent
        self.role_path = "conf/roles.json"
        self.adminable = 0  # set this to 1 and
        self.adminCode = 0  # this to "random.randint(100000, 999999)" and
        self.codePermLevel = 0  # this to whatever level you want to get and
        self.failed = False
        try:
            self.roles = self.__load_json(self.role_path)
        except KeyError:
            self.prepare = {}
            self.__prepare_json(self.role_path)
            self.roles = self.__load_json(self.role_path)

    @staticmethod
    def __load_json(path):
        file = open(path, "r")
        val = json.load(file)
        file.close()
        return val

    def __prepare_json(self, path):
        file = open(path, "w")
        file.write(json.dumps(self.prepare))
        file.close()

    @staticmethod
    def __update_json(path, val):
        file = open(path, "w")
        file.write(json.dumps(val))
        file.close()

    async def is_permitted(self, msg: discord.Message, bot: discord.Client):
        self.failed = True
        user = msg.author
        cmd = msg.content.split()[0].replace("$", "")
        if self.get_user_perm(user, cmd):
            self.failed = False
            return True
        else:
            await bot.send_message(msg.channel, "{}, you have no right to use ${}".format(user.mention, cmd))
            return False

    async def is_role_prior(self, role1, role2):
        if self.roles[role1]['permlvl'] > self.roles[role2]['permlvl']:
            return True
        else:
            return False

    def get_user_perm(self, user, cmd) -> bool:
        try:
            return bool(self.roles[self.parent.get_role(user)][cmd])
        except KeyError:
            return False

    def get_role_perm(self, role, cmd):
        try:
            return bool(self.roles[role][cmd])
        except KeyError:
            return False

    def set_role_perm(self, role, cmd, value):
        try:
            self.roles[role][cmd] = value
        except KeyError:
            return

    def get_failed(self):
        return self.failed

    def set_failed(self, b: bool):
        self.failed = b
