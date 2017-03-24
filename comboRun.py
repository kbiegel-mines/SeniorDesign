# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:26:00 2017

@author: kbiegel
"""

""" Runs both sgems and pathing"""

# Import Libraries
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Import scripts
import Pathing
import alltogethernow


#### variables
iterations = 10 #number of recycling iterations
path = os.getcwd()
input_location = 'sgems_inputs.txt'
videoclips = []
# Import gauss data
dataname1 = 'GaussData.txt' #'test_fullout.txt' 
with open(dataname1) as f: 
    array = [[float(x) for x in line.split()] for line in f]
nparray = np.array(array) 
f.close()
data = nparray[:,2] 
data = data.reshape(41,41)
# Random pointsets for first iteration
file_object = open(input_location, 'w')
file_object.write('objectName \n')
file_object.write('3 \n')
file_object.write('x \n')
file_object.write('y \n')
file_object.write('gravity value \n')
for i in range(3, 6):
    file_object.write('%s %s %s \n' % (i, i, data[i][i]))
file_object.close()
    

for i in range(iterations):
    # run Sgems
    [nx,ny,varmap] = alltogethernow.batchrun(i=i,path=path,pointset=input_location)
    # Run pathing
    [current_x, current_y] = Pathing.runPathing(n=nx, totalCount=5, current_x=1, current_y=1, gauss_data=data, data=varmap, textfile=input_location, loopCount=i)
    # Add video clip to array
    clip = VideoFileClip('Pathing_%s.mp4' % i)
    videoclips.append(clip)
    
# Output a video file that shows multiple realizations
final_clip = concatenate_videoclips(videoclips)
final_clip.write_videofile("iterations_%s.mp4" % iterations)