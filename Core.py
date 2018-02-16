from Locations import *
from Wall import Wall
from Objects import Hero

class Core:
    def __init__(self):
        self.locations = [location_sample]
        self.current_location = 0
        self.loc = self.locations[self.current_location]
        self.Hero = Hero
        self.ai_list = []

    def update_field(self):
        self.move_hero()

    def move_object(self, obj, x, y):
        self.loc.del_other_object(obj)
        obj.x = x
        obj.y = y
        self.loc.add_other_object(obj)

    def update_way(self, goal):
        if type(self.loc.field[goal[0]  // 24][goal[1]  // 24][0]) != Wall:
            Hero.way = self.loc.graph.way(self.loc.graph.graph[Hero.x][Hero.y], self.loc.graph.graph[goal[0] // 24][goal[1] //24])

    def move_hero(self):
        if Hero.way == []:
            Hero.way.append(self.loc.graph.graph[Hero.x][Hero.y])

        point = Hero.way.pop()
        
        #if self.loc.field[point.x][point.y][1] != None:
            #self.update_way(self, (Hero.way[0].x, Hero.way[0].y)) Тут должен быть перерасчет пути в колизии, но он пока падает
            #self.move_hero(self)
            #return
        self.move_object(Hero, point.x, point.y)


    
