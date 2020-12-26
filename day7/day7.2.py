f = open("input.txt", "r")


shiny = []
bags = {} # {'main_bag': [sub_bags]}

for x in f:
	b1 = x.split("contain")[0]
	b1 = b1.split(' ')[0] + ' ' + b1.split(' ')[1] 
	bn = x.split("contain")[1].split(',') 
	b_row = []
	for b in bn:
		# 'no other bags'
		if b.split(' ')[1] != 'no':
			# ' 2 dotted green bags'
			temp = {} # bag_name: number
			temp[b.split(' ')[2] + ' ' + b.split(' ')[3]] = int(b.split(' ')[1])
			b_row.append(temp)

	if 'shiny gold' in b1:
		shiny = b_row

	bags[b1] = b_row
	

def counter(current_bag, current_count, bags_before):
	bb = bags[current_bag] # [{'b1': 1}, {'b2': 1}, {'b3': 1}]
	if bb == []:
		return bags_before
	current_count = 0
	for b in bb:
		current_bag = list(b.keys())[0]
		bags_inside = b[current_bag]

		current_count += bags_before*counter(current_bag, bags_inside* bags_before, bags_inside)
		print(current_bag, current_count)

	return current_count + bags_before



print(counter('shiny gold',0, 1) - 1)


#print(bags)
#print(shiny)
