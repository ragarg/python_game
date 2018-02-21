from Object import Object

class Warp(Object):
    def __init__(self, x, y, image, link):
        Object.__init__(self, x, y, image)
        self.link = link
        self.patency = 1