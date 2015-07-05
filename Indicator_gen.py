# -*- coding: big5 -*-
# test that how to call module_template.py 
import glob, os, sys, platform, subprocess
# import module_PriceAVG 
import module_VR
import list_all_files

def debug_info(strMsg):
	print (strMsg)

# for idx in 
	#module_PriceAVG module_PriceAVG.module_func()
# arg='/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
# call module
# module_VR.module_func(arg)
################################################################################################
DB_folder='/home/rox/lab/stock/TSE_dwrobot/db_test/'

dbFile_filter='*.sl3'

idx= 1
for foundFiles in list_all_files.get_filepaths(DB_folder, dbFile_filter ):
	print (str(idx)+ " " + str(foundFiles))
	idx=idx+1

sys.exit()
