# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import Libraries 
import numpy as np
from matplotlib import pyplot as plt
from random import randint

# Read in Data from File
""" 
# UNCOMMENT THIS FOR READING IN A DATA FILE TO OVERLAY
filename = 'GaussData.txt'
with open(filename) as f: # with/open/as syntax useful for files
    array = [[float(x) for x in line.split()] for line in f]

# record subsequent lines as lists of ints into a list, array
nparray = np.array(array) # convert array to numpy array
gaussX = nparray[:,0]
gaussX = gaussX.reshape(41,41)
gaussY = nparray[:,1]
gaussY = gaussY.reshape(41,41)
gaussG = nparray[:,2]
gaussG = gaussG.reshape(41,41)
f.close()
"""

# Setting Variables
n=9 # set n to be the maximum value on the grid (ie x=[0,1,2,3,4,5,6,7,8,9] -> n=9)

#Create grid
x = np.arange(0,n+1,1)
y = np.arange(0,n+1,1)
grid = np.meshgrid(x,y)
start = 0

# Plotting Parameters
plt.scatter(grid[0],grid[1])
plt.axis([0,n,0,n])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.scatter(grid[0][start][start],grid[1][start][start])
plt.axis([0,n,0,n])
plt.savefig('Startingpoint.png',format='png')

fig = plt.figure()
plot = plt.scatter([],[])
plt.axis([0,n,0,n])

array = plot.get_offsets()

m=0
for j in range(10):

    for i in range(10):

        #if i != 0:
        #    if i%10 == 0:
        #        counter += 1
        currentx = i
        
        if j%2 != 0:
            currentx = 9-i
        else:
            currentx = i
        currenty = j
        #print(currenty)
        #print(j)
        point = (currentx,currenty)
        array = np.append(array,point)
        plot.set_offsets(array)
        m = 10*j+i
        #print(n)
        plt.savefig(('img%02d.png' % m),format='png')
        #plot = plt.scatter(grid[0][currentx][currenty],grid[1][currentx][currenty])
        fig.canvas.draw()
        
""" VIDEO IMPORTING AND EXPORTING NEEDS ADDITIONAL PACKAGE: import cv2 (or imageio) """

#%%  BUG FREE FOR FIRST DIRECTION...
# Attempting to use spiral formulation 
# Function for finding the first direction
def firstdirection(prox1,prox2,big1,big2):   
    # initialize Dir1 and done(bool)
    Dir1 = 99
    done = True
    if prox1==0 & done:
        if big1==True & done:
            if big2==True & done:
                Dir1=1
                done=False
            elif big2==False & done:
                Dir1=3
                done=False
        elif big1==False & done:
            if big2==True & done:
                Dir1=1
                done=False
            elif big2==False & done:
                Dir1=3
                done=False
    if prox2==0 & done:
        if big2==True & done:
            if big1==True & done:
                Dir1=0
                done=False
            elif big1==False & done:
                Dir1=2
                done=False
        elif big2==False & done:
            if big1==True & done:
                Dir1=0
                done=False
            elif big1==False & done:
                Dir1=2
                done=False
    if (prox1 <prox2) & done:
        if (big1==True) & (big2==True) & done:
            Dir1=0
            done=False
        elif (big1==True) & (big2==False) & done:
            Dir1=0
            done=False
        elif (big1==False) & (big2==True) & done:
            Dir1=2
            done=False
        elif (big1==False) & (big2==False) & done:
            Dir1=2
            done=False
    elif (prox2 < prox1) & done:
        if (big2==True) & (big1==True) & done:
            Dir1=1
            done=False
        elif (big2==True) & (big1==False) & done:
            Dir1=1
            done=False
        elif (big2==False) & (big1==True) & done:
            Dir1=3
            done=False
        elif (big2==False) & (big1==False) & done:
            Dir1=3
            done=False
    elif (prox1==prox2) & done:
        if (big1==True) & (big2==True) & done:
            Dir1=1
            done=False
        elif (big1==True) & (big2==False) & done:
            Dir1=3
            done=False
        elif (big1==False) & (big2==True) & done:
            Dir1=1
            done=False
        elif (big1==False) & (big2==False) & done:
            Dir1=3
            done=False
    return Dir1

# Function for switching directions (always turns right)
def switchdirections(Dir):
    if Dir==0:
        NewDir = 3
        return NewDir
    elif Dir==1:
        NewDir = 0
        return NewDir
    elif Dir==2:
        NewDir = 1
        return NewDir
    elif Dir==3:
        NewDir = 2
        return NewDir


