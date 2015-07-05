# -*- coding: big5 -*-
# VR module 
# calculate "volume ratio"
# 
import glob, os, sys, platform
import sqlite3 as lite
from os.path import basename

con = None
db_postfix=".sl3"
 

################## module section ##################
# 
# arguments: 
#	db_fpath: database full path 
# length_cal: length of day to calculate
# 
def module_func(db_fpath, length_cal):
	'''
		Volume ratio
	'''

	# numDaytoCal=30
	numDaytoCal=1
	if (int(length_cal)<0 ):								
		long_calDateNum=length_cal
	else:
		long_calDateNum=108
	mid_calDateNum=36
	short_calDateNum=12

	posVol=0
	negVol=0
	eqVol=0

	perviousDayClose=0.0

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
		'CLOSE',
		'Stock_number']
	# print("Processing DB " + db_fpath) 

	con = lite.connect(db_fpath)

	# "with" keyword will release resource autombatically and handle error.
	with con:
		cur = con.cursor()    
		# print ("connect DB...") 

		# list data from numbers of day
		for offsetDay in range(0, numDaytoCal):
			# print ("--------------- %10d --------------- " % offsetDay ) 
			# list numbers of day to calculate
			cur.execute("select " + Query_item[0] + "," + Query_item[2] + " from stock order by Date desc limit 1 offset " + str(offsetDay))
			record=cur.fetchall()
			# print( " %d |" % record[0] ,end="")
			# for result in record:
			#	print( " %d | vol: " % result[0] , result[1])

			# inverse calculate # from older day start
			cur.execute("select " + Query_item[0] + "," + Query_item[1] + "," + Query_item[2] + " from stock order by Date desc limit " + str(long_calDateNum) + " offset " + str(offsetDay))
			record=cur.fetchall()
			idx_Date=0
			idx_CLOSE=1
			idx_STOCK_NUM=2

			idx = -1
			# check which length is shorted to prevent out of range 
			if long_calDateNum > len(record):
				len_cal = len(record)
			else :
				len_cal = long_calDateNum
			# print ("\tlen of record %d" % len(record) )

			# count by neg index 
			while (len_cal+1) > (-idx):
				# print("\tidx " + str(idx) + "\t\t", end="") 
				# print( str(record[idx][idx_CLOSE])  )
				pClose = 0.0
				if(str(record[idx][idx_CLOSE]) == "--"):
					pClose = 0.0
				else :
					pClose = float(record[idx][idx_CLOSE])
				# print( " %f "  % float(record[idx][idx_CLOSE]))

				if(-1 == idx):
					eqVol = record[idx][idx_STOCK_NUM]
					# print( " case 1")
				elif ( pClose < perviousDayClose): 
					negVol = negVol + record[idx][idx_STOCK_NUM]
					# print( " case 2 [%f]<>[%f] "  % (perviousDayClose, pClose))

				elif(pClose > perviousDayClose): 
					posVol = posVol + record[idx][idx_STOCK_NUM]
					# print( " case 3 [%f]<>[%f] "  %( perviousDayClose, pClose))

				else : 
					eqVol = eqVol + record[idx][idx_STOCK_NUM]
					# print( " case 4 [%f]<>[%f]"  % (perviousDayClose, pClose))
				
				if(str(record[idx][idx_CLOSE]) == "--") :
					perviousDayClose = 0.0
				else :
					perviousDayClose = float(record[idx][idx_CLOSE])
				idx = idx -1

			result = 0 
			# print ("\t Neg Vol = %d, equal Vol = %d, post Vol = %d" % (negVol ,eqVol, posVol))

			if (negVol + eqVol) != 0: 
				result = (posVol + eqVol*0.5) / (negVol + eqVol*0.5) * 100
			else :
				print ("\t[Error] Neg Vol = %d, equal Vod = %d" % (negVol ,eqVol))

			return round(result,2)

