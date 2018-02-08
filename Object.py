import pygame

class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = None
        self.image_rect = None
        self.roomID = 0
        
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.move(x, y)
        self.roomID = 0

    def SetImage(self, image):
        self.image = image

    def SetCoordinates(self, x , y):
        self.x = x
        self.y = y

    def SetRoomID(self, roomnumber):
        roomID = roomnumber

    def GetImage(self,):
        return self.image

    def GetCoordinates(self):
        return self.y, self.x

    def GetRoomID(self):
        return self.roomID