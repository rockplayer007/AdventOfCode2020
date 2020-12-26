f = open("input.txt", "r")



def check_valid(cred):
	if (len(cred) == 8):
		return True	
	elif (len(cred) == 7 and "cid" not in cred):
		return True
	else: return False


valid = 0
cred = {}
for x in f:
	
	if (x != '\n'):		
		for c in x.split():
			cred[c.split(':')[0]] = c.split(':')[1]
		
	else:
		if (check_valid(cred)): valid += 1
		cred = {}

if (check_valid(cred)): valid += 1

print(valid)
	#passports.append(x)
