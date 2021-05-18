#nf is no of fields
#FNR is no of records per file
#NR  is total no of records, try with multiple files
BEGIN {ORS=" "}
#output record separator, used by print.. each print prints ORS in the end
#default ORS is newline
/R/	{for (i=0; i<NF; i++) {print i":"$i}; printf "**\n";}
					#print prints ORS, printf doesn't 
