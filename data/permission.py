import json

class Permission:
    def __init__(self, file, default_level=0):
        self.pjson = json.load(open(file, "r", encoding="utf-8"))
        self.default_level = default_level
        self.file = file
    def setperm(self, user, level):
        self.pjson[user.id] = [user.name, level]
        file = open(self.file, "w", encoding="utf-8")
        file.close()
    def readperm(self, user):
        if user.id not in self.pjson: return self.default_level
        return self.pjson[user.id][1]
    def getperm(self):
        return self.pjson
    def delperm(self, user):
        del self.pjson[user.id]
        file = open(self.file, "w", encoding="utf-8")
        file.close()
    def testperm(self, user, level):
        if self.pjson[user.id][1] >= level: return True
        return False