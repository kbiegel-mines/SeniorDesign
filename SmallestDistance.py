# -*- coding: utf-8 -*-
"""
@author: Katherine
"""

# Import Libraries
import numpy as np
from matplotlib import pyplot as plt
import math
from moviepy.editor import ImageSequenceClip

# Setting Variables
n = 10  # set n to be the maximum value on the grid (ie x=[0,1,2,3,4,5,6,7,8,9] -> n=9)
totalCount = 120  # total number of points to be surveyed
nearestNeighbors = 8  # 8 for a square grid (depends on shape but not sure how to incorporate)

#Create grid
x = np.arange(0, n+1, 1)
y = np.arange(0, n+1, 1)
grid = np.meshgrid(x, y)
compare = np.zeros((n+1, n+1))

# Starting Point
currentx = 3
currenty = 6
count = 1
images = []

# Plotting Parameters
plt.scatter(grid[0], grid[1])
plt.axis([0, n, 0, n])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis([0, n, 0, n])

# Plot first point and save image
plt.scatter(grid[0][currentx][currenty], grid[1][currentx][currenty])
path = 'images/img%02d.png' % count
plt.savefig(path, format='png')
images.append(path)

# Mark first point as visited
compare[currentx][currenty] = 1

# Ready plot for inside if statement
fig = plt.figure()
plot = plt.scatter([], [])
plt.axis([0, n, 0, n])

array = plot.get_offsets()


def smallestDistance(x, y, nearestNeighbors, compare):
    """ Function takes in an x and y value and the number of nearest neighbors
    to a specific point (8 for a square grid) and the compare grid which houses
    a binary yes or no for point visited and returns an x and y location
    of smallest distance and smallest cost distance"""

    # 2D Array to store weighted distance of each point from current
    distance = np.zeros((8, 1))

    # set distances (1000 used for boarders, 2 used for already measured,
    # sqrt(2) used for diagonals, 1 used for straight lines)
    if x-1 >= 0:
        # position 0
        if y+1 <= n:
            if compare[x-1][y+1] == 0:
                distance[0] = math.sqrt(2)
            else:
                distance[0] = 2
        else:
            distance[0] = 1000
        #position 3
        if compare[x-1][y] == 1:
            distance[3] = 2
        else:
            distance[3] = 1
        #position 5
        if currenty-1 >= 0:
            if compare[x-1][y-1] == 0:
                distance[5] = math.sqrt(2)
            else:
                distance[5] = 2
        else:
            distance[5] = 1000
    else:
        distance[0] = 1000
        distance[3] = 1000
        distance[5] = 1000

    if x+1 <= n:
        # position 2
        if y+1 <= n:
            if compare[x+1][y+1] == 0:
                distance[2] = math.sqrt(2)
            else:
                distance[2] = 2
        else:
            distance[2] = 1000
        #position 4
        if compare[x+1][y] == 1:
            distance[4] = 2
        else:
            distance[4] = 1
        #position 7
        if currenty-1 >= 0:
            if compare[x+1][y-1] == 0:
                distance[7] = math.sqrt(2)
            else:
                distance[7] = 2
        else:
            distance[7] = 1000
    else:
        distance[2] = 1000
        distance[4] = 1000
        distance[7] = 1000

    # position 1
    if y+1 >= n:
        distance[1] = 1000
    elif compare[x][y+1] == 1:
        distance[1] = 2
    else:
        distance[1] = 1

    # position 6
    if currenty-1 <= 0:
        distance[6] = 1000
    elif compare[x][y-1] == 1:
        distance[6] = 2
    else:
        distance[6] = 1

    # find minimum distance and choose random from minimums
    closestPos = np.argmin(distance)

    # set new x and y
    if closestPos == 0:
        newx = x-1
        newy = y+1
    elif closestPos == 1:
        newx = x
        newy = y+1
    elif closestPos == 2:
        newx = x+1
        newy = y+1
    elif closestPos == 3:
        newx = x-1
        newy = y
    elif closestPos == 4:
        newx = x+1
        newy = y
    elif closestPos == 5:
        newx = x-1
        newy = y-1
    elif closestPos == 6:
        newx = x
        newy = y-1
    elif closestPos == 7:
        newx = x+1
        newy = x-1
    else:
        print('Minimum distance function error')

    return newx, newy


# For statement looping through all points
for i in range(count+1, totalCount):
    currentx, currenty = smallestDistance(currentx, currenty, nearestNeighbors, compare)

    # plot new point and save image
    point = (currentx, currenty)
    array = np.append(array, point)
    plot.set_offsets(array)
    path = 'images/img%02d.png' % i
    plt.savefig(path, format='png')
    fig.canvas.draw()

    images.append(path)

    # mark point as visited
    compare[currentx][currenty] = 1


# Make Movie
multiclip = ImageSequenceClip(images, fps=4)
multiclip.write_videofile('Pathing.mp4', audio=False)
            