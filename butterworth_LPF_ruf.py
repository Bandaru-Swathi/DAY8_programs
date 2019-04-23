import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
t=0.1
ws=0.7*np.pi
wp=0.35*np.pi
ps=(2/t)*np.tan(ws/2)
pp=(2/t)*np.tan(wp/2)
n1=(10**(0.1*20))-1
n2=(10**(0.1*4.436))-1
n3=np.log(ps/pp)
N=np.ceil((0.5*np.log(n1/n2))/(n3))
n4=0.5/N
n5=(0.1**(-2))-1
pc=(ps/(n5**n4))
b1=2*np.sin(np.pi/(2*N))
b2=2*np.sin(3*np.pi/(2*11))
w=np.linspace(0,3.14,1000)
j=cm.sqrt(-1)
s=np.exp(j*w)
bk=2*(np.sin((1)*np.pi/(2*N))
H=(pc**2)/((s**2)+(bk*pc*s)+(pc**2))
print bk
print pc
print N
plt.plot(w,np.abs(H))
plt.show()
