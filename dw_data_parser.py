# -*- coding: utf-8 -*-
import csv
import sys
f = open(sys.argv[1], 'r')
j=0
for i in csv.reader(f):
	j=j+1
	if len(i) == 16:
		print "[" + str(j) + "] " + str(i)
		
		
f.close()

