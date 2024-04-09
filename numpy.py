import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print(type(arr1))

arr_tup=np.array((4,5,6))
arr_nd=np.ndarray([7,8,9])

print(type(arr_tup))
print(type(arr_nd))
# print(arr_nd)
print(arr_tup.ndim)
arr0=np.array([1],ndmin=7,dtype='O')
print(arr0.ndim)

print(arr1[0,1])

print(arr0.dtype)

arr00=arr0.astype('i')
print(type(arr0))
print(arr00.dtype)


arr00.reshape(3,4)

np.concatenate((arr1,arr_tup))

newarr=np.array_split(arr1,3)

arr01=arr0.copy()

x=np.where(arr_nd==4)

print(np.sort(newarr))


# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1)
# print(type(arr1))

# arr_tup=np.array((4,5,6))
# arr_nd=np.ndarray([7,8,9])

# print(type(arr_tup))
# print(type(arr_nd))
# # print(arr_nd)
# print(arr_tup.ndim)
# arr0=np.array([1],ndmin=7)
# print(arr0.ndim)

# print(arr1[0,1])

