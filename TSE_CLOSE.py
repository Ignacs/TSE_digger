#-*- coding:utf-8 -*-
import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re

# usage 
#	python TSE_CLOSE.py 1
#####################################################
# format 1
# strURL1A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/genpage/Report'
# strURL1B='ALLBUT0999_1.php?select2=ALLBUT0999&chk_date='

# format 2
# strURL2A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX3_print.php?genpage=genpage/Report'
# strURL2B='ALLBUT0999_1.php&type=csv'

# format 3, only for "TODAY" 
# example : 'http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104%2F05%2F26&selectType=MS'
# strURL3A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate='
# strURL3B='&selectType=MS'

# format 4
# example: http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104%2F05%2F26&selectType=ALLBUT0999

strURLHistory='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php'

req_values = {'download' : 'csv',
	'qdate' : '104/05/26',
	'selectType' : 'ALLBUT0999' }


############### begin of function ###############
# Des: down CSV from specified URL 
#
def dw_CSV_from_URL( TAI_Y, MM , DD , output_file):
	print ("[Info]download " + TAI_Y + MM + DD ) 
	condIDX=0
	for retryCount in range(0,3):
		try:
			time.sleep(0.2)	
			req_values['qdate'] = TAI_Y + '/' + MM + '/' + DD 
			print ("[Info]" + str(req_values['qdate']))
			
			# new method to download
			data = urllib.parse.urlencode(req_values)
			req= urllib.request.Request(strURLHistory, data.encode('utf-8'))
			response = urllib.request.urlopen(req)

			f=open(output_file,"w")
			for line in response.read().decode('CP950'):
				if len(line)>0:
					f.writelines(line)
					condIDX = 1
			f.close()
			break 
		except IOError as IOE :
			time.sleep(2)	 
			condIDX=0
			print ('[Error] Connect error: try',retryCount)	

	if	condIDX:
		print('	[Info] '+ output_file + ' download complete')
	else: 
		print("	[Warning] :("+YYYY+MM+DD+") is not a trade day")	
		condIDX=0					

	return condIDX
############### End of function ###############


# (python script name) + (day number) + (output folder)
if 3 > len(sys.argv):
	print ("[Error] Too few arguments")
	sys.exit(-1)

# get date, and count total days to output always from today
today = datetime.today()
yesterday=today
autoentry=today.strftime('%Y_%m_%d').split('_')
TAIYYYY1=int(autoentry[0])-1911

# Show download from which day
print ('[Info][Start form ' + str(today) + ']')

dayback = sys.argv[1]	# How many day to download (count from today)
outPATH = sys.argv[2]	# Output folder

if dayback=='':
	daynumMAX=1
else:
	if int(dayback)>0:
		daynumMAX=int(dayback)
	else:
		daynumMAX=1

# Check folder exist?
cond1=os.path.exists(outPATH)
if (not cond1):
	try:
		print( "[Warning] try to make folder")
		os.system('mkdir '+outPATH) 
		cond1=1
	except IOError as IOE :
		print ('[Error] output folder (' +outPATH +' ) cant build')	 
		cond1=0
		exit()

# Check output folder exist
outDST=outPATH+'/CLOSE/'
cond1A=os.path.exists(outDST)
if (not cond1A):
	try:
		os.system('mkdir '+outDST) 
		cond1A=1
	except IOError as IOE :
		print ('[Error] output folder (' +outDST +') cant build')	 
		cond1A=0
		exit()

# count and begin to download 
for daynum in range(1,daynumMAX+1):			
	print ("[Info] check " + str(int(yesterday.strftime('%Y%m%d'))))

	# Confirm output folder exist 
	if(cond1):
		# print (int(yesterday.strftime('%Y%m%d')))										
		if( int(yesterday.strftime('%Y%m%d')) >= 20040211):
			inputEntry = yesterday.strftime('%Y_%m_%d').split('_')

			YYYY= inputEntry[0]
			MM= inputEntry[1]
			DD=inputEntry[2] 

			# count Chinese of years 
			TAIYYYY = int(YYYY)-1911

			# if after era 2000
			if int(YYYY) >2000:
				if TAIYYYY<100:
					YYYY1='%02d'%(TAIYYYY)
				else:
					if TAIYYYY <1000:
						YYYY1='%03d'%(TAIYYYY)
					else:
						YYYY1='%04d'%(TAIYYYY)		
			else: # if before era 2000
				today = datetime.today()
				if TAIYYYY1 < 100:
					YYYY1='%02d'%(TAIYYYY1)
				else:
					if TAIYYYY1 < 1000:
						YYYY1='%03d'%(TAIYYYY1)
					else:
						YYYY1='%04d'%(TAIYYYY1)		

			print('\n [Info] ============ (%04d'%daynum+'/%04d'%daynumMAX+'):'+YYYY+MM+DD+' start ============')
			# daily close
			condIDX=0
			# strTSEIDX1=strURL1A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL1B+YYYY1+'/'+MM+'/'+DD
			strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
			Cond2 = os.path.exists(strDSTIDX1)

			# if file has not exist 
			if not Cond2:							
				print ('[Info] Connection')	
				condIDX = dw_CSV_from_URL( str(TAIYYYY1) , MM , DD, strDSTIDX1)
				# script got a file and too small than 2048 bytes
				if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
					print("	[Warning] ("+strDSTIDX1+") is not a valid file， ("+YYYY+MM+DD+") is not a trade day\n")
					# remove file and retry
					# dont Remove IT, thus script will remove again...
					# os.remove(strDSTIDX1) 
					condIDX=0
				else:
					print('[Warning] Date : ('+yesterday.strftime('%Y%m%d')+') cant download')				 
			else: # if file exists
				condIDX=1
				print("[Warning] " + strDSTIDX1+" already exist")			 
				 
					
		# discreament 1 day
		yesterday = yesterday - timedelta(1)	
	else:
		print('[Error] Output folder: ('+outPATH+') cant build')

# The end
print('[Info] Close data download completion')

