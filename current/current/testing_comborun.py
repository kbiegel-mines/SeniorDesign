# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:25:08 2017

@author: Ashton
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:26:00 2017
@author: kbiegel
"""

""" Runs both sgems and pathing"""

# Import Libraries
import numpy as np
import os
from matplotlib import pyplot as plt
import time
# Import scripts
import testing_pathing as pathing
import testing_alltogethernow as batch
import videoScript as videos

""" change these"""
iterations = 3 #number of recycling iterations
#path = 'C://Users/Ashton/Documents/School/SeniorDesign/scripting/' # path to WD
path = 'C://Users/Katherine/Documents/GitHub/SeniorDesign/current/current/'
numreal = '3' # number of realizations (needs to be string b/c sgems)
totalCount = 3 # number of points to path at each iteration (keep small)
current_x=5
current_y=5
n = 40

#path = os.getcwd()+'\''
"""
Path derived from os.getcwd() doesnt interact well with sgems 
(sgems uses forward slashes)  <-- ** THIS WOULD PROBABLY WORK WITH AR2GEMS **
"""

input_location = 'sgems_inputs.txt'
videoclips = []
# Import gauss data
dataname1 = 'GaussData_rev409.txt' #'test_fullout.txt' 
with open(dataname1) as f: 
    array = [[float(x) for x in line.split()] for line in f]
nparray = np.array(array) 
f.close()
xx = nparray[:,0]
xx = xx.reshape(41,41)
yy = nparray[:,1]
yy = yy.reshape(41,41)
data = nparray[:,2] 
data = data.reshape(n+1,n+1)
# Random pointsets for first iteration
file_object = open(input_location, 'w')
file_object.write('objectName \n')
file_object.write('3 \n')
file_object.write('x \n')
file_object.write('y \n')
file_object.write('gravity value \n')
for i in range(3, 6):
    for j in range(3,6):
        file_object.write('%s %s %s \n' % (xx[i][j], yy[i][j], data[i][j]))
file_object.close()

count = np.ones((n+1, n+1))
count[current_x][current_y] = 0
array = []
varmaps = np.zeros((41,41,iterations))
datamean = np.zeros((41,41,iterations))

for i in range(iterations):
    # run Sgems
    [nx,ny,varmaps[:,:,i],gridfile,outfile,datamean[:,:,i]] = batch.batchrun(i,path,numreal,pointset=input_location)
    #time.sleep(2)
    # Run pathing
    [current_x, current_y,count,array,weight] = pathing.runPathing(gridfile, array, n, totalCount, current_x, current_y, count, gauss_data=data, data=varmaps[:,:,i], textfile=input_location, loopCount=i)
    #time.sleep(2)
    
videos.createVideos(array, datamean, n, totalCount, iterations, data)
#plt.contourf(abs(varmaps[:,:,9]-varmaps[:,:,0]),cmap='coolwarm',vmin=0,vmax=2)
#plt.colorbar()
#for i in range(iterations*totalCount):
    
#    plt.hold('on')
#    plt.scatter(array[i][0],array[i][1])