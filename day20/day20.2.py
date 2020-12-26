tiles = open('input.txt').read().split('\n\n')


class Tile():

    def __init__(self, id, image):
        self.id = id

        self.pic = image.split('\n')
        # from left to right, from top to bottom
        self.edge_e = ''
        self.edge_w = ''
        self.edge_n = self.pic[0][:]
        self.edge_s = self.pic[-1][:]
        for line in self.pic:
            self.edge_w += line[0]
            self.edge_e += line[-1]

    def get_opposite_direction(self, direction):
        if direction == 'e':
            return self.edge_w
        elif direction == 's':
            return self.edge_n
        elif direction == 'w':
            return self.edge_e
        else:
            return self.edge_s

    def get_direction(self, direction):
        if direction == 'e':
            return self.edge_e
        elif direction == 's':
            return self.edge_s
        elif direction == 'w':
            return self.edge_w
        else:
            return self.edge_n

    # turn anticlockwise
    def turn90(self):
        self.edge_n, self.edge_e, self.edge_s, self.edge_w = self.edge_e, self.edge_s[::-1], self.edge_w, self.edge_n[
                                                                                                          ::-1]

        new_img = []
        for pos in range(len(self.pic[0])):
            current_row = ''
            for row in self.pic:
                current_row += row[pos]
            new_img.insert(0, current_row)
        self.pic = new_img

    def flip_horizontal(self):
        self.edge_w, self.edge_e = self.edge_w[::-1], self.edge_e[::-1]
        self.edge_n, self.edge_s = self.edge_s, self.edge_n

        self.pic = self.pic[::-1]


    def __repr__(self):
        return str(self.id)

    def remove_edges(self):
        temp_pic = []
        for line in range(1, len(self.pic) - 1):
            temp_pic.append(self.pic[line][1:-1])
        self.pic = temp_pic

    def print_tile(self):
        for row in self.pic:
            print(row)


class Puzzle():

    def __init__(self):
        self.all_tiles = []
        self.whole_image = []
        self.shrink_image = []  # ['..#', '#..']

    def assemble(self):
        # take a tile
        starting_tile = self.all_tiles.pop(0)

        # go up
        self.move_up_down(starting_tile, 'n')

        # go down
        self.move_up_down(starting_tile, 's')

    def move_up_down(self, starting_tile, up_or_down):
        temp_tiles = self.all_tiles
        current_tile = starting_tile

        while current_tile is not None:
            current_row = [current_tile]

            # go right until tile is an edge
            while current_tile is not None:
                # find right piece for current tile
                current_tile = self.find_match(current_tile.edge_e, 'e', temp_tiles)
                if current_tile is not None:
                    temp_tiles.remove(current_tile)
                    current_row.append(current_tile)

            current_tile = starting_tile

            # go left until tile is an edge
            while current_tile is not None:
                # find right piece for current tile
                current_tile = self.find_match(current_tile.edge_w, 'w', temp_tiles)
                if current_tile is not None:
                    temp_tiles.remove(current_tile)
                    current_row.insert(0, current_tile)

            # add current row
            if len(current_row) != 1:
                if up_or_down == 'n':
                    self.whole_image.insert(0, current_row)
                else:
                    self.whole_image.append(current_row)

            # go one up/down
            current_tile = self.find_match(starting_tile.get_direction(up_or_down), up_or_down, temp_tiles)
            starting_tile = current_tile
            if current_tile is not None:
                self.all_tiles.remove(current_tile)

    def find_match(sefl, edge, direction, pool):

        found = None
        for t in pool:
            for i in range(4):
                for j in range(2):
                    if edge == t.get_opposite_direction(direction):
                        return t
                    t.flip_horizontal()
                t.turn90()

        return found

    def add_tile(self, tile):
        self.all_tiles.append(tile)

    def create_img(self):
        for row in self.whole_image:
            for tile in row:
                tile.remove_edges()

        for row in self.whole_image:

            for one_by_one in range(8):
                current_row = ''
                for tile in row:
                    current_row += tile.pic[one_by_one]

                self.shrink_image.append(current_row)
        # print(len(self.shrink_image[0]), len(self.shrink_image))

    def turn90_img(self):
        new_img = []
        for pos in range(len(self.shrink_image[0])):
            current_row = ''
            for row in self.shrink_image:
                current_row += row[pos]
            new_img.insert(0, current_row)
        self.shrink_image = new_img

    def flip_image(self):
        self.shrink_image = self.shrink_image[::-1]

    def find_monster(self):
        row_count = 0
        monster_count = 0
        len_row = len(self.shrink_image[row_count])
        monster = ['                  # ',
                   '#    ##    ##    ###',
                   ' #  #  #  #  #  #   ']

        for i in range(4):
            for j in range(2):
                for row_count in range(len_row - 3):

                    for shift in range(len_row - len(monster[0])):
                        found = True
                        for row in range(len(monster)):
                            pic_row = self.shrink_image[row_count + row][shift:len(monster[0]) + shift]

                            for pos in range(len(pic_row)):
                                if monster[row][pos] == '#' and pic_row[pos] != '#':
                                    found = False
                                    break
                        if found:
                            monster_count += 1
                # print(monster_count)
                if monster_count > 0:
                    return monster_count
                self.flip_image()
            self.turn90_img()

    def print_image(self):
        for r in self.shrink_image:
            print(r)

    def count_hash(self):
        counter = 0
        for row in self.shrink_image:
            counter += row.count('#')
        return counter


puzzle = Puzzle()
for tile in tiles:
    current_id = int(tile.split(':')[0].split(' ')[1])
    new_tile = Tile(current_id, tile.split(':')[1].strip())

    puzzle.add_tile(new_tile)


puzzle.assemble()
puzzle.create_img()

monsters = puzzle.find_monster()
print(puzzle.count_hash() - monsters *
'''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.count('#'))
