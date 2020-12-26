f = open("input.txt", "r")

all_jolts = sorted([int(x) for x in f])

# input jolt is 0 and last is pc
all_jolts.insert(0,0)
all_jolts.append(max(all_jolts) + 3)

count_1 = 0
count_3 = 0
for pos in range(len(all_jolts)-1):
	if all_jolts[pos + 1] - all_jolts[pos] == 1:
		count_1 += 1
	elif all_jolts[pos + 1] - all_jolts[pos] == 3:
		count_3 += 1
print(count_1 * count_3 )

