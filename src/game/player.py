class Player:
    def __init__(self, map):
        self.x = 0
        self.y = 0
        self.inventory = []
        self.map = map
    
    def go(self, direction):
        if direction == 'up':
            self.y += 1
        elif direction == 'down':
            self.y -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'left':
            self.x -= 1
        else:
            print('Invalid direction')
    
    def print_inventory(self):
        print('Inventory:', ', '.join(map(str, self.inventory)))
    
    def look_around(self):
        self.map.generate(self.x, self.y)
        print('Coordinates:', self.x, self.y)
        current_square = self.map.square(self.x, self.y)
        print(f'Square: {current_square.type}, Objects: {', '.join(map(str, current_square.objects))}')
    
    def print_object_info(self, object):
        object = self.map.object(self.x, self.y, object)
        print(f'{object.name}: {object.description}\nMaterials: {', '.join(map(str, object.materials))}\nItems: {', '.join(map(str, object.items))}')
    
    def collect_items(self, object, items):
        object = self.map.object(self.x, self.y, object)

        for item in object.items:
            if item.name in items:
                if item not in self.inventory:
                    self.inventory.append(item)
                else:
                    self.inventory[self.inventory.index(item)].count += item.count
                object.items.remove(item)
                print(f'Collected {item}')
    
    def break_object(self, object):
        object = self.map.object(self.x, self.y, object)

        for material in object.materials:
            if material not in self.inventory:
                self.inventory.append(material)
            else:
                self.inventory[self.inventory.index(material)].count += material.count
        
        self.map.square(self.x, self.y).objects.remove(object)
        print(f'There is no {object} anymore')