import numpy as np
a=np.genfromtxt('info_day.csv',delimiter=',',dtype=None,encoding='ascii')
for i in range(1,8):
    a[i][1]=float(a[i][1]) * 1.8 + 32
np.savetxt('transformed.csv', a, fmt='%s', delimiter=",")