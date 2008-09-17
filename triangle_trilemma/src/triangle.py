
import math
class Triangle(object):

    def calculateLengths(self, line):
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        x3 = line[4]
        y3 = line[5]
        l1 = math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))
        l2 = math.sqrt(pow((x1-x3), 2)+pow((y1-y3), 2))
        l3 = math.sqrt(pow((x2-x3), 2)+pow((y2-y3), 2))
        return [l1, l2, l3]
    
    def calculateArea(self, sides):
        s = (sides[0]+sides[1]+sides[2])/2
        area = math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))
        return area