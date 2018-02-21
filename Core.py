from Locations import *
from Wall import Wall
from Objects import Hero, mobs

class Core:
    def __init__(self):
        Hero.x = 0
        Hero.y = 0

        self.loc = locations[0]
        self.ai_list = []

    def update_field(self):
        if type(self.loc.field[Hero.x][Hero.y][0]) == Warp:

            self.update_location(self.loc.field[Hero.x][Hero.y][0].link)
            self.move_object(Hero, Hero.x, Hero.y)

            cells = self.loc.field


        else:

            cells = []
            if Hero.way == []:
                cells.append(self.loc.field[Hero.x][Hero.y])
            else:
                cells.append([self.loc.field[Hero.x][Hero.y][0], None])
                self.move_hero()
                cells.append(self.loc.field[Hero.x][Hero.y])
            for mob in mobs:
                cells.append([self.loc.field[mob.x][mob.y][0], None])
                if mob.way == []:
                    cells.append(self.loc.field[mob.x][mob.y])
            #self.move_mob(mob)
            #cells.append(self.loc.field[mob.x][mob.y])
            cells = [cells]
        return cells

    def update_location(self, link):
        self.loc.field[Hero.x][Hero.y][1] = None
        self.loc = locations[link[0]]
        Hero.x = link[1][0]
        Hero.y = link[1][1]

    def move_object(self, obj, x, y):
        self.loc.del_other_object(obj)
        obj.x = x
        obj.y = y
        self.loc.add_other_object(obj)

    def update_way(self, goal):
        if type(self.loc.field[goal[0]  // 24][goal[1]  // 24][0]) != Wall:
            Hero.way = self.loc.graph.way(self.loc.graph.graph[Hero.x][Hero.y], self.loc.graph.graph[goal[0] // 24][goal[1] //24])

    def move_hero(self):
        point = Hero.way.pop()
        
        #if self.loc.field[point.x][point.y][1] != None:
            #self.update_way(self, (Hero.way[0].x, Hero.way[0].y)) 
            #self.move_hero(self)
            #return
        self.move_object(Hero, point.x, point.y)

    
