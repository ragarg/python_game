import Object


class Hero(Object.Object):
    def __init__(self, x, y, image):
        Object.Object.__init__(self, x, y, image)
        self.way = []
        
    def customization(self, image):
        self.image  =  image

