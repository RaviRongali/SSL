#nf is no of fields
#FNR is no of records that have been read so for in that file, reset to 0 every time a new input file is read
#NR  is total no of records, try with multiple files


/R/	{print $0; print "\nNF:"NF  "\t" "FNR:"FNR "\t" "NR:"NR; printf "\n";}
	#for all lines with an R in them


#run this file on just one file called data, 
#and then run it on both data and data1
#to see the difference between FNR and NR
#they count the total records read and not just those that matched
