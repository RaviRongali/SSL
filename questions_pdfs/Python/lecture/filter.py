def pickbyf(f,l):
	return filter (f,l)

def ev(x):
	if x%2==0:
		return True
	else:
		return False


l = [1,2,3,4,5,6]

r = pickbyf(ev,l)

print (r)

for x in r:
	print (x)

