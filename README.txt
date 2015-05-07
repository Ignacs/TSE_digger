README.TXT 本檔案

(0) TSE_eachone.bat 下載上市股票(不含權證)歷史資料
    Usage: 
        python3.2 ./TSE_CLOSE.py 3 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data
    Argument:
        1. Python 執行檔的路徑
        2. Python Script 的路徑
        3. 數字是檔案下載的日數，以今日回算，如果以 2013/6/9 看,數字3就是 2013/6/7 ~ 2013/6/9 
        4. 輸出檔案的目錄) 

    
(1) TSE_CLOSE.bat 下載上市股票(不含權證)收盤資料
    指令格式範例 C:\python33\python C:\盤後\TSE_CLOSE.py 3 C:\盤後\TSE\
    (第一個是Python 執行檔的路徑)上述例子為 C:\python33\python 
    (第二個是Python Script 的路徑)上述例子為 C:\盤後\TSE_CLOSE.py
    (第三個的數字是檔案下載的日數，以今日回算) 上述例子為 3 , 如果以 2013/6/9 看,數字3就是 2013/6/7 ~ 2013/6/9 
    (最後一個是輸出檔案的目錄) 上述例子為 C:\盤後\TSE\

    執行後 在C:\盤後\TSE\ 會產生兩個次目錄 CLOSE 與 AB
    CLOSE內存放證交所的原始資料
    AB 是彙整後的資料 可以給AB import 用import 的格式如下 (參考 TW_STOCK.format)
    
    # Format definition file generated automatically
    # by AmiBroker's ASCII Import Wizard
    $FORMAT Ticker, Date_YMD, Open, High, Low, Close, Volume, Fullname
    $SKIPLINES 1
    $SEPARATOR ,
    $CONT 1
    $GROUP 255
    $AUTOADD 1
    $DEBUG 1
    
    
(2) OTC_CLOSE.bat 下載上櫃股票(不含權證)收盤資料
    指令格式範例 C:\python33\python C:\盤後\OTC_CLOSE.py 3 C:\盤後\OTC\

    (第一個是Python 執行檔的路徑)上述例子為 C:\python33\python
    (第二個是Python Script 的路徑)上述例子為 C:\盤後\OTC_CLOSE.py
    (第三個的數字是檔案下載的日數，以今日回算) 上述例子為 3 , 如果以 2013/6/9 看,數字3就是 2013/6/7 ~ 2013/6/9 
    (最後一個是輸出檔案的目錄) 上述例子為 C:\盤後\OTC\

    執行後 在C:\盤後\OTC\ 會產生兩個次目錄 CLOSE 與 AB
    CLOSE內存放證交所的原始資料
    AB 是彙整後的資料 可以給AB import 用import 的格式 (參考 TW_STOCK.format)

(3) IDX_15Sec_1Min.bat 與  IDX_15Sec_Day.bat 下載指數類收盤資料
    指令格式範例分別為 C:\python33\python C:\盤後\IDX_15Sec_1Min.py 1 C:\盤後\IDX\  
                        C:\python33\python C:\盤後\IDX_15Sec_Day.py 1 C:\盤後\IDX\
                        
    (第一個是Python 執行檔的路徑)上述例子為 C:\python33\python
    (第二個是Python Script 的路徑)上述例子分別為 C:\盤後\IDX_15Sec_1Min.py C:\盤後\IDX_15Sec_Day.py
    (第三個的數字是檔案下載的日數，以今日回算) 上述例子為 1 , 如果以 2013/6/9 看,數字1就是  2013/6/9 
    (最後一個是輸出檔案的目錄) 上述例子為 C:\盤後\IDX\
    
    執行後 在C:\盤後\IDX\ 會產生兩個次目錄 IDX 與 AB
    IDX內存放證交所的原始資料                
    AB 是彙整後的資料 可以給AB import 用import 的格式
    檔案前置文字分別為 1Min_ 與 Day_ 代表 一分鐘K 與 日K
    請注意:匯入AB 時 1Min 與Day 需要的DATABASE 格式不同 (分別參考 IDX_1Min.format 和 IDX_Day.format)

(4) TSE_Vol.bat下載加權指數類收盤資料
    指令格式範例為 C:\python33\python C:\盤後\TSE_vol.py 1 C:\盤後\TSE\
                  
                        
    (第一個是Python 執行檔的路徑)上述例子為 C:\python33\python
    (第二個是Python Script 的路徑)上述例子為 C:\盤後\TSE_vol.py
    (第三個的數字是檔案下載的日數，以今日回算) 上述例子為 1 , 如果以 2013/6/9 看,數字1就是  2013/6/9 
    (最後一個是輸出檔案的目錄) 上述例子為 C:\盤後\TSE\
    
    執行後 在C:\盤後\TSE\ 會產生兩個次目錄 1Min 與 1MAB
    1Min內存放證交所的原始資料                
    1MAB 是彙整後的資料 可以給AB import 用import 的格式 (參考 TSE_vol.format)
  

(5) import.bat
    因為不知哪個原因 如果利用工作排程 批次檔的指令建議如下
    start "匯入資料 to AB" c:\python33\python C:\盤後\import.py  D:\AmiBrokerData\TWSTOCK\ C:\盤後\TSE\AB\ C:\盤後\TW_STOCK.format
    (第一個是批次檔另開視窗指令)上述例子為 start
    (第二個是視窗名稱)上述例子為 "匯入資料 to AB" 
    (第三個是Python 執行檔的路徑)上述例子為 c:\python33\python
    (第四個是Python Script 的路徑)上述例子為  C:\盤後\import.py 
    (第五個是要先用AB建立成功的的 DATABASE 路徑，)上述例子為  D:\AmiBrokerData\TWSTOCK\
    (第六個是匯入的資料檔案存放路徑)上述例子為 C:\盤後\TSE\AB\
    (最後一個是AB使用的格式檔案) 上述例子為  C:\盤後\TW_STOCK.format
    
    執行後 所有在C:\盤後\TSE\AB\ 當原始資料會在匯入完成後移到C:\盤後\TSE\AB\BAK\ 下
    日後如果需要 可以再搬回 C:\盤後\TSE\AB\
    這樣不會重複進行同一檔案的匯入
