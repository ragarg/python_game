import DinamicObject
from Base import LEUB

class Hero:
    def __init__(self, x, y, image, ObjectAtrtibutes):
        DinamicObject.DinamicObject.__init__(1, x, y, image, ObjectAtrtibutes)
        self.EXP = 0
        
    def customization(self, image):
        self.image  =  image

    def UPEXP(self):
        if self.EXP == LEUB[self.LVL]:
            self.EXP = 0
            self.LVL += 1
            self.LevelUP()