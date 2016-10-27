import json

class Level():
    def __init__(self):
        self.path = "functions/conf/levels.json"
        try:
            self.__load_json()
        except Exception:
            self.prepare = {0:{"xp":0,"lvl":0}}
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

    def test_json(self, user):
        print(user.id)
        self.users[user.id]['xp'] = 10
        self.__update_json()

    def add_xp(self, user, amount):
        self.users[user.id]['xp'] += amount

    def remove_xp(self, user, amount):
        self.user[user.id]['xp'] -= amount

    def levelup(self, user):
        self.users[user.id]['lvl'] += 1

    def get_current_xp(self, user):
        return self.users[user.id]['xp']

    def get_current_level(self, user):
        return self.users[user.id]['lvl']

    def set_current_xp(self, user, amount):
        self.users[user.id]['xp'] = amount

    def set_current_level(self, user, amount):
        self.users[user.id]['lvl'] = amount