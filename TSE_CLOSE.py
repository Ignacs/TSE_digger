import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re

p = re.compile('["]([^"]*)["]')
strURL1A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/genpage/Report'
strURL1B='ALLBUT0999_1.php?select2=ALLBUT0999&chk_date='

strURL2A='http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX3_print.php?genpage=genpage/Report'
strURL2B='ALLBUT0999_1.php&type=csv'

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
    print ('輸出目錄' +outPATH +' 無法建立')   
    cond1=0

#確認輸出目錄建立成功，才進行

if(cond1):
  #檢查輸出目錄是否存在         
  outDST=outPATH+'CLOSE\\'  
  cond1A=os.path.exists(outDST)
  if (not cond1A):
    try:
      os.system('mkdir '+outDST) 
      cond1A=1
    except IOError as IOE :
      print ('輸出目錄' +outDST +' 無法建立')   
      cond1A=0
  #檢查輸出目錄是否存在         
  outAB=outPATH+'AB\\'
  cond2A=os.path.exists(outAB)
  if (not cond2A):
    try:
      os.system('mkdir '+outAB) 
      cond2A=1
    except IOError as IOE :
      print ('輸出目錄' +outAB +' 無法建立')   
      cond2A=0
  #開始下載
  for daynum in range(1,daynumMAX+1):      
    #print (int(yesterday.strftime('%Y%m%d')))                    
    if( int(yesterday.strftime('%Y%m%d')) >= 20040211):
      inputEntry = yesterday.strftime('%Y_%m_%d').split('_')
      #日期檢查    
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
      
      print('\n(%04d'%daynum+'/%04d'%daynumMAX+'):'+YYYY+MM+DD+' 開始')
      #每日收盤行情
      condIDX=0
      #strTSEIDX1=strURL1A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL1B+YYYY1+'/'+MM+'/'+DD
      strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
      Cond2=os.path.exists(strDSTIDX1)
      if not Cond2:              
        print ('連線')  
        for retryCount in range(0,3): 
          try:
            time.sleep(0.2)  
            strTSEURLIDX1=strURL2A+YYYY+MM+'/A112'+YYYY+MM+DD+strURL2B
            condIDX=urllib.request.urlretrieve(strTSEURLIDX1,strDSTIDX1)
            break 
          except IOError as IOE :
            time.sleep(2)   
            condIDX=0
            print ('出現連線問題: 嘗試',retryCount)  
        if  condIDX:
            print('(%03d'%daynum+')  (1): '+strDSTIDX1+' 下載完成')
        else:
            print("  警告 ("+YYYY+MM+DD+") 並不是交易日")  
            condIDX=0          
      else:
        condIDX=1
        print(strDSTIDX1+"已經存在")       
         
      if (condIDX and os.path.getsize(strDSTIDX1) <=2048):
          print("  警告 ("+strDSTIDX1+") 不是一個有效的檔案， ("+YYYY+MM+DD+") 並不是交易日\n")
          os.remove(strDSTIDX1) 
          condIDX=0
      else:       
          if condIDX:             
            Cond1=os.path.exists(strDSTIDX1)
            if Cond1:
              sectionstart=0
              u1=open(strDSTIDX1)
              rows = u1.read().split('\n')
              outfileT1=outAB+YYYY+MM+DD+'.csv'
              f1 = open(outfileT1, 'w')
              print('      產生' + outfileT1+' 中') 
              #f.write('證券代號,證券名稱,成交股數,成交筆數,成交金額,開盤價,最高價,最低價,收盤價,漲跌(+/-),漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比'+'\n')
              for row in rows:
                  row=p.sub(lambda m: m.groups()[0].replace(',',''), row)
                  row=row.replace('=','')
                  #row=row.replace('"','')
                  if ('證券代號' in row):
                      sectionstart=1
                  if (sectionstart==1 and (not '漲跌符號' in row) and (not '說明' in row) and (row!='')):
                      if ('證券代號' in row):
                          f1.write('證券代號,日期,開盤價,最高價,最低價,收盤價,成交張數,證券名稱,成交筆數,成交金額,漲跌(+/-),漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比\n')    
                      else:	
                          item=row.split(',')
                          if (int(item[2]) !=0):
                              f1.write(item[0]+'.TW,'+YYYY+'/'+MM+'/'+DD+','+item[5]+','+item[6]+','+item[7]+','+item[8]+','+str(float(item[2])/1000)+','+item[1]+','+item[3]+','+item[4]+','+item[9]+','+item[10]+','+item[11]+','+item[12]+','+item[13]+','+item[14]+','+item[15]+'\n')
              f1.close()  
              u1.close()
              print('      上市台股盤後資料 (' + outfileT1+') 完成\n')
    else:
       print('指定日期: ('+yesterday.strftime('%Y%m%d')+') 無法下載')         
    yesterday = yesterday + timedelta(1)             
      
else:
    print('指定輸出目錄: ('+outPATH+') 無法建立')
print('盤後資料下載完成')
