import numpy as np

# x = np.array([[1,2,3],[4,5,6]])
# print(x)
# print(x.shape)

# x.shape = (3,2)
# print(x)
# print(x.shape)
# print(x.reshape(3,2))

# a = np.arange(12)


# a = np.arange(2,22,2)   

# print(a)


# x = np.array([1,2,3,4,5], dtype=np.int8)
# x = np.array([1,2,3,4,5], dtype=np.float32)

# print(x.itemsize)

# x  = np.array([1,2,3,4])
# print(x.flags)
# x  = np.empty([3,3],dtype=int)


# x  = np.eye(6,dtype=int) 
# x  = np.eye(6,k=1) 

# x  = np.identity(3,dtype=int) 
# x  = np.identity(3) 
# x  = np.zeros((2,2),dtype=int) 
# x  = np.ones((2,2)) 

# x = np.full((2,2),np.inf)
# x = np.full((2,2),22)


# print(x)

# mylist = [[1,2,3],[4,5,6],[7,8,9]]
# # mylist = (1,2,3,4,5,6,7,8,9)

# print(type(mylist))

# x = np.asarray(mylist)

# print(x)

# m = np.asmatrix(x)
# print(m)
# x[2,1] = 50 
# print(m)

# print(x)

# print(type(x))

# l = b'eisbalvindr'

# print(type(l))

# a = np.frombuffer(l,dtype="S1",count=3,offset=10)
# print(a)
# print(type(a))
# print(len(a))


# x = np.array([1,2,3])
# y = x
# z = np.copy(x)

# x[0] = 10

# print(x)

# print(x[0] == y[0])
# print(x[0] == z[0])

# a = np.arange(1,10,2,int)
# a = np.linspace(10,20,endpoint=False)

# print(len(a))
# print(a[6])


# x = np.logspace(10,20,num = 10, endpoint = True)

# print(x)

# a = np.array([1,2,3,4,5,6,7,8,9])

# print(a[::])


# a = np.array([[1,20],[0,40],[2,60]])

# bin = (a > 10)

# print(bin)
# print(a[bin])
# print(a[a>2])

# a = np.array([1,2,3])
# b = np.array([3,5,6])
# a = np.array([[3,5],[3,4]])
# b = np.array([[5,6],[1,9]])
# arr = np.concatenate((a,b))

# arr1 = np.stack((a,b), axis=1)
# arr2 = np.hstack((a,b))
# arr3 = np.vstack((a,b))

# print(arr1)
# print(arr2)
# print(arr3)


# a = np.logspace(10,20,num=5,endpoint=True)

# print(a)

# b = np.logspace(10,20,num=5,endpoint=False)

# print(b)

arr = np.array([1,2,3,4,5,6,7,8,9])

ary = np.array_split(arr,3)

print(ary)
