import uuid

class User:

    def __init__(self, name):
      self.id = str(uuid.uuid1())
      self.name = name

    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def setName(self,name):
        self.name = name