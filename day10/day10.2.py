f = open("input.txt", "r")

all_jolts = sorted([int(x) for x in f])

# input jolt is 0 and last is pc
all_jolts.insert(0,0)
pc = max(all_jolts) + 3
all_jolts.append(pc)


jolts_conn = {} # {1: [2,3], 2: [3,5], 3:[5], 5:[8]}
for j in all_jolts:
	jolts_conn[j] = []
	for x in range(1,4):
		if x + j in all_jolts:
			jolts_conn[j].append(x+j)

#print(jolts_conn)

connections_map = {}

def rec_count(current_jolt,glob_counter):
	
	connections = jolts_conn[current_jolt]

	for connection in connections:
		if connection == pc:
			glob_counter +=1
			connections_map[connection] = 1
		elif connection in connections_map:
			glob_counter += connections_map[connection]
		else:
			comb = rec_count(connection, glob_counter)
			glob_counter += comb
			connections_map[connection] = comb
	return glob_counter

glob_counter = 0
for current_jolt in jolts_conn:
	glob_counter += rec_count(current_jolt, glob_counter)

#print(connections_map)

# sum up the first combinations coming out from 0
result = 0
for first_conn in jolts_conn[0]:
	result += connections_map[first_conn]
print(result)
