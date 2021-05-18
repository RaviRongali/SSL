#! /bin/bash
	if [ ! -e $2 ]
	then
	cp  -u  $1 $2 
	echo "copied<$1>"
	else
	echo "not copied<$2>"
	fi 
