import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re
#import win32com
#from win32com.client import Dispatch, constants
#from win32com.client import DispatchEx


p = re.compile('["]([^"]*)["]')

#櫃買 960701

# old web site is not avaiable
#strOTCURL='http://www.gretai.org.tw/ch/stock/aftertrading/DAILY_CLOSE_quotes/RSTA3104_' #960702.csv
strOTCURL="http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_download.php?l=zh-tw&d=" #104/05/06&s=0,asc,0

today = datetime.today()
yesterday=today

dayback=sys.argv[1]   #下載資料日數[以今日起算]
outPATH= sys.argv[2]  #檔案輸出目錄

if dayback=='':
    daynumMAX=1
else:
    if int(dayback)>0:
        daynumMAX=int(dayback)
    else:
        daynumMAX=1
 

for i in range(1,daynumMAX):
    yesterday = yesterday - timedelta(1)  

#檢查輸出目錄是否存在
cond1=os.path.exists(outPATH)
if (not cond1):
  try:
    os.system('mkdir '+outPATH) 
    cond1=1
  except IOError as IOE :
    print ('output folder ' +outPATH +' cant build')   
    cond1=0

#確認輸出目錄建立成功，才進行

if(cond1):
  #檢查輸出目錄是否存在         
  outDST=outPATH+'CLOSE/'
  cond1A=os.path.exists(outDST)
  if (not cond1A):
    try:
      os.system('mkdir '+outDST) 
      cond1A=1
    except IOError as IOE :
      print ('output folder ' +outDST +' cant build ')   
      cond1A=0
  #檢查輸出目錄是否存在         
  outAB=outPATH+'AB/'
  cond2A=os.path.exists(outAB)
  if (not cond2A):
    try:
      os.system('mkdir '+outAB) 
      cond2A=1
    except IOError as IOE :
      print ('output folder' +outAB +' cant build')   
      cond2A=0
  #開始下載
  for daynum in range(1,daynumMAX+1):
    #print (int(yesterday.strftime('%Y%m%d')))                    
    if( int(yesterday.strftime('%Y%m%d')) >= 20070423):
      inputEntry = yesterday.strftime('%Y_%m_%d').split('_')
      #日期檢查    
      YYYY= inputEntry[0]
      MM= inputEntry[1]
      DD=inputEntry[2] 
      TAIYYYY=int(YYYY)-1911
      sTAIYY='%03d'%TAIYYYY
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
      #櫃買每日收盤行情
      #condIDX1=0
      condIDX=0
      #strOTCIDX1=strOTCURL+YYYY1+MM+DD+'.html'  
# strOTCURL="http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_download.php?l=zh-tw&d=104/05/06&s=0,asc,0"
      strOTCIDX2=strOTCURL+sTAIYY+'/'+MM+'/'+DD+'&s=0,asc,0'
      strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
      Cond2=os.path.exists(strDSTIDX1)
      if not Cond2:              
        print ('Connecting...')  
        for retryCount in range(0,3): 
          try:
            time.sleep(0.2)  
            #print (strOTCIDX2)   
            
            condIDX=urllib.request.urlretrieve(strOTCIDX2,strDSTIDX1)
            break 
          except IOError as IOE :
            time.sleep(2)   
            condIDX=0
            print ('Connection failed: try',retryCount)  

        if condIDX:
          print('(%03d'%daynum+')  (1): '+strDSTIDX1+' download complete')
        else:
          print("  Warning ("+YYYY+MM+DD+") is not a trade day")  
          condIDX=0          
      else:
        condIDX=1
        print(strDSTIDX1+" already exist.")       
         
      if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
          print("  Warning ("+strDSTIDX1+") is not a valid file， ("+YYYY+MM+DD+") is not a trade day\n")
          os.remove(strDSTIDX1) 
          condIDX1=0
          condIDX2=0
# Ignore AB database output # 2015/5/6
#     else:       
#         if condIDX:             
#           Cond1=os.path.exists(strDSTIDX1)
#           if Cond1:
#             sectionstart=0
#             u1=open(strDSTIDX1)
#              rows = u1.read().split('\n')
#              outfileT1=outAB+YYYY+MM+DD+'.csv'
#              f1 = open(outfileT1, 'w')
#              print('      Generating ' + outfileT1) 
#              #f.write('證券代號,證券名稱,成交股數,成交筆數,成交金額,開盤價,最高價,最低價,收盤價,漲跌(+/-),漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比'+'\n')
#              for row in rows:
#                row=p.sub(lambda m: m.groups()[0].replace(',',''), row)
#                row=row.replace('=','')
#                #row=row.replace('"','')
#                #print(row)
#                if ('ID' in row): 
#                                 #代號,名稱,收盤 ,漲跌,開盤 ,最高 ,最低,均價 ,成交股數  ,成交金額(元),成交筆數 ,最後買價,最後賣價,發行股數 ,次日參考價 , 次日漲停價 ,次日跌停價 
#                  sectionstart=1
#                if ('Total numbers:' in row or 'managment stocks'  in row):
#                  sectionstart=0    
#                if (sectionstart==1 and (row!='')):
#                  if ('id' in row):
#                    f1.write('證券代號,日期,開盤價,最高價,最低價,收盤價,成交張數,證券名稱,成交筆數,成交金額,漲跌(+/-),最後揭示買價,最後揭示賣價\n')    
#                  else:	
#                    item=row.split(',')
#                    if ((len(item[0])<=5) and (item[2]!=" ---") and (item[2]!="0.00")):
#                      f1.write(item[0]+'.TW,'+YYYY+'/'+MM+'/'+DD+','+item[4]+','+item[5]+','+item[6]+','+item[2]+','+str(float(item[8])/1000)+','+item[1]+','+item[10]+','+item[9]+','+item[3]+','+item[11]+','+item[12]+'\n')
#              f1.close()  
#              u1.close()
#              print('      OTC CLOSE data(' + outfileT1+') 完成\n')
    else:                                                       
       print('Specified date: ('+yesterday.strftime('%Y%m%d')+') cant download')   
       
    yesterday = yesterday + timedelta(1)  
else:
    print('Specified output folder: ('+outPATH+') cant build')
print('OTC close data download complete.')
