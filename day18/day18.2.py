f = open('input.txt', 'r')

def solve_sub(sub_operation):
	current_op = '+'
	current_res = 0	
	pos = 0
	while pos < len(sub_operation):
	#for literal in sub_operation:
		literal = sub_operation[pos]

		if literal == '+' or literal == '*':
			current_op = literal
		elif literal == '(':
			temp_res, temp_pos = solve_sub(sub_operation[pos + 1:])
			pos += temp_pos

			if current_op == '+':
				current_res += temp_res
			else:
				current_res *= temp_res
		elif literal == ')':
			return current_res, pos+1
		else:
			if current_op == '+':
				current_res += int(literal)
			else:
				current_res *= int(literal)

		pos += 1


	return current_res, pos


def transform(exp):
	new_exp = exp
	if '(' in exp:
		new_exp = exp.replace('(', '((').replace(')', '))')

	if '*' in new_exp:
		new_exp = new_exp.replace('*', ')*(')
	#print(new_exp)
	new_exp = '(' + new_exp + ')'
	#print(new_exp)
	return new_exp


result = 0
for op in f:
	op = op.replace(' ', '').strip()

	op = transform(op)
	result_temp, pos = solve_sub(op)
	result += result_temp




print(result)