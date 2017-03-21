# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 01:40:33 2017

@author: Ashton
"""

import os
import numpy as np
import random
from string import *
from sgems_script_wip_WRITE.py import writeSGEMSscript
from reading_control.py import computeVARmaps

# Creates the 2 files (batch and text) needed to run 
# the SGeMS script outside of the GUI. It needs as input the file name
# of the script for SGeMS to run.  On successful run, it will output the
# output file specified in the SGeMS script to the w-d.
path = 'C://Users/Ashton/Documents/School/SeniorDesign/wip/'
scriptname = 'sgems_script_test.py'
batchname = 'test.bat'
runname = 'testrun.txt'
gridfile = 'testgrid320_out.txt'
outfile = 'test320_out.txt'
pointset = 'Sample.txt'
gridname = 'testgrid320'
hardname = 'hardtest320'
propname = 'simtest320'
numreal = '10'

fid = open(batchname,'w')
fid.write('set GSTLAPPLIHOME=C:\SGeMS-x64-Beta \n')
fid.write('C:\SGeMS-x64-Beta\sgems-x64.exe '+runname)
fid.close()

# writeSGEMSscript(scriptname, pointset, gridname, hardname, propname, numreal, gridfile, outfile)
writeSGEMSscript(scriptname,pointset,gridname,hardname,propname,numreal,gridfile,outfile)

fid = open(runname,'w')
fid.write('RunScript '+path+scriptname) # C:/Users/Ashton/Documents/School/SeniorDesign/wip/sgems_script_wip.py')
fid.close()

os.system('test.bat')

[x, y, varmap] = computeVARmaps(gridfile,outfile)

