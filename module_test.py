# -*- coding: big5 -*-
# test that how to call module_template.py 
import glob, os, sys, platform, subprocess
# python module_template.py  '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
subprocess.call(['python', 'module_template.py', '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'], shell=False)

sys.exit()
