#-*- coding:utf-8 -*-
import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re

p = re.compile('["]([^"]*)["]')
strURL1A='http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report'#201505/201505_F3_1_8_2317.php?STK_NO=2317&myear=2015&mmon=05#

today = datetime.today()
yesterday=today

dayback=sys.argv[1]   # How many day to download (count from today)
outPATH=sys.argv[2]  # Output folder

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
    except IOError as IOE:
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
  # Check output folder exist
  outAB=outPATH+'/AB/' 
  cond2A=os.path.exists(outAB)
  if (not cond2A):
    try:
      os.system('mkdir '+outAB) 
      cond2A=1
    except IOError as IOE :
      print ('Output folder (' +outAB +') cant build')   
      cond2A=0
  # begin to download
  for daynum in range(1,daynumMAX+1):      
    #print (int(yesterday.strftime('%Y%m%d')))                    
    if( int(yesterday.strftime('%Y%m%d')) >= 20040211):
      inputEntry = yesterday.strftime('%Y_%m_%d').split('_')
      # Check date
      YYYY= inputEntry[0]
      MM= inputEntry[1]
      DD=inputEntry[2] 
      TAIYYYY=int(YYYY)-1911
      if int(YYYY) >2000:
          if TAIYYYY<100:
              YYYY1='%02d'%(TAIYYYY)
          else:
              if TAIYYYY <1000:
                  YYYY1='%03d'%(TAIYYYY)
              else:
                  YYYY1='%04d'%(TAIYYYY)    
      else:
          today = datetime.today()
          autoentry=today.strftime('%Y_%m_%d').split('_')
          TAIYYYY1=int(autoentry[0])-1911
          if TAIYYYY1 < 100:
              YYYY1='%02d'%(TAIYYYY1)
          else:
              if TAIYYYY1 < 1000:
                  YYYY1='%03d'%(TAIYYYY1)
              else:
                  YYYY1='%04d'%(TAIYYYY1)    
      
      print('\n(%04d'%daynum+'/%04d'%daynumMAX+'):'+YYYY+MM+DD+' start')
      # daily close
      condIDX=0
      #strTSEIDX1=strURL1A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL1B+YYYY1+'/'+MM+'/'+DD
      strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
      Cond2=os.path.exists(strDSTIDX1)
      if not Cond2:              
        print ('Connection')  
        for retryCount in range(0,3): 
          try:
            time.sleep(0.2)  
            strTSEURLIDX1=strURL2A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL2B
            condIDX=urllib.request.urlretrieve(strTSEURLIDX1,strDSTIDX1)
            break 
          except IOError as IOE :
            time.sleep(2)   
            condIDX=0
            print ('Connect error: try',retryCount)  
        if  condIDX:
            print('(%03d'%daynum+')  (1): '+strDSTIDX1+' download complete')
        else:
            print("  Warning :("+YYYY+MM+DD+") is not a trade day")  
            condIDX=0          
      else:
        condIDX=1
        print(strDSTIDX1+" already exist")       
         
      if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
          print("  Warning ("+strDSTIDX1+") is not a valid file， ("+YYYY+MM+DD+") is not a trade day\n")
          os.remove(strDSTIDX1) 
          condIDX=0
# Ignore AB database output # 2015/5/4
#      else:       
#          if condIDX:             
#            Cond1=os.path.exists(strDSTIDX1)
#            if Cond1:
#              sectionstart=0
#              u1=open(strDSTIDX1, encoding="utf-8") 
#              #u1 = strDSTIDX1.decode('big5','replace')
#              # u1 = unicode(stringVar,'big5','replace')
#              rows = u1.read().split(('\n').encodine('utf-8'))
#              outfileT1=outAB+YYYY+MM+DD+'.csv'
#              f1 = open(outfileT1, 'w')
#              print('      產生' + outfileT1+' 中') 
#              #f.write('證券代號,證券名稱,成交股數,成交筆數,成交金額,開盤價,最高價,最低價,收盤價,漲跌(+/-),漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比'+'\n')
#              for row in rows:
#                  row=p.sub(lambda m: m.groups()[0].replace(',',''), row)
#                  row=row.replace('=','')
#                  #row=row.replace('"','')
#                  if ('SID' in row):
#                      sectionstart=1
#                  if (sectionstart==1 and (not 'sign' in row) and (not 'description' in row) and (row!='')):
#                      if ('SID' in row):
#                          f1.write('證券代號,日期,開盤價,最高價,最低價,收盤價,成交張數,證券名稱,成交筆數,成交金額,漲跌(+/-),漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比\n')    
#                      else:	
#                          item=row.split(',')
#                          if (int(item[2]) !=0):
#                              f1.write(item[0]+'.TW,'+YYYY+'/'+MM+'/'+DD+','+item[5]+','+item[6]+','+item[7]+','+item[8]+','+str(float(item[2])/1000)+','+item[1]+','+item[3]+','+item[4]+','+item[9]+','+item[10]+','+item[11]+','+item[12]+','+item[13]+','+item[14]+','+item[15]+'\n')
#              f1.close()  
#              u1.close()
#              print('      上市台股盤後資料 (' + outfileT1+') 完成\n')
              
    else:
       print('Date : ('+yesterday.strftime('%Y%m%d')+') cant download')         
    yesterday = yesterday + timedelta(1)             
      
else:
    print('Output folder: ('+outPATH+') cant build')
print('Close data download completion')
