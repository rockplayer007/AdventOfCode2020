from itertools import chain

f = open('input.txt', 'r')

attributes = {}
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
my_ticket = map(int, f.readline().split(','))
f.readline()

# nearby tickets
f.readline()
curr_line = f.readline()
while curr_line:

	all_tickets.append(map(int, curr_line.split(',')))

	curr_line = f.readline()

conc = chain(range(0))
# create concatenation 
for attr in attributes:
	conc = chain(conc, *attributes[attr])


conc = set(conc)
wrong = []
for t in all_tickets:
	for attr in t:
		if attr not in conc:
			wrong.append(attr)

#print(wrong)
print(sum(wrong))

