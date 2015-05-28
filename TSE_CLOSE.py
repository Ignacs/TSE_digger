#-*- coding:utf-8 -*-
import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re

# format 1
strURL1A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/genpage/Report'
strURL1B='ALLBUT0999_1.php?select2=ALLBUT0999&chk_date='

# format 2
strURL2A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX3_print.php?genpage=genpage/Report'
strURL2B='ALLBUT0999_1.php&type=csv'

# format 3, only for "TODAY" 
# example : 'http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104%2F05%2F26&selectType=MS'
strURL3A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate='
strURL3B='&selectType=MS'

# format 4
# example: http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104%2F05%2F26&selectType=ALLBUT0999
strURL4A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate='
strURL4B='&selectType=ALLBUT0999'

############### End of function ###############
# Des: down CSV from specified URL 
#
def dw_CSV_from_URL(dw_URL, output_file):
	for retryCount in range(0,3):
		try:
			time.sleep(0.2)	
			# example : 'http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104%2F05%2F26&selectType=MS'
			condIDX = urllib.request.urlretrieve(dw_URL, output_file)
			break 
		except IOError as IOE :
			time.sleep(2)	 
			condIDX=0
			print ('Connect error: try',retryCount)	

	if	condIDX:
		print('	(1): '+ output_file + ' download complete')
	else: 
		print("	Warning :("+YYYY+MM+DD+") is not a trade day")	
		condIDX=0					

	return condIDX
############### End of function ###############

if 3 > len(sys.argv):
	print ("Too few arguments")
	sys.exit(-1)

# get date, and count total days to output always from today
today = datetime.today()
yesterday=today
autoentry=today.strftime('%Y_%m_%d').split('_')
TAIYYYY1=int(autoentry[0])-1911

# Show download from which day
print ('[Start form ' + str(today) + ']')

dayback = sys.argv[1]	 # How many day to download (count from today)
outPATH= sys.argv[2]	# Output folder

if dayback=='':
	daynumMAX=1
else:
	if int(dayback)>0:
		daynumMAX=int(dayback)
	else:
		daynumMAX=1

for i in range(1,daynumMAX):
	yesterday = yesterday - timedelta(1)	

# Check folder exist?
cond1=os.path.exists(outPATH)
if (not cond1):
	try:
		os.system('mkdir '+outPATH) 
		cond1=1
	except IOError as IOE :
		print ('output folder (' +outPATH +' ) cant build')	 
		cond1=0

# Confirm output folder exist 
if(cond1):
	# Check output folder exist
	outDST=outPATH+'/CLOSE/'
	cond1A=os.path.exists(outDST)
	if (not cond1A):
		try:
			os.system('mkdir '+outDST) 
			cond1A=1
		except IOError as IOE :
			print ('output folder (' +outDST +') cant build')	 
			cond1A=0

	# count and begin to download 
	for daynum in range(1,daynumMAX+1):			
		# print (int(yesterday.strftime('%Y%m%d')))										
		if( int(yesterday.strftime('%Y%m%d')) >= 20040211):
			inputEntry = yesterday.strftime('%Y_%m_%d').split('_')

			YYYY= inputEntry[0]
			MM= inputEntry[1]
			DD=inputEntry[2] 

			# count Chinese of years 
			TAIYYYY=int(YYYY)-1911

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

			print('\n ============ (%04d'%daynum+'/%04d'%daynumMAX+'):'+YYYY+MM+DD+' start ============')
			# daily close
			condIDX=0
			# strTSEIDX1=strURL1A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL1B+YYYY1+'/'+MM+'/'+DD
			strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
			Cond2=os.path.exists(strDSTIDX1)

			# downaload today 
			if daynumMAX+1 == daynum:
				print ('today - using URL type 3')
				# if file has not exist 
				if not Cond2:
					print ('Connection')	
					# try to download with different website
					strTSEURLIDX1=strURL3A+str(TAIYYYY1)+'%2F'+MM+'%2F'+DD+strURL3B
					condIDX = dw_CSV_from_URL(strTSEURLIDX1, strDSTIDX1)
				# if file exists
				else:
					condIDX=1
					print(strDSTIDX1+" already exist")			 

			# date not today
			else:
				# if file has not exist 
				if not Cond2:							
					print ('Connection')	
					strTSEURLIDX1 = strURL2A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL2B
					condIDX = dw_CSV_from_URL(strTSEURLIDX1, strDSTIDX1)
				
				else: # if file exists
					condIDX=1
					print(strDSTIDX1+" already exist")			 
					 
			# script got a file and too small than 2048 bytes
			if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
				print("	Warning ("+strDSTIDX1+") is not a valid file， ("+YYYY+MM+DD+") is not a trade day\n")
				# remove file and retry
				os.remove(strDSTIDX1) 
				condIDX=0

				# try another format 
				print ('Failed. Connection with another format')	
				strTSEURLIDX1 = strURL4A + str(TAIYYYY1) + '%2F' + MM + '%2F'+ DD + strURL4B
				condIDX = dw_CSV_from_URL(strTSEURLIDX1, strDSTIDX1)
				if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
					print("	Warning ("+strDSTIDX1+") is not a valid file， ("+YYYY+MM+DD+") is not a trade day\n")
					# remove file and retry
					os.remove(strDSTIDX1) 
					condIDX=0
				else:
					 print('Date : ('+yesterday.strftime('%Y%m%d')+') cant download')				 

			else:
				 print('Date : ('+yesterday.strftime('%Y%m%d')+') cant download')				 
		# next day
		yesterday = yesterday + timedelta(1)						 
				
else:
	print('Output folder: ('+outPATH+') cant build')


# The end
print('Close data download completion')

