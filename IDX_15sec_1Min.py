import sys
import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re

p = re.compile('["]([^"]*)["]')
strURL1A='http://www.twse.com.tw/ch/trading/exchange/MI_5MINS_INDEX/MI_5MINS_INDEX_PD.php?genpage=genpage%2FReport'
strURL1B='.php&type=csv'
           # Ticker, Open, High, Low, Close
Ticker=["TSE"]*34           
TickerInfo=["指數說明"]*34     
TickerOpen=[0.0]*34
TickerHigh=[0.0]*34
TickerLow=[0.0]*34
TickerClose=[0.0]*34

Ticker[0]="TSE00"    # 發行量加權股價指數
Ticker[1]="TSE01"    # 未含金融保險股指數
Ticker[2]="TSE02"    # 未含電子股指數
Ticker[3]="TSE03"    # 未含金融電子股指數
Ticker[4]="TSE11"    # 水泥類指數
Ticker[5]="TSE12"    # 食品類指數
Ticker[6]="TSE13"    # 塑膠類指數
Ticker[7]="TSE14"    # 紡織纖維類指數
Ticker[8]="TSE15"    # 電機機械類指數
Ticker[9]="TSE16"    # 電器電纜類指數
Ticker[10]="TSE17"   # 化學生技醫療類指數
Ticker[11]="TSE30"   # 化學類指數
Ticker[12]="TSE31"   # 生技醫療類指數
Ticker[13]="TSE18"   # 玻璃陶瓷類指數
Ticker[14]="TSE19"   # 造紙類指數
Ticker[15]="TSE20"   # 鋼鐵類指數
Ticker[16]="TSE21"   # 橡膠類指數
Ticker[17]="TSE22"   # 汽車類指數
Ticker[18]="TSE23"   # 電子類指數
Ticker[19]="TSE32"   # 半導體類指數
Ticker[20]="TSE33"   # 電腦及週邊設備類指數
Ticker[21]="TSE34"   # 光電類指數
Ticker[22]="TSE35"   # 通信網路類指數
Ticker[23]="TSE36"   # 電子零組件類指數
Ticker[24]="TSE37"   # 電子通路類指數
Ticker[25]="TSE38"   # 資訊服務類指數
Ticker[26]="TSE39"   # 其他電子類指數
Ticker[27]="TSE25"   # 建材營造類指數
Ticker[28]="TSE26"   # 航運類指數
Ticker[29]="TSE27"   # 觀光類指數
Ticker[30]="TSE28"   # 金融保險類指數
Ticker[31]="TSE29"   # 貿易百貨類指數
Ticker[32]="TSE40"   # 油電燃氣類指數
Ticker[33]="TSE99"   # 其他類指數

TickerInfo[0] ="發行量加權股價指數"
TickerInfo[1] ="未含金融保險股指數"
TickerInfo[2] ="未含電子股指數"
TickerInfo[3] ="未含金融電子股指數"
TickerInfo[4] ="水泥類指數"
TickerInfo[5] ="食品類指數"
TickerInfo[6] ="塑膠類指數"
TickerInfo[7] ="紡織纖維類指數"
TickerInfo[8] ="電機機械類指數"
TickerInfo[9] ="電器電纜類指數"
TickerInfo[10]="化學生技醫療類指數"
TickerInfo[11]="化學類指數"
TickerInfo[12]="生技醫療類指數"
TickerInfo[13]="玻璃陶瓷類指數"
TickerInfo[14]="造紙類指數"
TickerInfo[15]="鋼鐵類指數"
TickerInfo[16]="橡膠類指數"
TickerInfo[17]="汽車類指數"
TickerInfo[18]="電子類指數"
TickerInfo[19]="半導體類指數"
TickerInfo[20]="電腦及週邊設備類指數"
TickerInfo[21]="光電類指數"
TickerInfo[22]="通信網路類指數"
TickerInfo[23]="電子零組件類指數"
TickerInfo[24]="電子通路類指數"
TickerInfo[25]="資訊服務類指數"
TickerInfo[26]="其他電子類指數"
TickerInfo[27]="建材營造類指數"
TickerInfo[28]="航運類指數"
TickerInfo[29]="觀光類指數"
TickerInfo[30]="金融保險類指數"
TickerInfo[31]="貿易百貨類指數"
TickerInfo[32]="油電燃氣類指數"
TickerInfo[33]="其他類指數"


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
  outDST=outPATH+'IDX\\'  
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
      #每15秒指數盤後統計 
      condIDX=0
      strDSTIDX1=outDST+YYYY+MM+DD+'.csv'
      Cond2=os.path.exists(strDSTIDX1)
      if not Cond2:              
        print ('連線')  
        for retryCount in range(0,3): 
          try:
            time.sleep(0.2)  
            strTSEURLIDX1=strURL1A+YYYY+MM+'%2FA121'+YYYY+MM+DD+strURL1B
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
              outfileT1=outAB+"1Min_"+YYYY+MM+DD+'.csv'
              f1 = open(outfileT1, 'w')
              print('      產生' + outfileT1+' 中') 
              RowCount=0
              for row in rows:
                row=p.sub(lambda m: m.groups()[0].replace(',',''), row)
                row=row.replace('=','')
                RowCount=RowCount+1
                if ('時間,發行量加權股價指數,' in row):
                  sectionstart=1
                if (sectionstart==1 and (row!='')):
                  if ('時間,發行量加權股價指數' in row):
                    f1.write('指數代號,日期,時間,開盤價,最高價,最低價,收盤價,指數名稱\n')    
                  else:	   
                    if RowCount>=3:  
                      item=row.split(',')
                   
                      if ":00" in item[0][-3:]:        
                        #print(RowCount,item)
                        for i in range(0,34):
                          IdxValue=float(item[i+1])
                          TickerOpen[i] =IdxValue # Open
                          TickerHigh[i] =IdxValue # High
                          TickerLow[i]  =IdxValue # Low
                          TickerClose[i]=IdxValue # Close
                        if item[0]=="13:30:00":
                          for i in range(0,34):            
                            f1.write(Ticker[i]+','+YYYY+'/'+MM+'/'+DD+','+item[0]+','+str(TickerOpen[i])+','+str(TickerHigh[i])+','+str(TickerLow[i])+','+str(TickerClose[i])+','+TickerInfo[i]+'\n')                              
                      else:    
                        #print(RowCount,item)
                        for i in range(0,34):
                          IdxValue=float(item[i+1])
                          TickerClose[i]=IdxValue           # Close
                          if IdxValue > TickerHigh[i]:
                             TickerHigh[i]= IdxValue  # High 
                          if IdxValue < TickerLow[i]:
                             TickerLow[i]= IdxValue  #Low
                        if ":45" in item[0]:   
                          pos1=item[0].find(":",3)
                          for i in range(0,34):            
                            f1.write(Ticker[i]+','+YYYY+'/'+MM+'/'+DD+','+item[0][0:pos1+1]+'00,'+str(TickerOpen[i])+','+str(TickerHigh[i])+','+str(TickerLow[i])+','+str(TickerClose[i])+','+TickerInfo[i]+'\n')                              
              f1.close()  
              u1.close()
              print('      指數盤後當日統計    (' + outfileT1+') 完成\n')
    else:
       print('指定日期: ('+yesterday.strftime('%Y%m%d')+') 無法下載')         
    yesterday = yesterday + timedelta(1)             
      
else:
    print('指定輸出目錄: ('+outPATH+') 無法建立')
print('每15秒指數指數盤後當日統計    完成')
