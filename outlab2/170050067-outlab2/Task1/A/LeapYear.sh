#! /bin/bash
let foo=$1
if [ $foo>0 ]
then
    if (( $foo%4==0 ))
    then 
	if (( $foo%100==0 && $foo%400!=0 ))
	then 
	    echo "Not Leap Year!"
	else 
	    echo "Leap Year!"
	fi
    else 
	echo "Not a Leap Year"
    fi
else
    echo "Invalid argument!"
fi



