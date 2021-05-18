#! /bin/bash
myfunc(){
    if [[ $1 -le -1 ]]
    then
	echo "invalid"
    else
	
	
	if [[ $1 -eq 0 ]]
	then
	    b=1
	else
	    last=$(myfunc $[$1-1])
	    b=$(($1 * last))
	fi
	echo $b
    fi
    
}
myfunc $1
