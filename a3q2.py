import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def lotka_volterra(z,t):
    x,y=z
    dx_dt=-0.1*x+0.02*x*y
    dy_dt=0.2*y-0.025*x*y
    return[dx_dt,dy_dt]
x0=6
y0=6
z0=[x0,y0]
t=np.linspace(0,200,1000)
solution=odeint(lotka_volterra,z0,t)
x=solution[:,0]
y=solution[:,1]
print(solution)
plt.figure()
plt.plot(t,x,label='predators(x)')
plt.plot(t,y,label='prey(y)')
plt.xlabel('Time')
plt.ylabel('populations')
plt.legend()
plt.show()

equal_time=np.argmin(np.abs(x-y))
print(f'two populations are first equal={equal_time:.2f}')
