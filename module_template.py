# -*- coding: big5 -*-
# called by other python script 
# example : 
#	module_test.py

import glob, os, sys, platform
import sqlite3 as lite
from os.path import basename

con = None
db_postfix=".sl3"
 
# length of indicator 
long_calDateNum=108
mid_calDateNum=36
short_calDateNum=12

############### module function #####################
def module_func(db_fpath):
	print "Processing DB " + db_fpath 
	global long_calDateNum, mid_calDateNum, short_calDateNum

	con = lite.connect(db_fpath)

	# table format 
	#		Date INT,
	#		Stock_number INT, 
	#		Deal_volumn INT,
	#		Deal_money INT,
	#		Open REAL, 
	#		HIGHEST REAL,
	#		LOWEST REAL,
	#		CLOSE REAL,
	#		BID_PRICE REAL, 
	#		BUY_VOL INT, 
	#		SELL_PRICE REAL,
	#		SELL_VOL INT,
	#		PE INT

	# The element to query
	Query_item=[
		'Date',
		'HIGHEST',
		'LOWEST',
		'CLOSE']

	# "with" keyword will release resource autombatically and handle error.
	with con:
		cur = con.cursor()    

		print "Show short-term data"
		for record in cur.execute("select " + Query_item[0] + "," + Query_item[1] + "," + Query_item[2]+ "," + Query_item[3] +" from stock order by Date limit " + str(short_calDateNum)):
			print record[0], 
			print record[1], 
			print record[2], 
			print record[3] 

		print "============================================"
		print "Show short-term data reverse"
		for record in cur.execute("select " + Query_item[0] + "," + Query_item[1] + "," + Query_item[2]+ "," + Query_item[3] +" from stock order by Date desc limit " + str(short_calDateNum)):
			print record[0], 
			print record[1], 
			print record[2], 
			print record[3] 

		# cur.execute("select * from stock where date = " + str(nline_data[0]) ):
		# cur.execute("select * from stock where date=20150628" ):
		# cur.execute("SELECT * FROM stock ")
		#	print ""
		return 

# call by itself
#if __name__ == '__main__':
#	idx_DB=1
#	##########################################
#	# arguments check 
#	if len(sys.argv) < 2:
#		print "Too few arguments. Usage:"
#		print "python module_template.py (database file)"
#		sys.exit(1)
#
#	##########################################
#	# check DB exist?
#	try :
#		os.stat(str(sys.argv[idx_DB]))
#	except:
#		print sys.argv[idx_DB] + " doesnt exist" 
#		sys.exit()
#	module_func(sys.argv[idx_DB])
#		
## call by others 
#else:
#	idx_DB=0
#
#	sys.argv[idx_DB]
#	module_func(sys.argv[idx_DB])
#
# sys.exit()
