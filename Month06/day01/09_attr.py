'''
数组的一些常用属性
'''
import numpy as np
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape) #(3,3)
print(a.dtype) #complex128
print(a.ndim) #2
print(a.size) #9
print(a.itemsize) #16
print(a.nbytes) # 144
print(a.real, a.imag, sep='\n')
print(a.T)

for i in a.flat:
    print(i)
