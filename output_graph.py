#!/usr/bin/python 
#coding: utf-8 

import csv
import sys
import urllib
import sqlite3
import time

print("argvs:")
for i in sys.argv:
	print i
print("----------------")

if sys.argv[1]
	printf("Error when open db.")


# test to read file
# f = open('test.csv', 'r')
# for i in csv.reader(f):
# 	print i
# f.close()

# test print specified row in csv file
#	f = open('example.csv', 'r')  
#	for row in csv.DictReader(f):  
#		print row['¦¨¥æª÷ÃB']  
# f.close()  

# test write data to specified csv file
# data = [  
#	  [' 101/01/31', '5,486,734,180', '162,361,181,834', '1,283,951', '7,517.08', '109.67'],  
#	    [' 101/01/13', '3,497,838,901', '99,286,437,370', '819,762', '7,181.54', '-5.04'],  
#		]  
#	f = open("stock.csv","w")  
#	w = csv.writer(f)  
#	w.writerows(data)  
#	f.close()  

# test to read sqlite3 db
start_time = time.clock()

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

lines = 0
lst = list()
t = ('YES',)
for row in c.execute('SELECT * FROM my_db1 WHERE feature1=?', t):
	lst.append(row)
	lines += 1

	conn.close()

elapsed_time = time.clock() - start_time
print "Time elapsed: {} seconds".format(elapsed_time)
print "Read {} lines".format(lines)
