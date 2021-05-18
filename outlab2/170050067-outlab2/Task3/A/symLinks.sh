#! /bin/bash
find -L $1 -xtype l >  $2
let b=$(< "$2" wc -l)
echo $b
for(( i=1;i<=$b;i++ ))
do
    c=$(sed -n "${i}p" $2)
    if [[ -d $c ]]
    then
	printf "`echo $c` `readlink $c` ` md5sum $c/*/*.*` \n" >> $2
    else
	printf "`echo $c` `readlink $c` `echo $(md5sum $c)` \n" >> $2
	fi
done

