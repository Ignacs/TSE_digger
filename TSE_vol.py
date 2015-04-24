import sys
import urllib.request 
import os.path 
import datetime
from datetime import datetime, timedelta
import re

p = re.compile('["]([^"]*)["]')

#inputDATE = input('輸入起始西元年_月_日 (如 2012_02_17): ')
#startDATE=datetime.strptime(inputDATE+' 01:00:00', '%Y_%m_%d %H:%M:%S')
#yesterday=startDATE

today = datetime.today()
yesterday=today
#inputDATE = yesterday.strftime('%Y_%m_%d').split('_')

dayback=sys.argv[1] 
if dayback=='':
    daynumMAX=1
else:
    if int(dayback)>0:
        daynumMAX=int(dayback)
    else:
        daynumMAX=1
 
#daynumMAX=int(input('輸入回朔日期數:'))
#outPATH= input('輸入檔案存放目錄 (如 D:\TSE\):')

for i in range(1,daynumMAX):
    yesterday = yesterday - timedelta(1)  

outPATH= sys.argv[2] 
#outPATH='D:\\TSE\\'
#檢查輸出目錄是否存在
path1M=outPATH+'1Min\\'
cond1M=os.path.exists(path1M)
if (not cond1M):
  try:
    os.system('mkdir '+path1M) 
    cond1=1
  except IOError as IOE :
    print ('輸出目錄' +path1M +' 無法建立')   
    cond1=0

path1MAB=outPATH+'1M_AB\\'
cond1MAB=os.path.exists(path1MAB)
if (not cond1MAB):
  try:
    os.system('mkdir '+path1MAB) 
    cond1=1
  except IOError as IOE :
    print ('輸出目錄' +path1MAB +' 無法建立')   
    cond1=0

cond1=os.path.exists(outPATH)
if(cond1):
    for daynum in range(1,daynumMAX+1):
        inputEntry = yesterday.strftime('%Y_%m_%d').split('_')
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

#for y in range(2012, 2013):
# for d in range(1, 32): 
#  for m in range(1, 2): 
# Check trade date
#查無資料:101年01月27日
#目前無資料請稍候再試
#加權指數收盤行情1
        strTSEURLIDX1='http://www.twse.com.tw/ch/trading/exchange/MI_5MINS_INDEX/MI_5MINS_INDEX_PD.php?genpage=genpage%2FReport'+YYYY+MM+'%2F/A121'+YYYY+MM+DD+'.php&type=csv'
        strDSTIDX1=path1M+'TSE_'+YYYY+MM+DD+'.csv'
        condIDX1=urllib.request.urlretrieve(strTSEURLIDX1,strDSTIDX1)
        if condIDX1:
            print('(%03d'%daynum+')\n  (1): '+strDSTIDX1+' 下載完成')
        else:
            print('(%03d'%daynum+')\n  (1): '+strDSTIDX1+' 下載失敗')  
        if (os.path.getsize(strDSTIDX1) <=2048):
            print("  警告 ("+strDSTIDX1+") 不是一個有效的檔案，\n   ("+YYYY+MM+DD+") 並不是交易日\n")
            os.remove(strDSTIDX1) 
        else:     
            Cond1=os.path.exists(strDSTIDX1)
            strTSEURLIDX2='http://www.twse.com.tw/ch/trading/exchange/MI_5MINS/MI_5MINS2.php?input_date='+str(TAIYYYY)+'/'+str(MM)+'/'+str(DD)+'&type=csv'
            strDSTIDX2=path1M+'TSEVOL_'+YYYY+MM+DD+'.csv'
            condIDX2=urllib.request.urlretrieve(strTSEURLIDX2,strDSTIDX2)
            if condIDX2:
              print('(%03d'%daynum+')\n  (1): '+strDSTIDX2+' 下載完成')
            else:
              print('(%03d'%daynum+')\n  (1): '+strDSTIDX2+' 下載失敗')  
            if (os.path.getsize(strDSTIDX2) <=2048):
              print("  警告 ("+strDSTIDX2+") 不是一個有效的檔案，\n   ("+YYYY+MM+DD+") 並不是交易日\n")
              os.remove(strDSTIDX2) 
            else:                    
              Cond2=os.path.exists(strDSTIDX2)
              if (Cond1 and Cond1):
                IDXO=0
                IDXH=-1
                IDXL=1e6
                IDXC=0
                sectionstart=0
                u1=open(strDSTIDX1)
                rows1 = u1.read().split('\n')
                u1.close()
                u2=open(strDSTIDX2)
                rows2 = u2.read().split('\n')
                u2.close()
                outfile=path1MAB+'TSEVOL_'+YYYY+MM+DD+'.csv'
                f = open(outfile, 'w')
                print('      產生' + outfile+' 中') 
                vol=0
                volPrev=0  
                
                for row1 in rows1: #指數資訊
                    row1=p.sub(lambda m: m.groups()[0].replace(',',''), row1)
                    if ('時間' in row1):
                        sectionstart=1
                    if (sectionstart==1 and (row1!='')):
                        row1item = row1.split(',')
                        if ('時間' in row1):
                            f.write('加權股價指數,日期,時間,O,H,L,C,成交金額\n') 
                        else:	
                            timeitem1=row1item[0].split(':')      
                            currentIDX=float(row1item[1].strip())
                            hhmm=int(timeitem1[0])*10000+int(timeitem1[1])*100
                            if (hhmm<133000 and int(timeitem1[2])==0 ):
                              IDXO=currentIDX 
                              IDXH=-1
                              IDXL=1e6
                            else:
                              if currentIDX < IDXL:
                                IDXL=currentIDX
                              if currentIDX > IDXH:
                                IDXH=currentIDX                              
                              
                              if(hhmm==133000):
                                IDXO=currentIDX 
                                IDXH=currentIDX 
                                IDXL=currentIDX 
                                IDXC=currentIDX   

                              if(int(timeitem1[2])==45 or hhmm==133000):  
                                IDXC=currentIDX
                                for row2 in rows2:  #成交量資訊
                                  row2=p.sub(lambda m: m.groups()[0].replace(',',''), row2)
                                  if (row1item[0] in row2):
                                    row2item = row2.split(',')
                                    vol=int(row2item[7].strip())/100-volPrev
                                    volPrev=int(row2item[7].strip())/100 
                                    break
                                timevalue='%02d:%02d:%02d'%(int(timeitem1[0]),int(timeitem1[1]),0)
                                stridxvalue='%.2f,%.2f,%.2f,%.2f'%(IDXO,IDXH,IDXL,IDXC)
                                #print(stridxvalue)
                                f.write('TSEIDX,'+YYYY+'/'+MM+'/'+DD+','+timevalue+','+stridxvalue+','+'%.2f'%(vol)+'\n')
                f.close()
                
        print(yesterday.strftime('%Y_%m_%d').split('_'))
        yesterday = yesterday + timedelta(1)        
        
else:
  print('ERROR')

print('DONE')
