# -*- coding: big5 -*-
import csv
import glob, os, sys, platform
import sqlite3 as lite

con = None
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
	os.stat(str(sys.argv[1]))
except:
	print sys.argv[1] + " doesnt exist" 
	sys.exit()
	
# check db folder exist?
try :
	os.stat(str(sys.argv[2]))
except:
	print sys.argv[2] + " doesnt exist" 
	print "try to make it "
	try :
		os.makedirs(sys.argv[2])
	except:
		print "Failed to create it."
		sys.exit()

print "Processing CSV folder " + sys.argv[1] + "..."
print "Output DB folder " + sys.argv[2] + "..."

# through all CSV files
os.chdir(str(sys.argv[1]))
for csv_file in glob.glob("*"):
	print ">>>>> handle " + csv_file + " <<<<<"
	db_name = sys.argv[2] + '/' + csv_file + ".sl3"
	print "build database [" + db_name + "]"
	con = lite.connect(db_name)
	# "with" keyword will release resource autombatically and handle error.
	with con:
		cur = con.cursor()    
		cur.execute("DROP TABLE IF EXISTS " + str(db_name))
		cur.execute("CREATE TABLE " + db_name + "(date INT, Name TEXT, Price INT)")
		cur.execute("INSERT INTO " + db_name + " VALUES(1,'Audi',52642)")
