from collections import deque
import time
start_time = time.time()
cups = '315679824'

cups = [int(x) for x in cups] + [x for x in range(10, 1000001)]

new_cups = {}
for pos in range(len(cups) - 1):
    new_cups[cups[pos]] = cups[pos + 1]
new_cups[cups[pos + 1]] = cups[0]


MAX = max(cups)
current_cup = cups[-1]


for round in range(10000000):
    '''
    if round % 10 == 0:
        print(round)
    '''

    current_cup = new_cups[current_cup]

    next_3 = []
    to_add = current_cup
    for i in range(3):
        to_add = new_cups[to_add]
        next_3.append(to_add)

    to_check = current_cup - 1
    while to_check in next_3 or to_check < 1:
        to_check -= 1
        if to_check < 1:
            to_check = MAX

    new_cups[current_cup] = new_cups[next_3[2]]
    new_cups[next_3[2]] = new_cups[to_check]
    new_cups[to_check] = next_3[0]

'''
string = ''
next = 1
for x in range(8):
    next = new_cups[next]
    string += str(next)

print(string)
'''

print(new_cups[1]*new_cups[new_cups[1]])
print("--- %s seconds ---" % (time.time() - start_time))
