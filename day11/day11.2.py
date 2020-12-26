f = open("input.txt", "r")
seats = [x.strip() for x in f]
# add edges
seats.append("." * len(seats[0]))
seats.insert(0, "." * len(seats[0]))
for row in range(len(seats)):
    seats[row] = '.' + seats[row] + '.'



directions = [(x,y) for x in range(-1,2) for y in range(1,-2,-1) if not (x == 0 and y == 0)]
def five_occ_new(rrr, ccc):
    count = 0
    for x, y in directions:
        hit = False
        r = rrr
        c = ccc
        while not hit:
            r += x
            c += y
            if r == 0 or r == len(seats) or c == 0 or c == len(seats):
                break
            #print(r,c)
            current_seat = seats[r][c]
            if current_seat == 'L':
                break
            if current_seat == '#':
                count += 1
                break
    return count >= 5

def all_free_new(rrr, ccc):
    for x, y in directions:
        hit = False
        r = rrr
        c = ccc
        while not hit:
            r += x
            c += y
            if r == 0 or r == len(seats) or c == 0 or c == len(seats):
                break
            current_seat = seats[r][c]
            if current_seat == 'L':
                break
            if current_seat == '#':
                return False
    return True



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
                if all_free_new(row, col):
                    temp_row += '#'
                else:
                    temp_row += 'L'
            elif current_row[col] == '#':
                if five_occ_new(row, col):
                    temp_row += 'L'
                else:
                    temp_row += '#'
        seats_temp.append(temp_row)

    if seats_temp == seats:
        stable = True
    seats = seats_temp[:]
    seats_temp = []

    #for i in seats:
    #    print(i)

occupied = 0
for row in seats:
    occupied += row.count('#')

print(occupied)
# for r in seats:
#	print(r)
