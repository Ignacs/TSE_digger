# -*- coding: big5 -*-
import glob, os, sys, platform
import sqlite3 as lite
from os.path import basename

con = None
idx_DB=1
db_postfix=".sl3"
 
# length of indicator 
long_calDateNum=108
mid_calDateNum=36
short_calDateNum=12

# storage
longPriceAVG=0.0
midPriceAVG=0.0
shortPriceAVG=0.0

############### module function #####################
def module_func(db_fpath):
	global long_calDateNum, mid_calDateNum, short_calDateNum, longPriceAVG, midPriceAVG, shortPriceAVG
	print "Processing DB " + db_fpath 

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
		'CLOSE']

	# "with" keyword will release resource autombatically and handle error.
	with con:
		cur = con.cursor()    

		for offsetDay in range(0, 30):
			cur.execute("select " + Query_item[0] + " from stock order by Date desc limit 1 offset " + str(offsetDay))
			record=cur.fetchone()
			print record[0], 

			for record in cur.execute("select " + Query_item[1] + " from stock order by Date desc limit " + str(short_calDateNum) + " offset " + str(offsetDay)):
				shortPriceAVG = shortPriceAVG + record[0] 
			shortPriceAVG = shortPriceAVG/short_calDateNum
			print "%.2f" % round(shortPriceAVG,2),

			for record in cur.execute("select " + Query_item[1] + " from stock order by Date desc limit " + str(mid_calDateNum) + " offset " + str(offsetDay)):
				midPriceAVG = midPriceAVG + record[0] 
			midPriceAVG = midPriceAVG/mid_calDateNum
			print "%.2f" % round(midPriceAVG,2),

			for record in cur.execute("select " + Query_item[1] + " from stock order by Date desc limit " + str(long_calDateNum) + " offset " + str(offsetDay)):
				longPriceAVG = longPriceAVG + record[0] 
			longPriceAVG = longPriceAVG/long_calDateNum
			print "%.2f" % round(longPriceAVG, 2)

		# cur.execute("select * from stock where date = " + str(nline_data[0]) ):
		# cur.execute("select * from stock where date=20150628" ):
		# cur.execute("SELECT * FROM stock ")
		#	print ""

##########################################
# arguments check 
if len(sys.argv) < 2:
	print "Too few arguments. Usage:"
	print "python module_PriceAVG.py (database file)"
	sys.exit(1)

##########################################
# check DB exist?
try :
	os.stat(str(sys.argv[idx_DB]))
except:
	print sys.argv[idx_DB] + " doesnt exist" 
	sys.exit()

module_func(sys.argv[idx_DB])

sys.exit()


