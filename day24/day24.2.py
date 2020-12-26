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
#print(len(to_turn))

# initialize dict
blacks = {}
min_x, min_y = tuple(map(min, zip(*to_turn)))
max_x, max_y = tuple(map(max, zip(*to_turn)))

for xx in range(min_x - 1, max_x + 2):
    for yy in range(min_y - 1, max_y + 2):
        if (xx, yy) in to_turn:
            blacks[(xx, yy)] = True
        else:
            blacks[(xx, yy)] = False


# print(blacks)


def count_black(coord, tiles):
    x, y = coord
    if y % 2 != 0:
        to_check = [(x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1)]
    else:
        to_check = [(x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]

    count_active = 0
    for x_axis in range(x - 1, x + 2):
        for y_axis in range(y - 1, y + 2):
            if not (x_axis == x and y_axis == y):
                new_coord = (x_axis, y_axis)
                if new_coord in blacks:
                    if new_coord in to_check and blacks[new_coord]:
                        count_active += 1
                else:
                    tiles[new_coord] = False

    return count_active


def print_cube():
    string = ''
    minx = min([x[0] for x in blacks.keys()])
    miny = min([x[1] for x in blacks.keys()])
    maxx = max([x[0] for x in blacks.keys()])
    maxy = max([x[1] for x in blacks.keys()])
    print(minx, miny)

    for y_axis in reversed(range(miny, maxy + 1)):
        for x_axis in range(minx, maxx + 1):
            string += '#' if blacks[(x_axis, y_axis)] else '.'
        # for z_axis in range(minz, maxz + 1):
        string += '\n'
    print(string)


for day in range(100):
    #print_cube()
    tiles_temp = blacks.copy()
    for coord in blacks:
        n = count_black(coord, tiles_temp)

        if blacks[coord]:
            if n == 0 or n > 2:
                # flip to white
                tiles_temp[coord] = False
        else:
            if n == 2:
                # flip to black
                tiles_temp[coord] = True

    blacks = tiles_temp.copy()

total = 0
for c in blacks:
    if blacks[c]:
        total += 1

print(total)
