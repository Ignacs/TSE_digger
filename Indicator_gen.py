# -*- coding: big5 -*-
# test that how to call module_template.py 
import glob, os, sys, platform, subprocess
# import module_PriceAVG 
import module_VR

def debug_info(strMsg):
	print (strMsg)

# for idx in 
	#module_PriceAVG module_PriceAVG.module_func()
arg='/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
module_VR.module_func(arg)

sys.exit()
