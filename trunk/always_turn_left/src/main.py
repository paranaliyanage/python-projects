import sys

class Main(object):
    def __init__(self, type):
        for i in self._parse("./../input/B-"+type+"-practice.in"):
            line = i.split(" ")
            print line

    def _parse(self, filename):
        try:
            file = open(filename, "r", 0)
            numberoflines = int(file.readline())
            while numberoflines > 0:
                numberoflines -= 1
                yield file.readline()
        except IOError:
            print "No file found"

if __name__ == "__main__":
    type = "small"
    if len(sys.argv) > 1 and sys.argv[1] == "large":
        type = "large"
    Main(type)        