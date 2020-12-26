f = open("input.txt", "r").readlines()

earliest = int(f[0])

others = list(map(int, f[1].replace(',x','').split(',')))

#print(others)
best = 0
current_time = others[0]
for time in others:
	temp = max(best, time % earliest)

	if (best != temp):
		best = temp
		current_time = time

time_to_wait = current_time - (earliest % current_time)


print(time_to_wait * current_time)