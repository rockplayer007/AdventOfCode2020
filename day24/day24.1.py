tiles = open('input.txt').read().split('\n')

class Tile():

    def __init__(self):
        self.x = 0
        self.y = 0
        pass

    def move(self, coord):
        if coord == 'e':
            self.x += 1
        elif coord == 'w':
            self.x -= 1

        elif coord == 'ne':
            if self.y % 2 != 0:
                self.x += 1
            self.y += 1
        elif coord == 'nw':
            if self.y % 2 == 0:
                self.x -= 1
            self.y += 1

        elif coord == 'se':
            if self.y % 2 != 0:
                self.x += 1
            self.y -= 1
        elif coord == 'sw':
            if self.y % 2 == 0:
                self.x -= 1
            self.y -= 1

    def get_coord(self):
        return (self.x, self.y)


to_turn = []
for tile in tiles:
    new_tile = Tile()
    current_coord = ''
    for c in tile:
        if c == 's' or c == 'n':
            current_coord += c
        else:
            current_coord += c
            new_tile.move(current_coord)
            current_coord = ''


    if new_tile.get_coord() in to_turn:
        to_turn.remove(new_tile.get_coord())
    else:
        to_turn.append(new_tile.get_coord())

#print(to_turn)
print(len(to_turn))