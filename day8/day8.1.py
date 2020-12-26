f = open("input.txt", "r")



line = []
for r in f:
	code = r.split()[0]
	num = int(r.split()[1])
	line.append((code, num))

pos = 0
acc = 0
visited = []

loop = True
while loop:

	if pos in visited:
		loop = False
	else:
		visited.append(pos)
		code = line[pos][0]
		num = line[pos][1]
		if code == 'acc':
			acc += num
			pos += 1
		elif code == 'jmp':
			pos += num
		else:
			pos += 1
		
print(acc)