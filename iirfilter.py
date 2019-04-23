import numpy as np
import matplotlib.pytplot as plt
import cmath as cm
j=cm.sqrt(-1)
t=0.1
#for f in range(0,180):
w=np.linespace(0,np.pi)
z=exp(j*w)
z1=np.append(z1,z)
#s=(2/t)*((1-(1/z))/(1+(1/z)))
plt.plot(z)
plt.show()







'''n=np.arange(0,30,0.1)
x1=np.sinc(n*(np.pi/4))
plt.stem(n,x1/4,'b')
plt.title('SINC FUNCTION')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
