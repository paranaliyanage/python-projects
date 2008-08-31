
from converter.converter import Converter

class Main(object):
    def __init__(self):
        for i in self._parser("small.in"):
            line = i.split(" ")
            converter = Converter(line[1], line[2])
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
    Main()