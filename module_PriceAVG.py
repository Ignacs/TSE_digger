# -*- coding: big5 -*-
import glob, os, sys, platform
import sqlite3 as lite
from os.path import basename

con = None
idx_DB=1
db_postfix=".sl3"
 
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
	
print "Processing DB " + sys.argv[idx_DB] 

db_fpath=sys.argv[idx_DB]

con = lite.connect(db_fpath)

long_calDateNum=108
longPriceAVG=0.0
mid_calDateNum=36
midPriceAVG=0.0
short_calDateNum=12
shortPriceAVG=0.0

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

	print "Show short-term data" + str(short_calDateNum)
	for record in cur.execute("select " + Query_item[0] + "," + Query_item[1] + " from stock order by Date desc limit " + str(short_calDateNum)):
		shortPriceAVG = shortPriceAVG + record[1] 
	shortPriceAVG = shortPriceAVG/short_calDateNum
	print "Short AVG : " + str(round(shortPriceAVG,2))

	print "Show mid-term data" + str(mid_calDateNum)
	for record in cur.execute("select " + Query_item[0] + "," + Query_item[1] + " from stock order by Date desc limit " + str(mid_calDateNum)):
		midPriceAVG = midPriceAVG + record[1] 
	midPriceAVG = midPriceAVG/mid_calDateNum
	print "Mid AVG : " + str(round(midPriceAVG,2))

	print "Show long-term data" + str(long_calDateNum)
	for record in cur.execute("select " + Query_item[0] + "," + Query_item[1] + " from stock order by Date desc limit " + str(long_calDateNum)):
		longPriceAVG = longPriceAVG + record[1] 
	longPriceAVG = longPriceAVG/long_calDateNum
	print "Long AVG : " + str(round(longPriceAVG, 2))

	# cur.execute("select * from stock where date = " + str(nline_data[0]) ):
	# cur.execute("select * from stock where date=20150628" ):
	# cur.execute("SELECT * FROM stock ")
	#	print ""

sys.exit()


