foods = open('input.txt').read().split('\n')

allergens_in_food = {}
all_ingredients = []
for food in foods:
	# remove also parethesis )
	aller_temp = food.strip().split('contains')[1][:-1].split(', ')
	single_ingrediants = set(food.split('(contains')[0].strip().split(' '))
	all_ingredients += food.split('(contains')[0].strip().split(' ')
	for allerg in aller_temp:


		if allerg.strip() in allergens_in_food:
			allergens_in_food[allerg.strip()] = allergens_in_food[allerg.strip()].intersection(single_ingrediants)
		else:
			allergens_in_food[allerg.strip()] = single_ingrediants


dangerous = list(filter(lambda x: len(allergens_in_food[x]) == 1, allergens_in_food))
while len(dangerous) != len(allergens_in_food):

	for allerg in allergens_in_food:

		if len(allergens_in_food[allerg]) == 1:
			continue

		temp_words = allergens_in_food[allerg].copy()
		for word in temp_words:
			if word in [list(allergens_in_food[d])[0] for d in dangerous]:
				allergens_in_food[allerg].remove(word)

	dangerous = list(filter(lambda x: len(allergens_in_food[x]) == 1, allergens_in_food))

#print(dangerous)


collect_dangerous = []
for d in sorted(allergens_in_food):
	for word in allergens_in_food[d]:
		collect_dangerous.append(word)

# part 1
print(len(list(filter(lambda x: x not in collect_dangerous, all_ingredients))))

# part 2
print(','.join(collect_dangerous))