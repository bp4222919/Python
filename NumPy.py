import numpy as np

# # y = [67,8,809,8]
# # print(y*3)

# x = np.array([1,2,3,4] ,dtype=float)

# x = np.empty([3,2], dtype=int)

# x = np.zeros((2,2))
# print(x)

# x = np.array([(1,3,4),(2,3,4),(2,4,7),(6,8,9)])

# print(x)
# # x.shape = (3,2)

# print(x.reshape(6,2))
# print(x)


# print(x)
# print(type(x))
# print(len(x))

# x = np.array([(1,2,3),(4,5,6),("w","f")])


# x = np.arange(1,20,3)
# print(x)


# x = np.array([10,20,30,40,50])
# print(x.flags)

# x = np.empty([3,3], dtype=int)

# x = np.eye(3,dtype=int)

# x = np.eye(5, k=1)

# print(x)

# b = np.eye(2, dtype = float)
# print("Matrix b : \n", b)
 
# matrix with R=4 C=5 and 1 on diagonal
# below main diagonal
# a = np.eye(4, 5, k = -1)
# print("\nMatrix a : \n", a)

# mylist = [1,3,4,5,6,7,4]    
# mylist = (1,3,4,5,6,7,4)

# print(type(mylist))

# x = np.asarray(mylist)

# print(type(x))


# arr = np.array([[1,2,3],[4,5,6]])

# print(arr)

# mx = np.asmatrix(arr)

# arr[1,2] = 10

# print(mx)


# str = b'hellopython'

# print(str)

# print(type(str))

# x = np.frombuffer(str, dtype="S1",count=5,offset=3)

# print(x)
# print(type(x))

# list = range(10)
# x = iter(list)

# print(type(x))

# a = np.fromiter(x,dtype=int)

# print(a) 

# a = 10
# b = a
# c = b


# x = np.array([1,2,3,4])
# y = x
# z = np.copy(x)   

# x[0] = 10 #[10,2,3,4]

# print(x[0] == y[0]) 
# print(x[0] == z[0]) 


# a = np.arange(1,20,2,int)

# a = np.linspace(1,20 ,15, endpoint=False) 
# b = np.linspace(1,20 ,10, endpoint=True)  

# print(a)
# print("===========================")
# print(b)

# a = np.logspace(1,20,num=5,base=3)

# print(a)


# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# a3 = np.array([7,8,9])
# a4 = np.array([7,8,9])


# arr = np.stack((a1,a2,a3)) #0 or 1
# arr = np.hstack((a1,a2,a3)) #0 or 1


# arr = np.vstack((a1,a2,a3,a4)) #0 or 1

# print(arr)


# x = np.concatenate((a1,a2,a3))

# print(x)

# a = np.array([[1,2,3],[4,5,6,],[7,8,9]])

# print(a[1:5])
# print(a[1,0],a[0,2],a[2,2])
# print(a > 5)


# arr = np.array([1,2,3,4,5,6,7,8,9,1,6])

# newarr = np.array_split(arr,3)

# print(newarr)


a1 = np.array([[1,2,3],[2,3,4]])
# a2 = np.array([4,5,6])

# print(a1 + a2)
print(sum(a1))
