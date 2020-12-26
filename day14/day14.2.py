f = open("input.txt", "r")

memory = {}
current_mask = ''
current_mem = 0
current_value = 0 

def get_mem(ss):
	return int(ss[ss.find('[')+1:ss.find(']')])

def get_value(ss):
	return int(ss[ss.find('=')+1:])

def get_new_value(val, mask):

	val = "{0:b}".format(val).zfill(36)
	new_val = ''
	for pos in range(36):
		if mask[pos] == 'X':
			new_val += val[pos]
		else:
			new_val += mask[pos]

	return int(new_val, 2)

def get_new_memory(mem, mask):
	val = "{0:b}".format(mem).zfill(36)
	new_val = ''
	for pos in range(36):
		if mask[pos] == '0':
			new_val += val[pos]
		else:
			new_val += mask[pos]
	return new_val

def update_memory(mem, val):

	if 'X' not in mem:
		#print("adding to memory: ", int(mem, 2), val)
		memory[int(mem, 2)] = val
	else:
		temp_mem = mem[:mem.index('X')] + '0' + mem[mem.index('X') + 1:]
		update_memory(temp_mem, val)

		temp_mem = mem[:mem.index('X')] + '1' + mem[mem.index('X') + 1:]
		update_memory(temp_mem, val)




for line in f:
	if line[:3] == 'mem':
		current_mem = get_mem(line)
		current_value = get_value(line)

		#current_value = get_new_value(current_value, current_mask)

		update_memory(get_new_memory(current_mem, current_mask), current_value)
	else:
		current_mask = line.split('=')[1].strip()



print(sum(memory.values()))

