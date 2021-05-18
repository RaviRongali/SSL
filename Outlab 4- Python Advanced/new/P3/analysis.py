import numpy as np
a=np.genfromtxt('info_day.csv',delimiter=',',dtype=None,encoding='ascii')
print('Field         Mean       Std.Dev')
for i in range(1,5):
    mean=0
    std_dev=0
    for j in range(1,8):
        mean=mean+float(a[j][i])
    mean=mean/7
    for k in range(1,8):
        std_dev=std_dev+(mean-float(a[k][i]))**2.0
    std_dev=std_dev/6
    std_dev=std_dev**0.5
    print(a[0][i].replace('"',''),mean,std_dev)