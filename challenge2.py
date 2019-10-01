class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4
    
    def change_size(self, new_size):
        self.side += new_size
        

a_square = Square(12)
a_square.change_size(12)
print(a_square.side)