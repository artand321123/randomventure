from game.player import *
from game.map import Map, SquareType, Object
from game.items import *
from random import randint
from sys import exit

objects = [
    Object('Tree', [Item('Wood', count=randint(2, 5))]),
    Object('Rock', [Item('Stone', count=randint(1, 3))]),
    Object('Bush', [Item('Stick', count=randint(1, 3))], items=[Item('Berry', count=randint(1, 3))]),
    Object('Chest', [], items=[Item('Gold', count=randint(1, 5)), Item('Tool', count=1)])
]

types = [
    SquareType('Forest', [objects[0], objects[2]], 4),
    SquareType('Mountain', [objects[1], objects[3]], 2)
]

functions = {
    'go': Player.go,
    'inventory': Player.print_inventory,
    'inspect': Player.print_object_info,
    'look': Player.look_around,
    'collect': Player.collect_items,
    'break': Player.break_object,
    'exit': exit
}

def main():
    player = Player(Map(types))

    while True:
        command, *parameters = input('> ').split()

        if command in functions:
            functions[command](player, *parameters)
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()