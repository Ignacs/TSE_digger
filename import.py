import sys
#import urllib.request 
import os.path 
import time
import datetime
from datetime import datetime, timedelta
import re
import win32com
from win32com.client import Dispatch, constants
from win32com.client import DispatchEx

DataBase_Path= sys.argv[1]   #Amiboker資料庫路徑
csvPATH      = sys.argv[2]   #原始資料存放目錄   
formatPATH   = sys.argv[3]   #資料格式檔   

print ("Load DataBase:", DataBase_Path)
# 啟動 Amibroker 資料

AB=Dispatch("Broker.Application")
AB.Visible = 1
AB.LoadDatabase(DataBase_Path)

# Load AB
CNT=0
for file in os.listdir(csvPATH):
  if file[-3:].lower() == "csv":
    time.sleep(0.5) 
    CNT=CNT+1
    AB.Import(0, csvPATH+file, "TWSTK.format")
    print (CNT,": Importing:", csvPATH + file, "using: TWSTK.format")
    AB.SaveDatabase()
#AB.LoadDatabase(DataBase_Path)
AB.RefreshAll() 

#將匯入過的檔案搬至備份區
pathBAK=csvPATH+'BAK\\'
condBAK=os.path.exists(pathBAK)
if (not condBAK):
  try:
    os.system('mkdir '+pathBAK) 
    condBAK=1
  except IOError as IOE :
    print ('備份目錄' +condBAK +' 無法建立')   
    condBAK=0

if condBAK:
  strCMD='move /Y '+csvPATH+'*.* '+ pathBAK
  print(strCMD)
  os.system(strCMD) 