f = open("input.txt", "r")

mmax = 0
for i in f:
	r = int(i[:7].replace('F', '0').replace('B', '1'), 2)
	

	c = int(i[7:].replace('L', '0').replace('R', '1'), 2)

	if r * 8 + c > mmax: mmax = r * 8 + c

print(mmax)