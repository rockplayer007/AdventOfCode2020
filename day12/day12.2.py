f = open("input.txt", "r")

directions = [(x[0], int(x[1:])) for x in f]

degrees = set([x for x in directions if x[0] == 'R' or x[0] == 'L'])


# print(degrees)
#   N
# W   E
#   S
# (N/S, E/W) (1/-1, 1/-1)


class Direction:
    nesw = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    nesw_dic = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
    posx = 10  # waypoint
    posy = 1
    bx = 0
    by = 0

    # current_dir = 1 # referred to NSEW

    def move(self, d, s):
        if d == 'F':
            self.bx += self.posx * s
            self.by += self.posy * s
        # coord = self.nesw[self.current_dir]
        else:
            coord = self.nesw_dic[d]

            self.posy += s * coord[0]  # N/S
            self.posx += s * coord[1]  # E/W

    def manhattan(self):
        return abs(self.bx) + abs(self.by)

    def turn(self, d, s):
        degree = s / 90

        mul = 1  # Right
        if d == 'L':
            mul = -1

        change = int((mul * degree) % 4)

        if change == 1 or change == -3:  # R
            self.posx, self.posy = self.posy, -self.posx
        elif change == -1 or change == 3:
            self.posx, self.posy = -self.posy, self.posx
        else:  # change == 2
            self.posx, self.posy = -self.posx, -self.posy

    def move_boat(self, d):
        if d[0] == 'L' or d[0] == 'R':
            self.turn(d[0], d[1])
        else:
            self.move(d[0], d[1])


my_dir = Direction()
for d in directions:
    my_dir.move_boat(d)

print(my_dir.manhattan())
