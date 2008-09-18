
import math
class Triangle(object):

    def __init__(self, points):
        self.points = points
        self.sideLengths = self.__calculateLengths()
        self.area = self.__calculateArea()
        self.obtuseCosValue = self.__calculateAngles()

    def __calculateLengths(self):
        x1 = self.points[0]
        y1 = self.points[1]
        x2 = self.points[2]
        y2 = self.points[3]
        x3 = self.points[4]
        y3 = self.points[5]
        l1 = math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))
        l2 = math.sqrt(pow((x1-x3), 2)+pow((y1-y3), 2))
        l3 = math.sqrt(pow((x2-x3), 2)+pow((y2-y3), 2))
        return [l1, l2, l3]
    
    def __calculateArea(self):
        s = (self.sideLengths[0]+self.sideLengths[1]+self.sideLengths[2])/2
        area = math.sqrt(s*(s-self.sideLengths[0])*(s-self.sideLengths[1])*(s-self.sideLengths[2]))
        return area

    def getArea(self):
        return self.area

    def isTriangle(self):
        if self.area > 0:
            return True
        return False

    def triangleCategoryByLength(self):
        if (self.sideLengths[0] == self.sideLengths[1] or \
            self.sideLengths[0] == self.sideLengths[2] or \
            self.sideLengths[1] == self.sideLengths[2]):
            return "isosceles"

        else:
            return "scalene"
    
    def __calculateAngles(self):
        if self.area > 0:
            self.sideLengths.sort()
            cosValue = (pow(self.sideLengths[0], 2)+pow(self.sideLengths[1], 2)-pow(self.sideLengths[2], 2))/(2*self.sideLengths[0]*self.sideLengths[1])
            return round(cosValue, 2)

    def triangleCategoryByAngle(self):
        if self.obtuseCosValue == 0:
            return "right"
        elif self.obtuseCosValue > 0:
            return "acute"
        else:
            return "obtuse"

    def getTriangleDescription(self):
        if self.isTriangle():
            return self.triangleCategoryByLength()+" "+ self.triangleCategoryByAngle()+" "+ "triangle"
        else:
            return "not a triangle"
