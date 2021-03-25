import RunState

class RunConfig:
    def __init__(self, name, description ):
        self.name = name
        self.description = description
        pass

    def getName(self):
        return self.name
      
    def setName(self, x):
        self.name = x

    def getDescr(self):
        return self.description
      
    def setDescr(self, y):
        self.description = y

    def getState(self):
        pass

    def getTarget(self):
        pass
        
    def getscanConfig(self):
        pass
