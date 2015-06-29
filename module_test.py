# -*- coding: big5 -*-
# test that how to call module_template.py 
import glob, os, sys, platform, subprocess
import module_PriceAVG 
import module_template

# python module_template.py  '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
# subprocess.call(['python', 'module_template.py', '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'], shell=False)
# module_PriceAVG.module_func(['/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'])
arg='/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
module_template.module_func(arg)

sys.exit()
