from Locations import *

class Location:
    def __init__(self, size_x, size_y, objects):
        self.size = (size_x, size_y)
        self.field = [[None for i in range(self.size[1])] for i in range(self.size[0])]
        for obj in objects:
            self.field[obj.x][obj.y] = obj
        
    def add_object(self, obj):
        self.field[obj.x][obj.y] = obj
    
    def get_location(self, x, y):
        return self.field[x][y]

    def del_object(self, obj):
        self.field[obj.x][obj.y] = None
        
    def get_distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5