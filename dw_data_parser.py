# -*- coding: utf-8 -*-
import csv
import sys
f = open(sys.argv[1], 'r')
j=0
for i in csv.reader(f):
	j=j+1

	print j
	print str(i).encode('big5').decode('big5')
f.close()

