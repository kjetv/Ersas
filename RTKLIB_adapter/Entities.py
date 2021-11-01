class Entity(object):
    name = ""
    def __init__(self, name):
        self.name =  name

class Boat(Entity):
    Sensors = []
    States = []
