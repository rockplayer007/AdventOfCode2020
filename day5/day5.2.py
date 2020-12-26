f = open("input.txt", "r")

mmax = 0
ids = []
for i in f:
	r = int(i[:7].replace('F', '0').replace('B', '1'), 2)
	

	c = int(i[7:].replace('L', '0').replace('R', '1'), 2)

	ids.append(r * 8 + c) 

ids.sort()
found = False
pos = 1
while not found:
	if (ids[pos] - ids[pos-1] == 2 ): 
		print(ids[pos]-1)
		found = True
	pos += 1

