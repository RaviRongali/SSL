BEGIN {sum1=0; sum2=0; sum3=0; av1=0; av2=0; av3=0}
	#variables are initialized in BEGIN block

{sum1=sum1+$2; av1+=1}
	#first action sequence, for all patterns
{sum2=sum2+$3; av2+=1}
	#second action sequence, for all patterns
{sum3=sum3+$4; av3+=1}
	#third action sequence, for all patterns
END {print sum1/av1 "\t"  sum2/av2 "\t" sum3/av3}

