#!/bin/sh

# python3.2 ~/lab/stock/TSE_dwrobot/TSE_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data
#  python3.2 ~/lab/stock/TSE_dwrobot/OTC_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data

TODAY=`date +%y%m%d`

python3.2 ~/roxbins/TSE_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data &> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/log_$TODAY
python3.2 ~/roxbins/OTC_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data &> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data/log_$TODAY
python ~/roxbins/dw_TSE_parser.py /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/CLOSE/`date +%y%m%d`.csv /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data &> /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data/log_`date +%y%m%d`

rsync -av  /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data /media/data/stock_backup/TSE_daily_data
rsync -av /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data /media/data/stock_backup/OTC_daily_data
