# -*- coding: utf-8 -*-
"""
Spyder Editor

Reads in XY grid, Data realizations
Computes mean and STD for realizations
Plots average STD map 

NOTE: SGEMS saved csv files (thru gui) have a line of strings in line 1 - delete it
"""
import matplotlib.pyplot as plt
import numpy as np

#import X Y coordinates of grid
#make my_file.dat by using the sgems script 
filename = 'my_file.dat'
with open(filename) as f: # with/open/as syntax useful for files
        array1 = [[float(x) for x in line.split()] for line in f]
nparray = np.array(array1) # convert array to numpy array
f.close()

x = nparray[:,0] # x is first collumn, y is second
x = x.reshape(40,40)
y = nparray[:,1] 
y = y.reshape(40,40)


#import Data from selected property
#save the selected propery using Save Object tab in Sgems
# DELETE THE FIRST LINE OF THE SAVED FILE(strings)!!

dataname1 = 'gauss_1.txt' 
with open(dataname1) as f: 
        array = [[float(x) for x in line.split(",")] for line in f]
nparray1 = np.array(array) 
f.close()

plt.figure()
plt.pcolor(x,y,nparray1[:,0].reshape(40,40))
plt.title('Example realization for 1')
    
dataname2 = 'gauss_2.txt' 
with open(dataname2) as f: 
        array = [[float(x) for x in line.split(",")] for line in f]
nparray2 = np.array(array) 
f.close()

#plt.figure()
#plt.pcolor(x,y,nparray2[:,0].reshape(40,40))
#plt.title('Example realization for 2')

dataname3 = 'gauss_3.txt' 
with open(dataname3) as f: 
        array = [[float(x) for x in line.split(",")] for line in f]
nparray3 = np.array(array) 
f.close()

plt.figure()
plt.pcolor(x,y,nparray3[:,0].reshape(40,40))
plt.title('Example realization for 3')

dataname4 = 'gauss_4.txt' 
with open(dataname4) as f: 
        array = [[float(x) for x in line.split(",")] for line in f]
nparray4 = np.array(array) 
f.close()

plt.figure()
plt.pcolor(x,y,nparray4[:,0].reshape(40,40))
plt.title('Example realization for 4')



# Calculating mean of realizations, for STD determination
datamean1 = []
for i in range(len(nparray2[:,0])):
    datamean1.append(np.mean(nparray1[i,:]))

datamean1 = np.array(datamean1)

plt.figure()
plt.pcolor(x,y,datamean1.reshape(40,40))
plt.title('Mean for 1')


datamean2 = []
for i in range(len(nparray2[:,0])):
    datamean2.append(np.mean(nparray2[i,:]))

datamean2 = np.array(datamean2)

#plt.figure()
#plt.pcolor(x,y,datamean2.reshape(40,40))
#plt.title('Mean for 2')

datamean3 = []
for i in range(len(nparray3[:,0])):
    datamean3.append(np.mean(nparray3[i,:]))

datamean3 = np.array(datamean3)

plt.figure()
plt.pcolor(x,y,datamean3.reshape(40,40))
plt.title('Mean for 3')


datamean4 = []
for i in range(len(nparray4[:,0])):

    datamean4.append(np.mean(nparray4[i,:]))

datamean4 = np.array(datamean4)

plt.figure()
plt.pcolor(x,y,datamean4.reshape(40,40))
plt.title('Mean for 4')



# Compute STD and STDmeans
""""""
datalist1 = []
STDdata1 = []
for i in range(len(nparray1[:,0])):
        datalist1.append(nparray1[i])
        #datalist1[i] = datalist1[i].reshape(40,40)
        
        STDdata1.append(abs(datalist1[i]-datamean1[i]))
        #("data%d" %(i)) = nparray2[:,i]
STDdata1= np.array(STDdata1)

nR = len(nparray1[0,:])
nD = len(nparray1[:,0])
STDmean1 = np.zeros((nD,1))
#for i in range(len(nparray1[0,:])):
for ii in range(len(nparray1[:,0])):
    STDmean1[ii] = np.mean(STDdata1[ii,:])        
STDmean1 = STDmean1.reshape(40,40)

""""""    
datalist2 = []
STDdata2 = []
for i in range(len(nparray2[:,0])):
        datalist2.append(nparray2[i])

        
        STDdata2.append(abs(datalist2[i]-datamean2[i]))

STDdata2= np.array(STDdata2)

nR = len(nparray2[0,:])
nD = len(nparray2[:,0])
STDmean2 = np.zeros((nD,1))

for ii in range(len(nparray2[:,0])):
    STDmean2[ii] = np.mean(STDdata2[ii,:])        
STDmean2 = STDmean2.reshape(40,40)  
    
""""""
datalist3 = []
STDdata3 = []
for i in range(len(nparray3[:,0])):
        datalist3.append(nparray3[i])

        
        STDdata3.append(abs(datalist3[i]-datamean3[i]))

STDdata3= np.array(STDdata3)

nR = len(nparray3[0,:])
nD = len(nparray3[:,0])
STDmean3 = np.zeros((nD,1))
for ii in range(len(nparray3[:,0])):
    STDmean3[ii] = np.mean(STDdata3[ii,:])        
STDmean3 = STDmean3.reshape(40,40)

""""""
datalist4 = []
STDdata4 = []
for i in range(len(nparray4[:,0])):
        datalist4.append(nparray4[i])
        
        STDdata4.append(abs(datalist4[i]-datamean4[i]))
STDdata4= np.array(STDdata4)

nR = len(nparray4[0,:])
nD = len(nparray4[:,0])
STDmean4 = np.zeros((nD,1))
for ii in range(len(nparray4[:,0])):
    STDmean4[ii] = np.mean(STDdata4[ii,:])        
STDmean4 = STDmean4.reshape(40,40)


# Plot mean STD maps
plt.figure()
fig1 = plt.pcolor(x,y,STDmean1, vmin=0, vmax=1.25)
plt.colorbar(label = 'mean STD')
plt.title("mean STD for 1")

""" this data file (gauss_2) was incorrect so ignore it """
#plt.figure()
#plt.pcolor(x,y,STDmean2, vmin=0, vmax=2.0)
#plt.colorbar(label = 'mean STD')
#plt.title("mean STD for 2")

plt.figure()
plt.pcolor(x,y,STDmean3, vmin=0, vmax=1.25)
plt.colorbar(label = 'mean STD')
plt.title("mean STD for 3")

plt.figure()
plt.pcolor(x,y,STDmean4, vmin=0, vmax=1.25)
plt.colorbar(label = 'mean STD')
plt.title("mean STD for 4")

#Plotting routine for seeing each STD map
"""
for i in range(10):
    plt.figure()
    plt.pcolor(x,y,STDdata1[:,i].reshape(40,40))
"""
