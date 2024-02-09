import math
class Point:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
    def show(self):
        return (self.start_x, self.start_y)
    def move(self):
        self.end_x = int(input())
        self.end_y = int(input())
    def distance(self):
        return math.sqrt((self.end_x - self.start_x)**2+(self.end_y - self.start_y)**2)
start_x = int(input())
start_y = int(input())
point1 = Point(start_x, start_y)
point1.move()
print(point1.distance())