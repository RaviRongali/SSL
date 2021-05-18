l = [1,3,10,20]

it = iter (l)


while True:
	try:
#		x = it.next() #does not work in new python
		x = next (it) 
		print (x)
	except StopIteration:
		print ("list ends")
		break

