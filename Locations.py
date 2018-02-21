import Location
from Objects import *
from Floor import *
from Wall import *
from Warp import  Warp

a = []
for i in range(100):
    for j in range(100):
        a.append(Floor(i, j, grass_image))
for i in range(10, 14):
    for j in range(10, 14):
        a.append(Wall(i, j, dirt_image))

b = []
grass_image, dirt_image = dirt_image, grass_image
for i in range(100):
    for j in range(100):
        b.append(Floor(i, j, grass_image))
for i in range(10, 14):
    for j in range(10, 14):
        b.append(Wall(i, j, dirt_image))
a.append(Warp(0, 15, warp_image, [2, [20, 15]]))
b.append(Warp(21, 15, warp_image, [1, [1, 15]]))
start_warp = Warp(0, 0, warp_image, [1, [Hero.x, Hero.y]])


location_sample = Location.Location(100, 100, a, mobs)
location = Location.Location(100, 100, b, mobs)
start_location = Location.Location(1, 1, [start_warp], [])
locations = [start_location, location_sample, location]
