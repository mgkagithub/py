class Shape: area = lambda self: None
class Rectangle(Shape): 
    def __init__(self, w, h): assert w > 0 and h > 0; self.w, self.h = w, h
    area = lambda self: self.w * self.h
class Circle(Shape): 
    def __init__(self, r): assert r > 0; self.r = r
    area = lambda self: 3.14159 * self.r ** 2
rectangle ,circle= Rectangle(10, 10),Circle(1)
print("Rectangle area:", rectangle.area(),"\nCircle area:", circle.area())
