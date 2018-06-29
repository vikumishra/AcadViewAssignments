#Question-1
import numpy as np
import statistics as st

from numpy import float64

arr1=np.random.rand(10,1)

print("Mean is")
print(arr1.mean())
print('\n')


#Question-2
arr2=np.random.rand(20,1)
print("Variance is")
print(arr2.var())
print("Standard Deviation is")
print(arr2.std())
print('\n')

#Question-3
arr3=np.random.rand(10,20)
arr3.dtype=float64
arr4=np.random.rand(20,25)
arr4.dtype=float64
arr5=np.matmul(arr3,arr4)
print("Multiplaction of two arrays is")
print(arr5)
print('\n')

arr6=np.sum(arr5)
print("Sum of all element of above matrix is")
print(arr6)

#Question-4




