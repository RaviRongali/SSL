import numpy as np
from numpy.core.multiarray import concatenate

a = np.genfromtxt('info_day.csv', delimiter=',', dtype=None, encoding='ascii').astype(object) 
b = np.genfromtxt('info_night.csv', delimiter=',', dtype=None, encoding='ascii').astype(object)
a[0][1] = 'Temperature(Day)'
b[0][1] = 'Temperature(Night)'
a[0][2] = 'Humidity(Day)'
b[0][2] = 'Humidity(Night)'
a[0][3] = 'Light(Day)'
b[0][3] = 'Light(Night)'
a[0][4] = 'CO2(Day)'
b[0][4] = 'CO2(Night)'
c = concatenate((a, b), axis=1)  
my_permutation = [0,2,4,6,8,1,3,5,7,9]
i = np.argsort(my_permutation)
d=c[:,i]
e=np.delete(d,np.s_[1:2],axis=1)
np.savetxt("info_combine.csv", e,fmt='%s', delimiter=",")
