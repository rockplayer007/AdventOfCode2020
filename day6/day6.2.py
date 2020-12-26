f = open("input.txt", "r")

def split(word): 
    return [char for char in word]  

group = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])

count = 0
for r in f:

	if r != '\n':
		group = group.intersection(split(r.rstrip()))
		
	else:
		count += len(group)
		group = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
count += len(group)
print(count)