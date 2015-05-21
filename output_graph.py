# -*- coding: utf-8 -*-
import csv
f = open('test.csv', 'r')
for i in csv.reader(f):
	print i
f.close()
