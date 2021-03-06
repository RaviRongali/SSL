#! /bin/bash
wget -O temp.pdf $1
pdftotext temp.pdf 
rm temp.pdf
grep 'CS [0-9][0-9][0-9]*' temp.txt > course.txt
grep 'redits :' temp.txt | sed 's/^.*: //' > credits.txt
grep 'Instructor :' temp.txt | sed 's/^.*: //' > instructor.txt
b=$(< "course.txt" wc -l)
printf "Course Code | Course Name | Total Credits | Instructor \n"> ravi.txt
for(( i=1;i<=$b;i++ ))
do
    c2=$(sed -n "${i}p" course.txt)
    c3=$(sed -n "${i}p" credits.txt)
    c4=$(sed -n "${i}p" instructor.txt)
    printf "  $c2 |  $c3 |  $c4 \n" >>ravi.txt 
done
sed -e 's/:/|/g' ravi.txt
rm ravi.txt
rm credits.txt
rm instructor.txt
rm course.txt
rm temp.txt

