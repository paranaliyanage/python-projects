import sys
from triangle import Triangle

class Main(object):
    def __init__(self, type):
        for i in self._parser("input/A-"+type+"-practice.in"):
            line = i.split(" ")
            triangle = Triangle()
            sides = triangle.calculateLengths(self.getIntPoints(line))
            print triangle.calculateArea(sides)

    def _parser(self, filename):
        try:
            file = open(filename, "r", 0)
            number_of_lines = int(file.readline())
            while (number_of_lines > 0):
                line = file.readline()
                number_of_lines -= 1
                yield line

        except IOError:
            print "No file found"

    def getIntPoints(self, line):
        points = []
        for i in line:
            point = i.split("\n")[0]
            points.append(int(point))
        return points

if __name__ == "__main__":
    type = "small"
    if len(sys.argv) > 1 and sys.argv[1] == "large":
        type = "large"
    Main(type)
