class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def add_new_neighbors(self, point):
        self.neighbors.append(point)

class LocationGraf:
    def __init__(self, field):
        self.graf = [[None for i in range(field.size[1])] for i in range(field.size[0])]
        for x in range(field.size[0]):
            for y in range(1, field.size[1] + 1):
                self.graf[x][y] = Point(x, y)
        for x in range(field.size[0]):
            for y in range(1, field.size[1] + 1):

                if x != 0: 
                    if field.field[x - 1][y][0].patency():
                        self.graf[x][y].add_new_neighbors(self.graf[x - 1][y])
                    if y != 0: 
                        if field.field[x - 1][y - 1][0].patency():
                            self.graf[x][y].add_new_neighbors(self.graf[x - 1][y - 1])
                    if y != field.size[1] - 1: 
                        if field.field[x - 1][y + 1][0].patency():
                            self.graf[x][y].add_new_neighbors(self.graf[x - 1][y + 1])

                if x != field.size[0] - 1:
                    if field.field[x + 1][y][0].patency():
                        self.graf[x][y].add_new_neighbors(self.graf[x + 1][y])
                    if y != 0: 
                        if field.field[x + 1][y - 1][0].patency():
                            self.graf[x][y].add_new_neighbors(self.graf[x + 1][y - 1])
                    if y != field.size[1] - 1: 
                        if field.field[x + 1][y + 1][0].patency():
                            self.graf[x][y].add_new_neighbors(self.graf[x + 1][y + 1])

    def way(self, point_start, point_end):
        pass
