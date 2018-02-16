import Location
from Objects import *
from Floor import *
from Wall import *

a = []
grass_image = pygame.image.load("arts/grass.png")
dirt_image = pygame.image.load("arts/dirt.png")
for i in range(100):
    for j in range(100):
        a.append(Floor(i, j, grass_image))
for i in range(10, 14):
    for j in range(10, 14):
        a.append(Wall(i, j, dirt_image))
        
location_sample = Location.Location(100, 100, a, [Hero, Dog1, Dog2])
