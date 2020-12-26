f = open("input.txt", "r")

memory = {}
current_mask = ''
current_mem = 0
current_value = 0 

def get_mem(ss):
	return int(ss[ss.find('[')+1:ss.find(']')])

def get_value(ss):
	return int(ss[ss.find('=')+1:])

def update_memory(mem, val, mask):

	val = "{0:b}".format(val).zfill(36)
	new_val = ''
	for pos in range(36):
		if mask[pos] == 'X':
			new_val += val[pos]
		else:
			new_val += mask[pos]

	memory[mem] = int(new_val, 2)


for line in f:
	if line[:3] == 'mem':
		current_mem = get_mem(line)
		current_value = get_value(line)

		update_memory(current_mem, current_value, current_mask)
	else:
		current_mask = line.split('=')[1].strip()



print(sum(memory.values()))
