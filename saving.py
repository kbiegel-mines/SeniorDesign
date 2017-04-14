import sgems

gauss1_0 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real0')

gauss1_1 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real1')

gauss1_2 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real2')

gauss1_3 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real3')

gauss1_4 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real4')

gauss1_5 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real5')

gauss1_6 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real6')

gauss1_7 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real8')

gauss1_8 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real7')

gauss1_9 = sgems.get_property('gauss','gaussSGSIM1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0__real9')

filename = 'test1.dat'
f = open(filename, 'w')

separator = ","


print(gauss1_9[1599])


for i in range(len(gauss1_0)) : 

	f.write(str(gauss1_0[i])+separator+str(gauss1_1[i])+separator+str(gauss1_2[i])+separator+str(gauss1_3[i])+separator+str(gauss1_4[i])+separator+str(gauss1_5[i])+separator+str(gauss1_6[i])+separator+str(gauss1_7[i])+separator+str(gauss1_8[i])+separator+str(gauss1_9[i])+separator+"\n")


print(gauss1_9[i])
f.close()

#for i0,i1,i2,i3,i4,i5,i6,i7,i8,i9 in zip(gauss1_0,gauss1_1,gauss1_2,gauss1_3,gauss1_4,gauss1_5,gauss1_6,gauss1_7,gauss1_8,gauss1_9) : 


	#fid.write(str(i0)+separator+str(i1)+separator+str(i2)+separator+str(i3)+separator+str(i4)+separator+str(i5)+separator+str(i6)+separator+str(i7)+separator+str(i8)+separator+str(i9)+separator+"\n")

#fid.close()

