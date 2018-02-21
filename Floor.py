import Object

class Floor(Object.Object):
    def __init__(self, x, y, image):
        Object.Object.__init__(self, x, y, image)
        self.size = (24, 24)
        self.patency = 1

    def GetSize(self):
        return self.size


