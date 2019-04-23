import numpy as np
import matplotlib.pyplot as plt
import math 
import cmath as cm
del_1=0.6
del_s=0.1
w_p=0.7*np.pi
w_s=0.35*np.pi
t=0.1
j=cm.sqrt(-1)
wo_p=(2/t)*np.tan(w_p/2)
wo_s=(2/t)*np.tan(w_s/2)
d_s=del_s**-2
d_p=del_1**-2
x=(d_s-1)/(d_p-1)
print(x)
#sq=np.sqrt(x)
l=d_s-1/d_p-1
sq=np.sqrt(l)
print l
wo_s1=wo_p/wo_s
wo_p1=wo_p/wo_p
dq=wo_s1/wo_p1
print('sq',sq)
print('dq',dq)
#N_0=(math.acosh(sq))/(math.acosh(dq))
#N=math.ceil(N_0)
#print('N',N)

