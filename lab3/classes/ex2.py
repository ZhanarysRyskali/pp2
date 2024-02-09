#ex 2
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self):
        self.length = int(input())

    def area(self):
        return self.length**2
side = Square()
print(side.area())

