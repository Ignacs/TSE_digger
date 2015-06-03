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
if os.stat(str(sys.argv[1])):
	print sys.argv[1] + "doesnt exist" 
	sys.exit()
	
# check db folder exist?
if os.stat(str(sys.argv[2])):
	print sys.argv[2] + "doesnt exist" 
	sys.exit()

print "Processing CSV folder " + sys.argv[1] + "..."
print "Output db folder " + sys.argv[2] + "..."

# through all CSV files
os.chdir(str(sys.argv[1]))
for csv_file in glob.glob("*"):
	print ">>>>> handle " + csv_file + " <<<<<"
	con = lite.connect(sys.argv[2] + csv_file + ".sl3")
	# "with" keyword will release resource autombatically and handle error.
	with con:
		cur = con.cursor()    
		cur.execute("DROP TABLE IF EXISTS " + str(db_name))
		cur.execute("CREATE TABLE " + db_name + "(date INT, Name TEXT, Price INT)")
		cur.execute("INSERT INTO " + db_name + " VALUES(1,'Audi',52642)")
