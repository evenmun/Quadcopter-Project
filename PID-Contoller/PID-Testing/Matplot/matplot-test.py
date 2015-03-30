
import numpy as np;
import matplotlib.pyplot as plt;

x = [];
y = [];

for i in np.arange(0,2*np.pi ,2*np.pi/1000):
    x.append(i);
    y.append(np.sin(i));

plt.plot(x,y, 'b-', linewidth=2);
plt.grid(True);
plt.axis([0,2*np.pi,-1.5,1.5]);
plt.title('Sinus-Wave');
plt.xlabel('Time in sec');
plt.ylabel('Sin(t)');
plt.show();