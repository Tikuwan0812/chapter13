class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size

a_rectangle = Rectangle(12, 20)
a_square = Square(24)
a_rectangle.what_am_i()
a_square.what_am_i()