import Location
import heapq
from Floor import Floor


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def add_new_neighbors(self, point):
        self.neighbors.append(point)

    def __eq__(self, other):
        if type(other) == Point and other.x == self.x and other.y == self.y:
            return 1
        else:
            return 0

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

class LocationGraf:
    def __init__(self, field):
        self.graf = [[None for i in range(field.size[1])] for i in range(field.size[0])]
        for x in range(field.size[0]):
            for y in range(field.size[1]):
                self.graf[x][y] = Point(x, y)
        for x in range(field.size[0]):
            for y in range(field.size[1]):

                if x != 0:
                    if type(field.field[x - 1][y][0]) == Floor:
                        self.graf[x][y].add_new_neighbors(self.graf[x - 1][y])
                    if y != 0:
                        if type(field.field[x - 1][y - 1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x - 1][y - 1])
                    if  type(field.field[x][y - 1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x][y - 1])
                    if y != field.size[1] - 1:
                        if type(field.field[x - 1][y + 1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x - 1][y + 1])
                        if type(field.field[x][y + 1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x][y + 1])
                if x != field.size[0] - 1:
                    if type(field.field[x + 1][y][0]) == Floor:
                        self.graf[x][y].add_new_neighbors(self.graf[x + 1][y])
                    if y != 0:
                        if type(field.field[x + 1][y -1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x + 1][y - 1])
                    if y != field.size[1] - 1:
                        if type(field.field[x + 1][y + 1][0]) == Floor:
                            self.graf[x][y].add_new_neighbors(self.graf[x + 1][y + 1])

    def cost(self, first, second):
        if second in first.neighbors:
            if (second.x % 2 - first.x) == (second.y - first.y) % 2:
                return 2**0.5
            else:
                return 1

    def way(self, point_start, point_end):
        came_from = self.a_star_search(point_start, point_end)
        way = []
        point = point_end
        while point != point_start:
            way.append(point)
            point = came_from[(point.x, point.y)]
        return way    


    def heuristic(self, first, second):
        return abs(first.x - second.x) + abs(first.y - second.y)

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[(start.x, start.y)] = None
        cost_so_far[(start.x, start.y)] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break

            for next in current.neighbors:
                new_cost = cost_so_far[(current.x, current.y)] + self.cost(current, next)
                if (next.x, next.y) not in cost_so_far or new_cost < cost_so_far[(next.x, next.y)]:
                    cost_so_far[(next.x, next.y)] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[(next.x, next.y)] = current

        return came_from
