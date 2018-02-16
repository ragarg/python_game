import Object


class Poor_dog(Object.Object):
    def __init__(self, x, y, image):
        Object.Object.__init__(self, x, y, image)
        self.way = []
        self.move_cooldown = 20
        self.move_actual_cooldown = 0
        
    def customization(self, image):
        self.image  =  image
        
    #def make_a_move(self, location):
        #if location.get_distance(self, Hero)

