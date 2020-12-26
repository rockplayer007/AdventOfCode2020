f = open("input.txt", "r")



def check_valid(cred):
	if (len(cred) == 8):
		return True	
	elif (len(cred) == 7 and "cid" not in cred):
		return True
	else: return False

def check_valid2(cred):
	b = int(cred['byr'])
	if(b < 1920 or b > 2002): return False

	i = int(cred['iyr'])
	if(i < 2010 or i > 2020): return False

	i = int(cred['eyr'])
	if(i<2020 or i > 2030): return False

	h = cred['hgt']
	if ('cm' in h):
		h = int(h[:-2])
		if(h<150 or h >193): return False
	elif('in' in h):
		h = int(h[:-2])
		if(h<59 or h >76): return False
	else:
		return False

	hc = cred['hcl']
	if(hc[0] == '#' and len(hc) == 7): 
		try:
			int(hc[1:],16)
		except Exception as e:
			return False
	else: return False

	e = cred['ecl']
	if(e not in 'amb blu brn gry grn hzl oth'.split()): return False

	if ('pid' in cred):
		p = cred['pid']
		if(len(p) != 9): return False

	return True






valid = 0
cred = {}
for x in f:
	
	if (x != '\n'):		
		for c in x.split():
			cred[c.split(':')[0]] = c.split(':')[1]
		
	else:
		if (check_valid(cred)): 
			if(check_valid2(cred)):
				valid += 1
		cred = {}

if (check_valid(cred)): 
	if(check_valid2(cred)):
		valid += 1

print(valid)
	#passports.append(x)
