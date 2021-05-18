#!/bin/bash

./recursiveSearch.sh "the" "and" | sort > tempfile
diff tempfile output1
rm tempfile




