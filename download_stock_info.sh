#!/bin/sh

# python3.2 ~/lab/stock/TSE_dwrobot/TSE_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data
#  python3.2 ~/lab/stock/TSE_dwrobot/OTC_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data

TODAY=`date +%y%m%d`

python3.2 ~/roxbins/TSE_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data &>> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/log_$CALD_DAY.log
python3.2 ~/roxbins/OTC_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data &>> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/log_$CALD_DAY.log
 
for idx in $(seq 0 180 ) 
do 
	CALD_DAY=`date '+%C%y%m%d' -d "$end_date+$idx days"`
	python ~/roxbins/dw_TSE_parser.py /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/CLOSE/$CALD_DAY.csv /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data &>> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/log_$CALD_DAY.log
done

rsync -av  /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data /media/data/stock_backup/TSE_daily_data
rsync -av /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data /media/data/stock_backup/OTC_daily_data
