# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 01:40:33 2017

@author: Ashton
"""

import os
import numpy as np
import random
from string import *
from sgems_script_WRITE_revised import writeSGEMSscript
from reading_control import computeVARmaps

# Creates the 2 files (batch and text) needed to run 
# the SGeMS script outside of the GUI. It needs as input the file name
# of the script for SGeMS to run.  On successful run, it will output the
# output file specified in the SGeMS script to the w-d.

def batchrun(i,path,pointset):
    """i, integer for iteration number.  
       path, string indicating path of W.D. 
       pointset, string indicating txt file of SGEMS input data."""
    # i = 1
    # n = 100
    # path = 'C://Users/Ashton/Documents/School/SeniorDesign/wip/'
       
    # Filenames for running the batch
    scriptname = 'scripts/sgems_script%d.py' % (i)
    batchname = 'test%d.bat' % (i)
    runname = 'testrun%d.txt' % (i)
    
    # pointset = 'Sample%d.txt' % (i) # This is now an argument
    
    # SGEMS variable names    
    gridname = 'gridxy'
    hardname = 'hardtest%d' % (i)
    propname = 'simtest%d' % (i)
    
    # SGEMS output data file names
    gridfile = 'gridxy.txt'
    outfile = 'outputs/testout%d.txt' % (i)
    
    numreal = '10'
    
    # Running the batch
    fid = open(batchname,'w')
    fid.write('set GSTLAPPLIHOME=C:\SGeMS-x64-Beta \n')
    fid.write('C:\SGeMS-x64-Beta\sgems-x64.exe '+runname)
    fid.close()
    
    # writeSGEMSscript(scriptname, pointset, gridname, hardname, propname, numreal, gridfile, outfile)
    writeSGEMSscript(path,scriptname,pointset,gridname,hardname,propname,numreal,gridfile,outfile)
    
    fid = open(runname,'w')
    fid.write('RunScript '+path+scriptname) # C:/Users/Ashton/Documents/School/SeniorDesign/wip/sgems_script_wip.py')
    fid.close()
    
    os.system(batchname)
    
    
    # Computing weight matrix and outputting
    [x, y, varmap] = computeVARmaps(gridfile,outfile)
    [nx,ny] = np.shape(varmap)
    
    return nx,ny,varmap
    #varmaps_all = np.zeros(nx,ny,n)
    #varmaps_all[:,:,i] = varmap