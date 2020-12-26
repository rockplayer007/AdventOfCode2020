from functools import reduce

def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a * b, n)
	for n_i, a_i in zip(n, a):
		p = prod // n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod


def mul_inv(a, b):
	b0 = b
	x0, x1 = 0, 1
	if b == 1: return 1
	while a > 1:
		q = a // b
		a, b = b, a % b
		x0, x1 = x1 - q * x0, x0
	if x1 < 0: x1 += b0
	return x1


if __name__ == '__main__':
	f = open("input.txt", "r").readlines()

	buses = {}
	delay = 0
	for id in f[1].split(','):
		if id != 'x':
			buses[int(id)] = delay
		delay -= 1

	n = list(buses.keys())
	a = list(buses.values())
	print(chinese_remainder(n, a))
'''
#really slow
buses = {}
delay = 0
for id in f[1].split(','):
	if id != 'x':
		buses[int(id)] = delay
	delay += 1

print(delay_buses)

first_bus = list(buses.keys())[0]
last_bus = list(buses.keys())[-1]

if delay_buses == 1:
	delay_buses = first_bus

iteration = 1

found = False
while not found:
	last_time = delay_buses * iteration
	first_time = last_time - first_bus
	#first_time = delay_buses * iteration
	works = True
	for b in buses:
		if (first_time + buses[b]) % b != 0:
			works = False
			break
	if works:
		print(first_time)
		break

	iteration += 1
'''
