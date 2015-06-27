# -*- coding: big5 -*-
# test for import stock CSV file 
# examle : 
#	  20150626;4926733;1336;346310265;70.45;70.45;70.15;70.45; ;0;70.4;9;70.45;41;0.00
#	[0:20150626] [1:4926733] [2:1336] [3:346310265] [4:70.45] [5:70.45] [6:70.15] [7:70.45] [8: ] [9:0] [10:70.4] [11:9] [12:70.45] [13:41] [14:0.00] 
# 


import csv
import glob, os, sys, platform

#

csv_file = open(sys.argv[1], 'r')
csv_line = 0
for nline_data in csv.reader(csv_file, delimiter=';'):
	csv_line = csv_line+1
	print str(csv_line),
	for idx in range(0, len(nline_data)):
		date_line=str(nline_data[idx])
		print '[' + str(idx) + ':' +  date_line + ']',
		idx=idx+1
	print ""

#	print date_line
