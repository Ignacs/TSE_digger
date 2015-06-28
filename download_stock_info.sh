#!/bin/sh

# python3.2 ~/lab/stock/TSE_dwrobot/TSE_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data
#  python3.2 ~/lab/stock/TSE_dwrobot/OTC_CLOSE.py 180 /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data

TODAY=`date +%y%m%d`
day_num=180
TSE_data_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data
OTC_data_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/OTC_daily_data
Stock_data_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/stock
Database_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/stock_database
backup_folder=/media/data/stock_backup/

log_file=~/lab/log/dw_stock/$TODAY.log

echo "$TODYA start" > $log_file
echo "check $day_num(s)" >> $log_file


echo $1 

# TODO: add file system check later
# if [ ! -e /media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/TSE_daily_data ] ; then 
# 	echo Error with download TSE data.	
# 	exit
# fi 
# 

if [ ! "$1" = "debug" ] ; then
	echo Normal mode 

	# 
	python3.2 ~/roxbins/TSE_CLOSE.py  $day_num  $TSE_data_folder >> $log_file
	python3.2 ~/roxbins/OTC_CLOSE.py  $day_num  $OTC_data_folder >> $log_file
	 
	for idx in $(seq 0 $day_num ) 
	do 
		CALD_DAY=`date '+%C%y%m%d' -d "$end_date-$idx days"`
		echo " Handle $TSE_data_folder/CLOSE/$CALD_DAY.csv " >> $log_file

		python ~/roxbins/dw_TSE_parser.py $TSE_data_folder/CLOSE/$CALD_DAY.csv $Stock_data_folder &>> $log_file
	done
	
	~/roxbins/build_DB.sh	>> $log_file
	
	echo "Total $idx had check ">> $log_file
	
	echo "Executed backup">> $log_file
	rsync -av  $TSE_data_folder $backup_folder >> $log_file
	rsync -av $OTC_data_folder $backup_folder >>  $log_file
	rsync -av $Stock_data_folder $backup_folder >>  $log_file
	rsync -av $Database_folder $backup_folder >>  $log_file

else 
	echo "debug mode"
	python3.2 TSE_CLOSE.py $day_num output/
	 
	for idx in $(seq 0 $day_num ) 
	do 
		CALD_DAY=`date '+%C%y%m%d' -d "$end_date-$idx days"`
		python dw_TSE_parser.py ./output/$CALD_DAY.csv output/
	done
fi 
