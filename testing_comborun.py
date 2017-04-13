# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:26:00 2017
@author: kbiegel
"""

""" Runs both sgems and pathing"""

# Import Libraries
import numpy as np
#from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from matplotlib import pyplot as plt
# Import scripts
import testing_pathing
import testing_alltogethernow


#### variables
iterations = 50 #number of recycling iterations
#path = os.getcwd()+'\''
"""
Path derived from os.getcwd() doesnt interact well with sgems 
(sgems uses forward slashes)
"""
path = 'C://Users/Ashton/Documents/School/SeniorDesign/scripting/'
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
n = 40
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
    
current_x=5
current_y=5
totalCount = 1
count = np.ones((n+1, n+1))
count[current_x][current_y] = 0
array = []
varmaps = np.zeros((41,41,iterations))

for i in range(iterations):
    # run Sgems
    [nx,ny,varmaps[:,:,i],gridfile] = testing_alltogethernow.batchrun(i,path,pointset=input_location)
    # Run pathing
    
    [current_x, current_y,count,array,weight] = testing_pathing.runPathing(gridfile, array, n, totalCount, current_x, current_y, count, gauss_data=data, data=varmaps[:,:,i], textfile=input_location, loopCount=i)
    # Add video clip to array
    #clip = VideoFileClip('Pathing_%s.mp4' % i)
    #videoclips.append(clip)
    
# Output a video file that shows multiple realizations
#final_clip = concatenate_videoclips(videoclips)
#final_clip.write_videofile("iterations_%s.mp4" % iterations)
plt.contourf(abs(varmaps[:,:,9]-varmaps[:,:,0]),cmap='coolwarm',vmin=0,vmax=2)
plt.colorbar()
for i in range(iterations):
    
    plt.hold('on')
    plt.scatter(array[i][0],array[i][1])