
from src.location import Location, locate

class Node(Location):
    def __init__(self, name):
        self.__name__ = name
