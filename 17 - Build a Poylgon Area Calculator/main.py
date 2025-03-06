class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'{__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        rec_width = self.width // shape.width
        rec_height = self.height // shape.height
        return rec_width * rec_height



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 
        self.side = side

    def __repr__(self):
        return f'{__class__.__name__}(side={self.side})'

    def get_area(self):
        area = self.side * self.side
        return area

    def get_perimeter(self):
        perimeter = 2 * self.side + 2 * self.side
        return perimeter

    def get_diagonal(self):
        diagonal = (self.side ** 2 + self.side ** 2) ** 0.5
        return diagonal

    def set_side(self, side):
        self.side = side

    def set_width(self, side):
        self.side = side
    
    def set_height(self, side):
        self.side = side

    def get_picture(self):
        if self.side > 50:
            return 'Too big for picture.'
        picture = ""
        for _ in range(self.side):
            picture += "*" * self.side + "\n"
        return picture

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))