# PICK STARTING POINT
n=9
startingpoint2 = (randint(0,n),randint(0,n))
#directions = [0,1,2,3]
p1 = startingpoint2[0]
p2 = startingpoint2[1]
p1inv = n-p1
p2inv = n-p2
if p1 > p1inv:
    prox1=p1inv
    big1=True
else:
    prox1=p1
    big1=False

if p2>p2inv:
    prox2=p2inv
    big2=True
else:
    prox2=p2
    big2=False

# Initialize plot, get offsets array, and set starting point to offsets

plt.ion()
    
firstswitch = False
for i in range(0,(n+1)*(n+1)):
    if i == 0:
        fig2 = plt.figure()
        plot2 = plt.scatter([],[])
        plt.axis([0,n,0,n])
    
        array = plot2.get_offsets()
    
        array = np.append(array,startingpoint2)
        plot2.set_offsets(array)
    
        fig2.canvas.draw()
        
        Dir1 = firstdirection(prox1,prox2,big1,big2)
        
        xo = startingpoint2[0]
        yo = startingpoint2[1]

        xlast = xo
        ylast = yo
        Dir = Dir1
    
    xmin = False
    xmax = False
    ymin = False
    ymax = False
    # check edges 
    if xlast == 0:
        xmin = True
    elif xlast == n:
        xmax = True
    if ylast == 0:
        ymin = True
    elif ylast == n:
        ymax = True

    if ((xmin==True) or (xmax==True) or (ymin==True) or (ymax==True)) & (not firstswitch):
        Dir = switchdirections(Dir)
        firstswitch=True
    
    if (xmin==True) & (ymin==True) & firstswitch:
        Dir = switchdirections(Dir)

    elif (xmin==True) & (ymax==True) & firstswitch:
        Dir = switchdirections(Dir)

    elif (xmax==True) & (ymin==True) & firstswitch:
        Dir = switchdirections(Dir)

    elif (xmax==True) & (ymax==True) & firstswitch:
        Dir = switchdirections(Dir)

#    elif (xmin==True):
#        if (ymin==True) or (ymax==True):
#            Dir = switchdirections(Dir)
#
#    elif (xmax==True):
#        Dir = switchdirections(Dir)
#
#    elif (ymin==True):
#        Dir = switchdirections(Dir)
#
#    elif (ymax==True):
#        Dir = switchdirections(Dir)

    
    #check direction
    if Dir==0:
        x = xlast+1
        y = ylast
    elif Dir==1:
        x = xlast
        y = ylast+1
    elif Dir==2:
        x = xlast-1
        y = ylast
    elif Dir==3:
        x = xlast
        y = ylast-1
    
    nextpoint = (x,y)
    array = plot2.get_offsets()
    array = np.append(array,nextpoint)
    plot2.set_offsets(array)
    fig2.canvas.draw()
    plt.show()
    #plt.savefig(('img%02d.png' % m),format='png')
    xlast = x
    ylast = y
    
for i in range(len(array)):
    fig2 = plt.figure()
    plot2 = plt.scatter([],[])
    plt.axis([0,n,0,n])
    
    plt.hold(True)
    plot2.set_offsets(array[i,:])
    fig2.canvas.draw()



#%%


"""
# EARLIER ATTEMPT AT CHOOSING STARTING DIRECTION... Doesn't work as intended.
for i in range(100):
    prox1 = startingpoint2[0]
    prox2 = startingpoint2[1]
    if prox1==prox2:
        if prox1==0:
            dir1 = directions[0]
        elif prox1==9:
            dir1 = directions[2]
        elif prox1<=4:
            dir1 = directions[2]
        elif prox1>=5:
            dir1 = directions[0]
    elif prox1<prox2:
        if prox1==0:
            if prox2==9:
                dir1 = directions[2]
            elif prox2<=4:
                dir1 = directions[2]
            elif prox2>=5:
                dir1 = directions[0]
                
        elif prox1==9:
            if prox2<=4:
                dir1 = directions[2]
            elif prox2>=5:
                dir1 = directions[0]
        elif prox1<=4: # NEED WORK FROM HERE
            dir1 = directions[1]
        elif prox1>=5:
            dir1 = directions[3]
    elif prox1>prox2:
        if prox2==0:
            if prox1==9:
                dir1 = directions[1]
            elif prox1<=4:
                dir1 = directions[1]
            elif prox1>=5:
                dir1 = directions[3]
        elif prox2==9:
            if prox1<=4:
                dir1 = directions[1]
            elif prox1>=5:
                dir1 = directions[3]
        elif prox2<=4: # AND HERE
            dir1 = directions[2]
        elif prox2>=5:
            dir1 = directions[0]
            
            """
    
    
