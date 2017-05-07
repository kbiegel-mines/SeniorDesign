# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:17:29 2017

@author: Katherine
"""

"""
Script creates videos within the comborun framework using what was returned from previous
functions.  This script requires intallation of both moviepy and ffmpeg.
"""

#import libraries
#import moviepy.editor as mp
from matplotlib import pyplot as plt
import numpy as np
import sys
#from PIL import Image
import matplotlib as mpl


def createVideos(points, datamean, n, count, iterations, data, var, SSX, SSY):
    """
    Points is an ndarray that contains the points added in the pathing function
    var is the variancemaps returned from sGEMs
    mean is the datamean returned from sGEMs
    n is the dimension of the grid
    """

    counter = 0
    images = []
    mean = []
    dataarr = []
    levels = [0.0, 0.5, 1.0, 1.5, 2.0]

    for i in range(0,iterations):
        fig = plt.figure()
        plt.axis([0, n, 0, n])
        plt.contourf(var[:,:,i], cmap='coolwarm', vmin=0, vmax=2)
        #plt.colorbar(ticks=levels, vmin=0., vmax=2.)
        plot = plt.scatter([], [])

        maxi = np.argmax(var[:,:,i])
        maxi_tuple = np.unravel_index(maxi, (n+1, n+1))
        ymax, xmax = maxi_tuple
        plt.scatter(xmax,ymax)

        plt.scatter(SSX,SSY)
        
        plt.axis([0, n, 0, n])
        
        for j in range(0,count):
            plot = plt.scatter([], [])
            plot.set_offsets(points[0:counter,:])
            plt.plot(points[0:counter,0], points[0:counter,1])
            
            plt.title('Data var map')
            path2 = 'images/img%i%d.png' % (i,j)
            plt.savefig(path, format='png')
            counter = int(counter+1)
            images.append(path2)
        
        plt.colorbar()
        plt.close()


    for i in range(0,iterations):
        fig = plt.figure()
        plt.axis([0, n, 0, n])
        plt.contourf(datamean[:,:,i], vmin=0., vmax=2.0, extend='max', cmap='coolwarm')
        plt.colorbar()
        
        for j in range(0,count):
            plot = plt.scatter([], [])
            plot.set_offsets(points[0:counter,:])
            plt.plot(points[0:counter,0], points[0:counter,1])
            
            plt.title('Data mean map - 20 realizations')
            path = 'mean/img%i%d.png' % (i,j)
            plt.savefig(path, format='png')
            counter = counter+1
            mean.append(path)
        
        plt.close()
            
    counter = 0
    data_new = np.zeros((n+1,n+1))
    for i in range(0,iterations):        
        for j in range(0,count):
            fig = plt.figure()
            plt.axis([0, n, 0, n])
            data_new[points[counter,0], points[counter,1]] = data[points[counter,0], points[counter,1]]
            #plot = plt.scatter([], [])
            plt.contourf(data_new, vmin=0., vmax=2.0, extend='max', cmap='coolwarm')
            plt.colorbar()
            #plot.set_offsets(points[0:counter,:])
            #plt.plot(points[0:counter,0], points[0:counter,1])
            
            plt.title('Data update')
            path3 = 'data/img%i%d.png' % (i,j)
            plt.savefig(path3, format='png')
            plt.close()
            counter = counter+1
            dataarr.append(path3)
    
#    combined = []
#    for i in range(0, counter):
#        photos = map(Image.open, [images[i], dataarr[i]])
#        widths, heights = zip(*(j.size for j in photos))
#
#        total_width = sum(widths)
#        max_height = max(heights)
#
#        path4 = 'combined/img%i.png' % i
#        new_im = Image.new('RGB', (total_width, max_height))
#
#        x_offset = 0
#        for im in photos:
#            new_im.paste(im, (x_offset,0))
#            x_offset += im.size[0]
#
#            new_im.save(path4)
#            combined.append(path4)
#  
            
    ## Add video clip to array
    #clip = mp.ImageSequenceClip(images, fps=3)
    #clip2 = mp.ImageSequenceClip(mean, fps=3)
    #clip3 = mp.ImageSequenceClip(dataarr, fps=3)
    #clip4 = mp.ImageSequenceClip(combined, fps=3)
    #clip.write_videofile('Images.mp4', audio=False)
    #clip2.write_videofile('Mean.mp4', audio=False)
    #clip3.write_videofile('Data.mp4', audio=False)
    #clip4.write_videofile('Combined.mp4', audio=False)
    
    #clip4 = mp.VideoFileClip('Images.mp4')
    #clip4.resize(0.5)
    #clip5 = mp.VideoFileClip('Data.mp4')
    #clip5.resize(0.5)
    
    #video = mp.CompositeVideoClip([clip4,clip5.set_pos((700,0))])
    #video.resize(0.5)
    #video.write_videofile('Combined.mp4')
