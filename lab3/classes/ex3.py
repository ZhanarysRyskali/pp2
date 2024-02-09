#ex 2
class Shape:
    def area(self):
        self.a = 0
        print(self.a)
class Square(Shape):
    def __init__(self):
        self.length = int(input())

    def area(self):
        return self.length**2
class Rectangle(Shape):
    def __init__(self):
        self.length = int(input())
        self.width = int(input())
    def area(self):
        return self.width * self.length
# side = Square(length)
side2 = Rectangle()
print(side2.area())

