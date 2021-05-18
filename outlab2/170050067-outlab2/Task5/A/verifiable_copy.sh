#! /bin/bash
cat $1 | tee $2 | md5sum > $2.md5
sed -i -e "s/-/$2/g" $2.md5
md5sum -c $2.md5


