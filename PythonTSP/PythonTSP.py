import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, city):
        xDistance = math.fabs(self.x - city.x)
        yDistance = math.fabs(self.y - city.y)
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance

    def toString(self):
        return str(self.x) + ", " + str(self.y)

city = City(100,25)
city2 = City(200,40)
print(city.distanceTo(city2))