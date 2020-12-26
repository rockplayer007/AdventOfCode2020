f = open("input.txt", "r")



line = []
for r in f:
	code = r.split()[0]
	num = int(r.split()[1])
	line.append((code, num))



for pos1 in range(len(line)):
	
	# restore original code
	mod_code = line[:]

	# change the code
	if mod_code[pos1][0] == 'jmp':
		mod_code[pos1] = ('nop', mod_code[pos1][1])
	elif mod_code[pos1][0] == 'nop':
		#if mod_code[pos1][1] == 0:
		#	continue
		#else:
		mod_code[pos1] = ('jmp', mod_code[pos1][1])

	# run the code
	found = False
	loop = True
	pos = 0
	acc = 0
	visited = []
	while loop:

		if pos in visited or pos < 0:
			loop = False

		elif pos == len(mod_code):
			loop = False
			found = True
			print(acc)
		else:
			visited.append(pos)
			code = mod_code[pos][0]
			num = mod_code[pos][1]
			if code == 'acc':
				acc += num
				pos += 1
			elif code == 'jmp':
				pos += num
			else:
				pos += 1


	# check if it works
	if found:
		break
