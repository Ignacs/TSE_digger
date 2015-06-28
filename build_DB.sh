#!/bin/sh 


Stock_CSV_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/stock
Stock_DB_folder=/media/493742f3-57ea-4deb-8a89-975caf65f8ee/lab/stock_database

idx=1
for csvFile in `ls -d $Stock_CSV_folder/*`  
do
	echo "$idx | $csvFile"
	idx=$((`expr $idx+1`))
	python ~/roxbins/trans_CSV_DB.py $csvFile $Stock_DB_folder
done
