BEGIN 	{sum=0}
	# init

/mgr/ {sum=sum+$3; print $0 "\t" $1 "\t" $3}  
	#look for lines on which regular expression mgr occurs
	#add third field into sum, and print the whole line, and fields 1 and 3

END 	{print "sum=" sum}
	# finally print the sum
