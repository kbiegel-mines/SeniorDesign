# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:26:00 2017

@author: kbiegel
"""

""" Runs both sgems and pathing"""

# Import Libraries
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Import scripts
import Pathing
import alltogethernow


#### variables
iterations =15 #number of recycling iterations
current_x=10
current_y=0
path = 'C:/Users/Katherine/Documents/GitHub/SeniorDesign/'
input_location = 'inputs/sgems_inputs.txt'
videoclips = []
count = np.zeros((41, 41))
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
    [current_x, current_y, input_location, count] = Pathing.runPathing(n=nx, totalCount=15, current_x=current_x, current_y=current_y, gauss_data=data, data=varmap, count=count, loopCount=i)
    # Add video clip to array
    clip = VideoFileClip('VideoStitch/Pathing_%s.mp4' % i)
    videoclips.append(clip)
    
# Output a video file that shows multiple realizations
final_clip = concatenate_videoclips(videoclips)
final_clip.write_videofile("iterations_%s.mp4" % iterations)