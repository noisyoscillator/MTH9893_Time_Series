'''
 Markov chain Monte Carlo simulation
 Reference: P36 in lecture notes 6
'''

import numpy as np
import matplotlib.pyplot as plt
def target density(x):
fac = np.sin(x) * np.sin(2*x) return fac**2 * np.exp(-0.5*x**2)
def metropolis(theta, a):
eta = np.random.uniform(theta - a, theta + a)
u = np.random.uniform()
if u > target density(eta) / target density(theta):
       eta = theta
   return eta
N = 100000
theta = np.zeros(N)
theta[0] = 3.14
for i in range(1, N):
   theta[i] = metropolis(theta[i-1], 1.0)
plt.hist(theta[1000:N], 150, color = ’g’)
plt.show()
