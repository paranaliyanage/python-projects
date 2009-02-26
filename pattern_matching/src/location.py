
class Location(object):
    __parent__ = __name__ = None
    
    
def locate(object, parent):
    object.__parent__ = parent