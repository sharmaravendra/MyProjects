import numpy as np
a=np.array([5,6,9])
# print(a[1])
print("Dimension:",a.ndim)
print("Item Size:",a.itemsize)

a=np.array([[1,2],[3,4],[5,6]])
print("Dimension:",a.ndim)
print("Item Size:",a.itemsize)
print("Data Type:",a.dtype)
print(a)
print("Array size:",a.size)

a=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print("Data Type:",a.dtype)
print("Item Size:",a.itemsize)
print(a)
print("Array size:",a.size)
print("Shape:",a.shape)

a=np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(a)

a=np.zeros((3,4))
print(a)

a=np.ones((3,4))
print(a)

a=np.arange(1,5)
print(a)

astep=np.arange(1,10,3)
print(astep)

lnspc=np.linspace(1,5,10)
print(lnspc)

# shape
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)

b=a.reshape(2,3)
print(b)
print(a.reshape(6,1))

print(a.ravel())
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))

ar=np.array([[1,2],[3,4]])
print(ar)
ar1=np.array([[1,2],[3,4]])
print(ar1)
print(ar+ar1)
print(ar*ar1)
print(ar/ar1)
print(ar.dot(ar1))


