class Object:
    def __init__(self, x, y, image):
        self.SetCoordinates(x, y)
        self.SetImage(image)
        self.roomID = 0

    def SetImage(self, image):
        self.image = image

    def SetCoordinates(self, x , y):
        self.x = x
        self.y = y

    def SetRoomID(self, roomnumber):
        roomID = roomnumber

    def GetImage(self):
        return self.image

    def GetCoordinates(self):
        return self.y, self.x

    def GetRoomID(self):
        return self.roomID
