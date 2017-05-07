# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:23:49 2017
@author: Ashton
"""

import os
import numpy as np
import random
from string import *
from sgems_script_WRITE_revised import writeSGEMSscript
from testing_reading_control import computeVARmaps
import time

# Creates the 2 files (batch and text) needed to run 
# the SGeMS script outside of the GUI. It needs as input the file name
# of the script for SGeMS to run.  On successful run, it will output the
# output file specified in the SGeMS script to the w-d.

def batchrun(i,path,numreal,pointset):
    """i, integer for iteration number.  
       path, string indicating path of W.D. 
       pointset, string indicating txt file of SGEMS input data.
       numreal, number of realizations"""
    # i = 1
    # n = 100
    #path = 'C://Users/Ashton/Documents/School/SeniorDesign/scripting/'
    #i=0
    # Filenames for running the batch
    gridfile = '5-2_gridxy.txt'
    scriptname = 'sgems_script%d.py' % (i)
    batchname = 'test%d.bat' % (i)
    runname = 'testrun%d.txt' % (i)
    
    #pointset = 'testing_input.txt' # % (i) # This is now an argument THIS FKING LINE 
    
    # SGEMS variable names    
    gridname = 'gridxy%d' % (i)
    hardname = 'hardtest%d' % (i)
    propname = 'simtest%d' % (i)
    pointname = 'pointset%d' % (i)
    
    # SGEMS output data file names
    gridfile = 'gridxy.txt'
    outfile = '5-2_out%d.txt' % (i)
    


    
    # Running the batch
    fid = open(batchname,'w')
    fid.write('set GSTLAPPLIHOME=C:\\ar2gems-beta \n')
    fid.write('C:\\ar2gems-beta\\ar2gems_com.exe '+runname)
    fid.close()
    
    # writeSGEMSscript(scriptname, pointset, gridname, hardname, propname, numreal, gridfile, outfile)
    writeSGEMSscript(path,scriptname,pointset,gridname,hardname,propname,numreal,gridfile,outfile,pointname)
    
    fid = open(runname,'w')
    fid.write('RunScript '+path+scriptname) # C:/Users/Ashton/Documents/School/SeniorDesign/wip/sgems_script_wip.py')
    fid.close()
    
    os.system(batchname)
    time.sleep(2)

    # Computing weight matrix and outputting
    [x, y, varmap, datamean] = computeVARmaps(gridfile,outfile)
    [nx,ny] = np.shape(varmap)
    
    
    return nx,ny,varmap,gridfile,outfile, datamean
    #varmaps_all = np.zeros(nx,ny,n)
    #varmaps_all[:,:,i] = varmap

#batchrun(0,'C://Users/Ashton/Documents/School/SeniorDesign/scripting/','testing_input.txt')