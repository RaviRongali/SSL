from functools import reduce #needed for new python

l = [1,2,3,10]

def sum (x,y):
	return (x+y)

def myfunc(g,l):
	return reduce (g,l)

x = myfunc(sum,l)

print (x)
