import Wall
import Floor

class Location:
    def __init__(self, size_x, size_y, locality_object, other_object):
        self.size = (size_x, size_y)
        self.field = [[[None, None] for i in range(self.size[1])] for i in range(self.size[0])]
        for obj in locality_object:
            self.add_locality_object(obj)
        for obj in other_object:
            self.add_other_object(obj)    

    def add_locality_object(self, obj):
        self.field[obj.x][obj.y][0] = obj

    def add_other_object(self, obj):
        self.field[obj.x][obj.y][1] = obj

    def get_location(self, coordinates):
        return self.field[coordinates[0]][coordinates[1]])

    def del_locality_object(self, obj):
        self.field[obj.x][obj.y][0] = None

    def del_other_object(self, obj):
        self.field[obj.x][obj.y][1] = None

    def get_distance(self, obj_1, obj_2):
        return ((obj_1.x - obj_2.x) ** 2 + (obj_1.y - obj_2.y) ** 2) ** 0.5

    def get_type_location(self, coordinates):
        return type(self.field[coordinates[0]][coordinates[1]][0])
