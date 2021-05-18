def sq (x):
	return x*x

def collapse (l):
	return map (sq,l)

l=[1,2,3,10]

r = collapse(l)


print (r)  #does not work in new python, as map returns iterator and not list
for x in r:
	print (x) #this will work

