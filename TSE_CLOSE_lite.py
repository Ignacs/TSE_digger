import csv
import string
import codecs
import urllib.parse
import urllib.request
import configparser
import os
import datetime
import shutil
url="http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
values = {'download' : 'csv',
	'qdate' : '104/05/22',
	'selectType' : 'ALLBUT0999' }

data = urllib.parse.urlencode(values)
req= urllib.request.Request(url, data.encode('utf-8'))
response = urllib.request.urlopen(req)

file1=open("test.log","w")
for line in response.read().decode('CP950'):
	if len(line)>0:
		file1.writelines(line)
file1.close()

