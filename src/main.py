
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.cos(x)  
    

X = np.linspace(0, 10, 1000)
Y = func(X)

plt.plot(X, Y)
plt.show()