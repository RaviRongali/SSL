#! /bin/bash
wget -O temp.pdf $1
pdftotext temp.pdf 
rm temp.pdf
