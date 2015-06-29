# -*- coding: big5 -*-
# test that how to call module_template.py 

import glob, os, sys, platform
import module_template

# python module_template.py `pwd`/db_test/0050.sl3

module_template.module_temp("/home/ignacs/lab/git_test/TSE_robot/TSE_dwrobot/db_test/0050.sl3")

sys.exit()
