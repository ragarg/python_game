from Locations import *

class Core:
    def __init__(self):
        self.locations = [location_sample]
        self.current_location = 0
        self.loc = self.locations[self.current_location]
        
    def move_object(self, obj, x, y):
        if self.loc.field[x][y] == None:
            if self.loc.get_distance(obj.x, obj.y, x, y) <= obj.speed:
                self.loc.del_object(obj)
                obj.x = x
                obj.y = y
                self.loc.add_object(obj)
            else:
                self.loc.del_object(obj)
                obj.x = (obj.speed**2/(x**2/y**2) + 1)**0.5
                obj.y = (obj.speed**2/(y**2/x**2) + 1)**0.5
                self.loc.add_object(obj)
                
    
