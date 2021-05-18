BEGIN 	{sum=0}
	# init

{sum=sum+$3; print $0 "\t" $1 "\t" $3}  
	# $0 gives you the line, and $1 etc the words in that line
	# this action sequence is executed for all patterns

END 	{print "sum=" sum}
	# finally
