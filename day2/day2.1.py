
correct = 0
for x in open("input.txt", "r"):
	# 2-3 v: vhfv
	row = x.split()
	nums = row[0]
	mini = int(nums.split('-')[0])
	maxi = int(nums.split('-')[1])
	letter = row[1][0]
	pwd = []
	pwd[:0] = row[2]
	
	c = pwd.count(letter)
	if c >= mini and c <= maxi: correct += 1

print(correct)