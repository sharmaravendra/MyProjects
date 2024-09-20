import numpy
import time
import sys

import numpy as np

SIZE=10

l1=range(SIZE)
l2=range(SIZE)
print(l1)
a1=np.arange(SIZE)
a2=np.arange(SIZE)
print(a1)
start = time.time()
result= [(x+y) for x,y in zip(l1,l2)]
print(result)
print("Python list took:",(time.time()-start)*1000)

start = time.time()
result=a1+a2
print(result)
print("Numpy took:",(time.time()-start)*1000)

import array as arr
array1 = arr.array('d', [0.1, 1.2, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(array1[i], end=" ")


