class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a 2 dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A polygon has 3 sides")


class Quad(Polygon):
    def display_info(self):
        print("A quadrilateral has 4 sides")

t1= Triangle([5,6,7])
perimeter= t1.get_perimeter()
t1.display_info()
print("The perimeter is", perimeter)