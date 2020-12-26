from itertools import chain

f = open('input.txt', 'r')

attributes = {} # name_attribute: [ranges]
my_ticket = []
all_tickets = []

# parse attributs
curr_line = f.readline()
while curr_line != '\n':
	ranges = curr_line.split(':')[1].split('or')
	ranges = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1) for x in ranges]
	attributes[curr_line.split(':')[0]] = ranges

	curr_line = f.readline()

# read my ticket
f.readline()
my_ticket = list(map(int, f.readline().split(',')))
f.readline()

# nearby tickets
f.readline()
curr_line = f.readline()
while curr_line:

	all_tickets.append(list(map(int, curr_line.split(','))))

	curr_line = f.readline()

########


conc = chain(range(0))
# create concatenation 
for attr in attributes:
	conc = chain(conc, *attributes[attr])


conc = set(conc)
temp_tickets = all_tickets[:]
for t in temp_tickets:
	for attr in t:
		if attr not in conc:
			all_tickets.remove(t)
			break


# start finding matchings
mapping = {} # pos: [attributs]
for p in range(len(all_tickets[0])):
	mapping[p] = list(attributes.keys())


to_remove = [] # the ones that match that don't need to be taken in consideration anymore
all_tickets = all_tickets + [my_ticket]
for ticket in all_tickets:
	for pos in range(len(ticket)):
		curr_attr = ticket[pos]
		available_attr = mapping[pos]

		new_attr = []
		if len(available_attr) == 1:
			continue
		for attr in available_attr:
			ranges = attributes[attr]

			if attr in to_remove:
				# don't add
				continue
			if curr_attr in ranges[0] or curr_attr in ranges[1]:
				new_attr.append(attr)
			# else
				# don't add 
		if len(new_attr) == 1:
			to_remove.append(new_attr[0])

		mapping[pos] = new_attr

# final reduction
while len(mapping.keys()) != len(to_remove):
	for pos in mapping:

		if len(mapping[pos]) == 1:
			continue
		new_attr = []
		for attr in mapping[pos]:
			if attr not in to_remove:
				new_attr.append(attr)

		if len(new_attr) == 1:
			to_remove.append(new_attr[0])
		mapping[pos] = new_attr


#for m in mapping:
#	print(m, mapping[m])


positions = [p for p in mapping  if 'departure' in mapping[p][0]]

sol = 1
for p in positions:
	sol *= my_ticket[p]

print(sol)