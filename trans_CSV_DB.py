# -*- coding: big5 -*-
import csv
import glob, os, sys, platform
import sqlite3 as lite

con = None
idx_fileCSV=1
idx_outputFolder=2

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
csv_file=sys.argv[idx_fileCSV]

print ">>>>> handle " + csv_file + " <<<<<"
db_name = csv_file[0] + csv_file[1] + csv_file[2] + csv_file[3] + ".sl3"
print "build database [" + db_name + "]"
con = lite.connect(db_name)
# "with" keyword will release resource autombatically and handle error.
with con:
	cur = con.cursor()    
	# table format 
	# "日期","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比"
	# cur.execute("DROP TABLE IF EXISTS " + str(db_name))
	cur.execute(''' CREATE TABLE IF NOT EXISTS stock (
			Date INT,
			Stock_number INT, 
			volumn INT,
			Trade_money INT,
			Open REAL, 
			HIGHEST REAL,
			LOWEST REAL,
			CLOSE REAL,
			UP_DOWN TEXT, 
			DIFF REAL,
			BUY REAL, 
			BUY_VOL INT, 
			SELL REAL,
			SELL_VOL INT,
			PE INT)''')
	# create INDEX for speed-up quary
	# cur.execute("CREATE INDEX stock ON stock(title);

	# Insert a row of data
	cur.execute("INSERT INTO stock VALUES ('20150626','4926733','1336','346310265','70.45','70.45','70.15','70.45',' ','0','70.4','9','70.45','41','0.00')")


	# Save (commit) the changes
	# cur.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	# cur.close()
