
import sys
from converter.converter import Converter

class Main(object):
    def __init__(self, type):
        for i in self._parser("input/A-"+type+"-practice.in"):
            line = i.split(" ")
            converter = Converter(line[1], line[2].split("\n")[0])
            print converter.convert(line[0])

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


if __name__ == "__main__":
    type = "small"
    if len(sys.argv) > 1 and sys.argv[1] == "large":
        type = "large"
    Main(type)