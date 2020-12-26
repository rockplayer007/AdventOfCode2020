f = open("input.txt", "r")

bag1 = set()
bag2 = []
outer = set()
count = 0
contains_star = set()
bags = {}

for x in f:
	b1 = x.split("contain")[0]
	b1 = b1.split(' ')[0] + ' ' + b1.split(' ')[1] 
	bn = x.split("contain")[1].split(',') 
	b_row = []
	for b in bn:
		# 'no other bags'
		if b.split(' ')[1] != 'no':
			# ' 2 dotted green bags'
			b_row.append(b.split(' ')[2] + ' ' + b.split(' ')[3])

	if 'shiny gold' in b_row:
		contains_star.add(b1)

	bags[b1] = b_row
	bag1.add(b1)
	bag1.update(b_row)
	bag2 = [b1] + b_row + bag2
	outer.add(b1)
	count += 1

new_added = [x for x in contains_star]

pos = 0
#print(new_added)
while pos < len(new_added):
	current_bag = new_added[pos]
	for main_bag in bags:
		if current_bag in bags[main_bag]:
			contains_star.add(main_bag)
			if main_bag not in new_added:
				new_added.append(main_bag)

	pos += 1


print(len(contains_star))