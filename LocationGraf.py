import Location
import heapq


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
        if type(other) = Point and other.x = self.x and other.y = self.y:
            return 1
        else:
            return 0
        


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
        came_from = self.a_star_search(point_start, point_end)
        way = []
        point = came_from[point_end]
        while point != point_start:
            way.append(point)
            point = came_from[point]
        return way    


    def heuristic(first, second):
        return abs(first.x - second.x) + abs(first.y - second.y)

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in current.neighbors:
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from



