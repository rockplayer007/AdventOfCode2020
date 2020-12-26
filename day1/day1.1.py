f = open("input.txt", "r")
inp = []
for x in f:
	inp.append(int(x))

for x in inp:
	for y in inp:
		if (x + y == 2020):
			print(x*y) 
			