import json

class Permission:
    def __init__(self, file, default_level=0):
        self.pjson = json.load(open(file, "r", encoding="utf-8"))
        self.default_level = default_level
        self.file = file
    def setperm(self, user, level):
        self.pjson[user.id] = {"name":user.name, "lvl":level}
        self.updateFile()
    def readperm(self, user):
        if user.id not in self.pjson: return self.default_level
        return self.pjson[user.id]["lvl"]
    def getpjson(self):
        return self.pjson
    def delperm(self, user):
        del self.pjson[user.id]
        self.updateFile()
    def testperm(self, user, level):
        if self.pjson[user.id]["lvl"] >= level: return True
        return False
    def updateFile(self):
        file = open(self.file, "w", encoding="utf-8")
        file.write(self.pjson)
        file.close()
    def get_name(self, user):
        return self.pjson[user.id]["name"]