# -*- coding: big5 -*-
import csv
import glob, os, sys, platform
import sqlite3 as lite
from os.path import basename

con = None
idx_fileCSV=1
idx_outputFolder=2
db_postfix=".sl3"
 
# "日期","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比"
item_list = [ 
	'idx_Date',
	'idx_Stock_number',
	'idx_Deal_volumn',
	'idx_Deal_money',
	'idx_Open',
	'idx_HIGHEST',
	'idx_LOWEST',
	'idx_CLOSE',
	'idx_Diff_sign', # ignore 
	'idx_Diff', # ignore diff # calculate by close[n] and close[n+1]
	'idx_Bid_price',
	'idx_BUY_VOL',
	'idx_SELL_price',
	'idx_SELL_VOL',
	'idx_PE' ]

##########################################
# arguments check 
if len(sys.argv) < 3:
	print "Too few arguments. Usage:"
	print "python trans_CSV_DB.py (CSV folder) (database folder)"
	sys.exit(1)

##########################################
# main section
# check CSV folder exist?
try :
	os.stat(str(sys.argv[idx_fileCSV]))
except:
	print sys.argv[idx_fileCSV] + " doesnt exist" 
	sys.exit()
	
# check db folder exist?
try :
	os.stat(str(sys.argv[idx_outputFolder]))
except:
	print sys.argv[idx_outputFolder] + " doesnt exist" 
	print "try to make it "
	try :
		os.makedirs(sys.argv[idx_outputFolder])
	except:
		print "Failed to create it."
		sys.exit()

print "Processing CSV folder " + sys.argv[idx_fileCSV] 
print "Output DB folder " + sys.argv[idx_outputFolder] 

# through all CSV files
os.chdir(str(sys.argv[idx_outputFolder]))
# for csv_file in glob.glob("*"):
# stock data CSV file
csv_fpath=sys.argv[idx_fileCSV]
csv_file = open(csv_fpath,'r' )
csv_fn=basename(csv_fpath)
print ">>>>> handle " + csv_fn + " <<<<<"
# dont support non-stock id , debt of foreign stock  (more than 4 digit number) 
# 
#if len(csv_fn) > 7:
#	if csv_fn[4].isdigit():
#		print "But not accept ..."
#		sys.exit()
#if len(csv_fn) > 6:
#	if csv_fn[4].isdigit():
#		print "But not accept ..."
#		sys.exit()


# putput database file name
db_name = csv_fn[0] + csv_fn[1] + csv_fn[2] + csv_fn[3] + db_postfix

print "build database [" + db_name + "]"
con = lite.connect(db_name)
# "with" keyword will release resource autombatically and handle error.
with con:
	cur = con.cursor()    
	# table format 
	# "日期","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比"
	# cur.execute("DROP TABLE IF EXISTS " + str(db_name))
	cur.execute(''' CREATE TABLE IF NOT EXISTS stock (
			Date INT,
			Stock_number INT, 
			Deal_volumn INT,
			Deal_money INT,
			Open REAL, 
			HIGHEST REAL,
			LOWEST REAL,
			CLOSE REAL,
			BID_PRICE REAL, 
			BUY_VOL INT, 
			SELL_PRICE REAL,
			SELL_VOL INT,
			PE INT)''')
	# create INDEX for speed-up quary
	# cur.execute("CREATE INDEX stock ON stock(title);

	# Insert a row of data
	# csv_line = 0
	for nline_data in csv.reader(csv_file, delimiter=';'):
		# csv_line = csv_line+1
		# print str(csv_line),
		# for idx in range(0, len(nline_data)):
		#	date_line=str(nline_data[idx])
		# 	print '[' + str(idx) + ':' +  date_line + ']',
		cur.execute("INSERT INTO stock VALUES ( '" + str(nline_data[item_list.index('idx_Date')]) + "','" + str(nline_data[item_list.index('idx_Stock_number')]) + "','" + str(nline_data[item_list.index('idx_Deal_volumn')]) + "','" + str(nline_data[item_list.index('idx_Deal_money')]) + "','" + str(nline_data[item_list.index('idx_Open')]) + "','" + str(nline_data[item_list.index('idx_HIGHEST')]) + "','" + str(nline_data[item_list.index('idx_LOWEST')]) + "','" + str(nline_data[item_list.index('idx_CLOSE')]) + "','" + str(nline_data[item_list.index('idx_Bid_price')]) + "','" + str(nline_data[item_list.index('idx_BUY_VOL')]) + "','" + str(nline_data[item_list.index('idx_SELL_price')]) + "','" + str(nline_data[item_list.index('idx_SELL_VOL') ]) + "','" + str(nline_data[item_list.index('idx_PE')]) + "')" )

	# cur.execute("select * from stock where date = " + str(nline_data[0]) ):
	# cur.execute("select * from stock where date=20150628" ):
	# cur.execute("SELECT * FROM stock ")
	#	print ""

	# Save (commit) the changes
	con.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	# con.close()
csv_file.close()
sys.exit()


