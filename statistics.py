import numpy as np

def var(n):
    mean = (n-1)/2
    var = mean**2 + (n-1)*(2*n -1)/6 - (n-1)*mean
    return mean, var

v = np.arange(50)
print(v.mean(), v.var())
print(*var(len(v)))
 
