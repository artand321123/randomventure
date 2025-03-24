from random import choice, choices, randint

class Object:
    def __init__(self, name, materials, description='', items=[]):
        self.name = name
        self.description = description
        self.materials = materials
        self.items = items
    
    def __str__(self):
        return self.name

class SquareType:
    def __init__(self, name, objects, max_objects):
        self.name = name
        self.objects = objects
        self.max_objects = max_objects
    
    def __str__(self):
        return self.name

class Square:
    def __init__(self, type):
        self.type = type
        self.objects = []
        #if not randint(0, 2):
        self.objects = choices(self.type.objects, k=randint(0, self.type.max_objects))

class Map:
    def __init__(self, types):
        self.map = {}
        self.types = types
    
    def generate(self, x, y):
        if (x,y) not in self.map:
            self.map[(x, y)] = Square(choice(self.types))

    def square(self, x, y):
        return self.map.get((x, y))

    def object(self, x, y, name):
        obj = next((obj for obj in self.square(x, y).objects if obj.name == name), None)
        if obj is None:
            raise ValueError(f'No such object: {name}')
        return obj