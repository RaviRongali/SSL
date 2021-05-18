#/bin/bash
if [ $# -le 0 ]
then
    echo Usage:./recursiveSearch.sh \<words-to-search\>
    exit 1
else
args=("$@")  
b=${#args[@]} 
e="grep -H -r -n $1 ./Data/"
for (( i=0;i<$b;i++ )); do 
    d=${args[${i}]}
    e="$e | grep $d "
done
eval $e
fi

