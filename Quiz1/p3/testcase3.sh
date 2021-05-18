#!/bin/bash

./recursiveSearch.sh "the" "and" "in" | sort > tempfile
diff tempfile output1
rm tempfile

