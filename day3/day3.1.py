f = open("input.txt", "r")
inp = []
for x in f:
	inp.append(x)


def tree_counter(right, down):
	row = 0
	col = 0
	tree_count = 0
	row_len = len(inp[0]) -1

	while(row < len(inp)):
		r = inp[row]
		if r[col] == '#':
			tree_count += 1
		#print(r, col, tree_count)
		if col + right >= row_len:
			col = col - row_len  + right
		else:
			col += right

		row += down
	return tree_count

# first part
print(tree_counter(3,1))

trees= 1
for r,d in ((1,1),(3,1),(5,1),(7,1),(1,2)):
	trees *= tree_counter(r,d)


print(trees)