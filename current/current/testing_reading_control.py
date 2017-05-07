# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:25:29 2017
@author: Ashton
"""

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# This script accepts a grid file (my_file.dat) and a data file (containing N
# realizations for a single hard data set), and computes the variance map to be
# used for pathing weights.
def computeVARmaps(gridfile,outfile):
        
    # Import X Y coordinates of grid
    filename = gridfile #'my_file.dat'
    with open(filename,'r') as f: # with/open/as syntax useful for files
            array1 = [[float(x) for x in line.split()] for line in f]
    nparray = np.array(array1) # convert array to numpy array
    f.close()
    
    x = nparray[:,0] # x is first collumn, y is second
    x = x.reshape(41,41)
    y = nparray[:,1] 
    y = y.reshape(41,41)
    
    #%% Importing data file
    #dataname1 = outfile #'test_fullout.txt' 
    with open(outfile,'r') as f: 
            array = [[float(x) for x in line.split()] for line in f]
    nparray1 = np.array(array) 
    f.close()
    
    """
    plt.figure()
    plt.pcolor(x,y,nparray1[:,0].reshape(40,40))
    plt.title('Example realization for 1')
    """
    #%% Computing mean of realizations
    datamean1 = []
    for i in range(len(nparray1[:,0])):
        datamean1.append(np.mean(nparray1[i,:]))
    
    datamean1 = np.array(datamean1)
    datamean2 = datamean1.reshape(41,41)
    
    #plt.figure()
    #plt.contourf(datamean1.reshape(41,41), cmap='coolwarm')
    #plt.title('Mean')
    #path = 'mean/image%i.png' % j
    #plt.savefig(path, format='png')
    
    #%% Calculating variances
    datalist1 = []
    STDdata1 = []
    for i in range(len(nparray1[:,0])):
            datalist1.append(nparray1[i])
            #datalist1[i] = datalist1[i].reshape(40,40)
            
            STDdata1.append((datalist1[i]-datamean1[i])*(datalist1[i]-datamean1[i]))
            # variance as square of residual
            #("data%d" %(i)) = nparray2[:,i]
    STDdata1= np.array(STDdata1)
    
    nR = len(nparray1[0,:])
    nD = len(nparray1[:,0])
    varmap1 = np.zeros((nD,1))
    #for i in range(len(nparray1[0,:])):
    for ii in range(len(nparray1[:,0])):
        varmap1[ii] = np.mean(STDdata1[ii,:])        
    varmap1 = varmap1.reshape(41,41)
    

    # Normalize to a PDF (for combining with other weights)
    varmap1_pdf = varmap1/(np.sum(np.sum(varmap1)))
    
    
    #%% Plotting variance map
    #plt.figure()
    #fig1 = plt.pcolor(x,y,varmap1_pdf, vmin=0, vmax=np.max(varmap1_pdf))
    #plt.colorbar(label = 'variance')
    #plt.title("variance map from input realizations")
    #plt.xlabel('x (m)')
    #plt.ylabel('y (m)')

    return x,y,varmap1, datamean2