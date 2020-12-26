f = open("input.txt", "r")

all_nums = [int(x) for x in f]

pre_start = 0
pre_end = 25

def find_sum(pre, final_sum):
	for r in range(len(pre)-1):
		num1 = pre[r]
		pre2 = pre[r+1:]
		for r2 in range(len(pre2)):
			num2 = pre2[r2]
			if num1 + num2 == final_sum:
				return True

	return False

found = 0
while found == 0:

	to_check = all_nums[pre_end]

	preamble = all_nums[pre_start:pre_end]

	if not find_sum(preamble, to_check):
		found = to_check
		print(to_check)
	
	pre_start += 1
	pre_end += 1



