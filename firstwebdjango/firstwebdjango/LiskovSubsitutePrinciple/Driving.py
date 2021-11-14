from firstwebdjango.LiskovSubsitutePrinciple.Rectangle import Rectangle
from firstwebdjango.LiskovSubsitutePrinciple.Square import Square


class Driving:
    def GetArea(self, areaToFindObj):
        return (areaToFindObj.area())


d = Driving()

rectangle = Rectangle(2, 3)
print("area of rectangle", d.GetArea(rectangle))

square = Square(2)
print("area of square",  d.GetArea(square))

rectangle = square
# # square = rectangle # not a valid statement, cannot assign base class object to derived class in other languages
print("area of rectangle", d.GetArea(rectangle))


