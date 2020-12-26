f = open("input.txt", "r")

def split(word): 
    return [char for char in word]  

group = set()
count = 0
for r in f:
	if r != '\n':
		group.update(split(r.rstrip()))
	else:
		count += len(group)
		
		group = set()
count += len(group)
print(count)