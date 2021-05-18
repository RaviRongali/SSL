from inc import ang_to_vec
f=open("euler.out","rU")
lines=f.readlines()
read=[]
for line in lines:
	word=line.split()
	read.append([word])
print read
for line in lines:
	for word in line:
		  for letter in word:
			letter=int(letter)
			
		

k=ang_to_vec(read)
print k
