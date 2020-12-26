f = open('input.txt', 'r')

cube = {}  # coordinates: active (#) {(x,y,z): True/False}
# x positive down
# y positive right
# z positive up
# active = set()
# inactive = set()

x, y, z, w = 0, 0, 0, 0
for row in f:
    y = 0
    for col in row.strip():
        if col == '#':
            cube[(x, y, z, w)] = True
        else:
            cube[(x, y, z, w)] = False
        y += 1

    x += 1


def add_padding():
    minx = min([x[0] for x in cube.keys()])
    miny = min([x[1] for x in cube.keys()])
    minz = min([x[2] for x in cube.keys()])
    minw = min([x[3] for x in cube.keys()])
    maxx = max([x[0] for x in cube.keys()])
    maxy = max([x[1] for x in cube.keys()])
    maxz = max([x[2] for x in cube.keys()])
    maxw = max([x[3] for x in cube.keys()])

    for x_axis in range(minx - 1, maxx + 2):
        for y_axis in range(miny - 1, maxy + 2):
            for z_axis in range(minz - 1, maxz + 2):
                for w_axis in range(minw - 1, maxw + 2):
                    if (x_axis, y_axis, z_axis, w_axis) not in cube:
                        cube[(x_axis, y_axis, z_axis, w_axis)] = False


def find_active(coordinates, cube_t):
    x, y, z, w = coordinates
    count_active = 0
    for x_axis in range(x - 1, x + 2):
        for y_axis in range(y - 1, y + 2):
            for z_axis in range(z - 1, z + 2):
                for w_axis in range(w - 1, w + 2):
                    if not (x_axis == x and y_axis == y and z_axis == z and w_axis == w):
                        new_coord = (x_axis, y_axis, z_axis, w_axis)

                        if new_coord in cube:
                            if cube[new_coord]:
                                count_active += 1
                        else:
                            cube_t[new_coord] = False

    return count_active


def print_cube():
    string = ''
    minx = min([x[0] for x in cube.keys()])
    miny = min([x[1] for x in cube.keys()])
    minz = min([x[2] for x in cube.keys()])
    maxx = max([x[0] for x in cube.keys()])
    maxy = max([x[1] for x in cube.keys()])
    maxz = max([x[2] for x in cube.keys()])
    print(minx, miny)
    for x_axis in range(minx, maxx + 1):
        for y_axis in range(miny, maxy + 1):
            string += '#' if cube[x_axis, y_axis, 0] else '.'
        # for z_axis in range(minz, maxz + 1):
        string += '\n'
    print(string)


add_padding()
for i in range(6):
    # print_cube()
    cube_temp = cube.copy()
    # active_temp = active.copy()
    # inactive_temp = inactive.copy()

    for coord in cube:

        n = find_active(coord, cube_temp)

        if cube[coord]:
            if n == 2 or n == 3:
                # active remains active
                pass
            else:
                # active becomes inactive
                cube_temp[coord] = False
        else:
            if n == 3:
                # inactive becomes active
                cube_temp[coord] = True
            else:
                # inactive remains inactive
                pass

    cube = cube_temp.copy()

print(len([a for a in cube if cube[a]]))
