#! /bin/bash
read r
a=A
b=$r
for (( i=1;i<=26;i++ ))
do
echo "$a" "$b" 
b=$(echo "$b" | tr "A-Z" "ZA-Z")
a=$(echo "$a" | tr "A-Z" "B-ZA")
done

