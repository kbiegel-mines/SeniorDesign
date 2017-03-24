# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:44:16 2017
@author: Katherine
"""

# Import Libraries
import numpy as np
from matplotlib import pyplot as plt
import math
from moviepy.editor import ImageSequenceClip
#import random


def createDistance(x, y, distance, n):
    """ Function takes in an x and y value (int) and a distance array (np) and
    fills distance array with the physical distance each point is from the current
    point.  Current points set at 1000 to prevent double counting."""
    for i in range(0, n):
        for j in range(0, n):
            distance[i][j] = math.sqrt((x-i)**2 + (y-j)**2)
    
    distance[x][y] = 10000000
            
    return distance

def totalWeighting(distance, count, data, n):
    """Function takes in three weighting arrays for distance, the number of 
    times each point has been surveyed, and the geo-data.  Function then 
    returns a total weighting array that is calculated using the RMS of the 
    other arrays.  The way this is calculated could be changed later."""
    
    weighting = np.zeros((n, n))
    inverseData = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if data[i][j]==0:
                inverseData[i][j] = 1./0.0001
            else:
                inverseData[i][j] = 1./float(data[i][j]) 
    weighting = np.sqrt(distance**2 + (10*count)**2 + inverseData**2)
    #weighting = np.sqrt(distance**2 + count**2)
    
    return weighting

def newPoint(x, y, weighting, n):
    """Function takes an x and y location (int) and the weighting array.  Finds
    the point with the minimum weighting and then find the point closest to the
    current point to move to."""
    closest = np.argmin(weighting)
    closest_tuple = np.unravel_index(closest, (n, n))
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


def runPathing(n, totalCount, current_x, current_y, gauss_data, data, count, loopCount=1):
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
    print(gauss_data.tolist())
    print(n)
    #Create grids and arrays
    x = np.arange(0, n, 1)
    y = np.arange(0, n, 1)
    grid = np.meshgrid(x, y)
    distance = np.zeros((n, n))
    #data = np.ones((n+1, n+1))
    #for i in range(2,5):
    #    for j in range(2,5):
    #        data[i][j] = 10
    #data = np.random.random_integers(1, 5, (n+1, n+1))
    images = []
    textfile = 'inputs/sgems_inputs_%i.txt' % loopCount
    
    # Plotting Parameters
    plt.contourf(data, cmap='coolwarm')
    plt.scatter(grid[0], grid[1])
    plt.axis([0, n-1, 0, n-1])
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    
    current = 1
    print(current)
    
    # Plot first point and save image
    plt.contourf(data, cmap='coolwarm')
    plt.scatter(grid[0][current_x][current_y], grid[1][current_x][current_y])
    path = 'images/img%02d.png' % current
    plt.savefig(path, format='png')
    
    # Mark first point as visited
    count[current_x][current_y] = 10
    
    # Ready plot for inside if statement
    fig = plt.figure()
    plt.contourf(data, cmap='coolwarm')
    plot = plt.scatter([], [])
    plt.axis([0, n-1, 0, n-1])
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    
    array = plot.get_offsets()
    
    # Start text file
    file_object = open(textfile, 'w')
    file_object.write('objectName \n')
    file_object.write('3 \n')
    file_object.write('x \n')
    file_object.write('y \n')
    file_object.write('gravity value \n')
    file_object.close()
    
    # For statement looping through all points
    for i in range(current+1, totalCount):
        distance = createDistance(current_x, current_y, distance, n)
        weight = totalWeighting(distance, count, data, n)
        current_x, current_y = newPoint(current_x, current_y, weight, n)
        
        # plot new point and save image
        point = (current_x, current_y)
        array = np.append(array, point)
        plot.set_offsets(array)
        path = 'images/img%02d.png' % i
        plt.savefig(path, format='png')
        fig.canvas.draw()
    
        images.append(path)
    
        # mark point as visited
        count[current_x][current_y] = count[current_x][current_y]+10
    
        # Add point to file object
        file_object = open(textfile, 'a')
        file_object.write('%s %s %s \n' % (current_x, current_y, gauss_data[current_x][current_y]))
        file_object.close()
    
    # Make Movie
    multiclip = ImageSequenceClip(images, fps=3)
    multiclip.write_videofile('VideoStitch/Pathing_%s.mp4' % loopCount, audio=False)
    
    print(current_x)
    print(current_y)
    #print(weight.tolist())
    #print(distance.tolist())
    #print(count.tolist())
    print(weight[7][16])
    print(distance[7][16])
    print(count[7][16])
    print(current)
    
    # Return last point measured
    return current_x, current_y, textfile, count