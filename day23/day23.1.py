import time
start_time = time.time()

cups = '315679824'
cups = [int(x) for x in cups] #+ [x for x in range(10, 1000001)]


for round in range(100):



    current_cup = cups.pop(0)
    #cups.append(current_cup) # double check


    next_3 = cups[:3]
    temp_cups = cups[3:]

    to_check = current_cup - 1
    while True:

        if to_check in temp_cups:
            destination = temp_cups.index(to_check)
            cups = temp_cups[:destination + 1] + next_3 + temp_cups[destination + 1:] + [current_cup]
            break
        else:
            to_check -= 1
            if to_check < min(temp_cups):
                to_check = max(temp_cups)


#print(''.join(map(str, cups[cups.index(1) + 1:] + cups[:cups.index(1)])))
print(cups[0])
print("--- %s seconds ---" % (time.time() - start_time))