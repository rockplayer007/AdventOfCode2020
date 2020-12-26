f = open("input.txt", "r")
seats = [x.strip() for x in f]
# add edges
seats.append("." * len(seats[0]))
seats.insert(0, "." * len(seats[0]))
for row in range(len(seats)):
    seats[row] = '.' + seats[row] + '.'


# print(seats[row])


def all_free(row, col):
    for r in range(-1, 2):
        for c in range(-1, 2):
            if not (r == 0 and c == 0):
                if seats[row + r][col + c] == '#':
                    return False
    return True


def four_occ(rrr, ccc):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if not (r == 0 and c == 0):
                current_seat = seats[rrr + r][ccc + c]
                if current_seat == '#':
                    count += 1
    return count >= 4


seats_temp = []
stable = False
while not stable:
    for row in range(len(seats)):

        current_row = seats[row]
        temp_row = ''
        for col in range(len(seats[0])):

            if current_row[col] == '.':
                temp_row += '.'
            elif current_row[col] == 'L':
                if all_free(row, col):
                    temp_row += '#'
                else:
                    temp_row += 'L'
            elif current_row[col] == '#':
                if four_occ(row, col):
                    temp_row += 'L'
                else:
                    temp_row += '#'
        seats_temp.append(temp_row)

    if seats_temp == seats:
        stable = True
    seats = seats_temp[:]
    seats_temp = []

    #for i in seats:
     #   print(i)

occupied = 0
for row in seats:
    occupied += row.count('#')

print(occupied)
# for r in seats:
#	print(r)
