class Item:
    def __init__(self, name, description='', count=1):
        self.name = name
        self.description = description
        self.count = count

    def __str__(self):
        if self.count > 1:
            if self.name[-1] == 'y':
                return f'{self.count} {self.name[:-1]}ies'
            else:
                return f'{self.count} {self.name}s'
        return self.name