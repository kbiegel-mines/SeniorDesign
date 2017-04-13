# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:44:16 2017
@author: Katherine
"""

# Import Libraries
import numpy as np
from matplotlib import pyplot as plt
import math
#from moviepy.editor import ImageSequenceClip
#import random


def createDistance(x, y, distance, n):
    """ Function takes in an x and y value (int) and a distance array (np) and
    fills distance array with the physical distance each point is from the current
    point.  Current points set at 1000 to prevent double counting."""
    for i in range(0, n+1):
        for j in range(0, n+1):
            if (math.sqrt((x-i)**2 + (y-j)**2))<= 3.5:
                distance[i][j] = 1
            else: 
                distance[i][j] = 1
    
    distance[x][y] = 0
    #distance = float(distance/(np.sum(np.sum(distance))))
            
    return distance

def totalWeighting(distance, count, data, n):
    """Function takes in three weighting arrays for distance, the number of 
    times each point has been surveyed, and the geo-data.  Function then 
    returns a total weighting array that is calculated using the RMS of the 
    other arrays.  The way this is calculated could be changed later."""
    
    weighting = np.zeros((n+1, n+1))
    #inverseData = np.zeros((n+1, n+1))
    #for i in range(0, n+1):
    #    for j in range(0, n+1):
    #        inverseData[i][j] = float(data[i][j]) 
    
    #weighting = (np.sqrt(distance**2 + (data)**2))*count
    weighting = (data)*(distance)*count
    weighting = weighting/(np.sum(np.sum(weighting)))
    #weighting = np.sqrt(distance**2 + count**2)
    
    return weighting

def newPoint(x, y, weighting, n):
    """Function takes an x and y location (int) and the weighting array.  Finds
    the point with the minimum weighting and then find the point closest to the
    current point to move to."""

    closest = np.argmax(weighting)
    closest_tuple = np.unravel_index(closest, (n+1, n+1))
    closestX, closestY = closest_tuple
    
    # Set x value
    if closestX == x:
        x = closestX
    elif closestX >= x+1:
        x = x+1
    elif closestX <= x-1:
        x = x-1

    # Set y value
    if closestY == y:
        y = closestY
    elif closestY >= y+1:
        y = y+1
    elif closestY <= y-1:
        y = y-1
    
    return x,y
    """
    i,j = np.unravel_index(weighting.argmax(),weighting.shape)
    return i,j
"""

def runPathing(gridfile, array, n, totalCount, current_x, current_y, count, gauss_data, data, textfile, loopCount=1):
    """Function that runs pathing outside of script allowing combination with
    sgems function.
    n = integer, grid size, set to maximum grid value
    totalCount = integer, number of points to be surveyed,
    current_x = integer, starting x location
    current_y = integer, starting y location
    gauss_data = numpy array, actual gravity data ### edit to become user input at some point ####
    data = np object, variable map
    textfile = string, sGemsinput file location
    loopCount = integer, how many times you want to loop through sgems/pathing,
                default value of 1 for a singular run through script"""
    filename = gridfile #'my_file.dat'
    with open(filename) as f: # with/open/as syntax useful for files
            array1 = [[float(x) for x in line.split()] for line in f]
    nparray = np.array(array1) # convert array to numpy array
    f.close()
    
    x = nparray[:,0] # x is first collumn, y is second
    x = x.reshape(41,41)
    y = nparray[:,1] 
    y = y.reshape(41,41)
    
    #Create grids and arrays
#    x = np.arange(0, n+1, 1)
#    y = np.arange(0, n+1, 1)
#    grid = np.meshgrid(x, y)

    distance = np.zeros((n+1, n+1))
    #data = np.ones((n+1, n+1))
    #for i in range(2,5):
    #    for j in range(2,5):
    #        data[i][j] = 10
    #data = np.random.random_integers(1, 5, (n+1, n+1))
    #images = []
    
    # Plotting Parameters
#    plt.contourf(data, cmap='coolwarm')
##    plt.scatter(grid[0], grid[1])
#    plt.axis([0, n, 0, n])
#    plt.xlabel('x (m)')
#    plt.ylabel('y (m)')
    
    current = 1
    
    # Plot first point and save image
#    plt.contourf(data, cmap='coolwarm')
#    plt.scatter(grid[0][current_x][current_y], grid[1][current_x][current_y])
    #path = 'images/img%02d.png' % current
    #plt.savefig(path, format='png')
    #images.append(path)
    
    # Mark first point as visited

    
    # Ready plot for inside if statement
    fig = plt.figure()
    plt.contourf(data, cmap='coolwarm',vmin=0,vmax=2)
    plt.colorbar()
    plot = plt.scatter([], [])
    
    #plot point of max variance
    maxi = np.argmax(data)
    maxi_tuple = np.unravel_index(maxi, (n+1, n+1))
    ymax, xmax = maxi_tuple
    plot1 = plt.scatter(xmax,ymax)
    
    plt.axis([0, n, 0, n])
    
    #array = plot.get_offsets()
    
    # Start text file
#    file_object = open(textfile, 'w')
#    file_object.write('objectName \n')
#    file_object.write('3 \n')
#    file_object.write('x \n')
#    file_object.write('y \n')
#    file_object.write('gravity \n')
#    file_object.close()
    
    # For statement looping through all points
    #for i in range(current+1, totalCount):
    distance = createDistance(current_x, current_y, distance, n)
    weight = totalWeighting(distance, count, data, n)
    current_x, current_y = newPoint(current_x, current_y, weight, n)
    
    # plot new point and save image
    point = (current_y, current_x)
    array = np.append(array, point)
    plot.set_offsets(array)
    #path = 'images/img%02d.png' % i
    #plt.savefig(path, format='png')
    #fig.canvas.draw()

    #images.append(path)

    # mark point as visited
    count[current_x][current_y] = 0

    # Add point to file object
    file_object = open(textfile, 'a')
    file_object.write('%s %s %s \n' % (x[current_x][current_y], y[current_x][current_y], gauss_data[current_x][current_y]))
    file_object.close()
    
    # Make Movie
    #multiclip = ImageSequenceClip(images, fps=3)
    #multiclip.write_videofile('Pathing_%s.mp4' % loopCount, audio=False)
    
    # Return last point measured
    return current_x, current_y, count, array, weight