class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    
class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4

a_rectangle = Rectangle(12, 20)
a_square = Square(24)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())