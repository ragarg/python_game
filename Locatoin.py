class Location:
    def __init__(self, configs):
        self.im = configs['image']
        self.size = configs['size']
        self.objects = configs['objects']
        self.field = [[None for i in range(self.size[1])] for i in range(self.size[0])]
        for obj in objects:
            field[obj.x][obj.y] = obj
        
    def add_object(self, obj):
        self.field[obj.x][obj.y] = obj
    
    def get_location(self, x, y):
        return self.field[x][y]
