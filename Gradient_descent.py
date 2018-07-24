import numpy as np
import pylab

#---Dataset location---

data = np.genfromtxt('C:\School\Yr2-1-Semester\AI-Programming\python\Assignment\population_vs_profit.txt', delimiter=',', names=['x','y'])


#---labeling the axes---
pylab.title('Population vs Profit plt')
pylab.xlabel('Population')
pylab.ylabel('Profit')

#---plotting on pylab---

pylab.plot(data['x'], data['y'])
pylab.scatter(data['x'], data['y'])
#pylab.hist2d(data['x'], data['y'])

pylab.show()

def compute_cost_function(m, t0, t1, x, y):
    return 1/2/m * sum([(t0 + t1* np.asarray([x[i]]) - y[i])**2 for i in range(m)])
grad0 = 1.0/m * sum([(t0 + t1*np.asarray([x[i]]) - y[i]) for i in range(m)])
grad1 = 1.0/m * sum([(t0 + t1*np.asarray([x[i]]) - y[i])*np.asarray([x[i]]) for i in range(m)])
# update the theta_temp
theta1 = t0 - alpha * grad0
theta2 = t1 - alpha * grad1