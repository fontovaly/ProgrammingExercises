
# para mas ejercicios http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html

## Exercise 1: Generate random numbers between 0, 1
import numpy as np
r = np.random.random()

## Exercise 2: Generate vector of random numbers
r = np.random.randn(100)

## Exercise 3: Compute mean and std
mean = np.mean(r)
std = np.std(r)

## Exercise 4: Threshold this vector x>-1 and x < 1
rb = np.logical_and(x>-1, x < 1)

## Exercise 5: Generate a matrix of random numbers
r = np.random.randn(100,100)

## Exercise 6: Solve a linear problem Ax = b with A(shape(10,10), x,b (shape(10))
A = np.random.randn(10,10)
b = np.random.randn(10)

x = np.linalg.solve(A, b)

## Exercise 7: Create a mesh with np.linspace
x = np.linspace(0,10,1000)

## Exercise 8: Obtain the values of the sin function
y = np.sin(x)

## Exercise 9: Plot with matplotlib.pyplot the function
import matplotlib.pyplot as plt

fig = plt.figure(True)
l1 =  plt.plot(x,y, label='fitted')


## Exercise 10: Apply a random noise with std 0.1 and plot within the real values
y2 = y + np.random.randn(y.shape[0])*0.1

l2 = plt.plot(x,y2, 'r.', markersize=3, label='real')

## Exercise 11: Add legend, axis names and titles to the plot
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi],
          [r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$', r'$3\pi$'])
plt.yticks([-1, 0, +1])
plt.ylabel('Magnitude')
plt.xlabel('Domain')
plt.legend(loc=3)
plt.title('Data measured')

fig.show()

## Exercise 12: Create random numbers and make and histogram

x = np.random.randn(1000)

fig = plt.figure()
plt.hist(x, bins=30)
fig.show()

## Exercise 13: Create a linar model by creating an artificial data and check the parameters the model get and the error R²
x = np.random.uniform(0, 10, (10000,3))
A = np.array([9,2.5,1,4])
r = np.random.randn(10000, 3)*.01
y = A[0]+ np.sum(r+ A[1:]*x, axis=1)

import sklearn
from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit (x, y)

clf.intercept_
clf.coef_
clf.score(x,y)








