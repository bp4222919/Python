# mylist = ["a","b","c","d","e","f"]
# mylist2 =[1,2,3,4]

# mylist[1]="hello"
# mylist.append("hello")
# mylist.insert(2,"name")
# mylist.extend(mylist2)
# mylist.remove("b")
# mylist.pop(2)

# del mylist[3]

# print(mylist[:5])

# print(mylist[1:4])


# print(list())


# =====================03/04/2024========

# str1 = "Python"

# print(reverse(str1))

# str2 = "Pyhton,Java,JavaScript,PHP,C,C++"

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# num1 = [1,2,3,4,45,78,42,74859]

# thislist.sort(key=len)
# print(thislist)
    
# i = 1

# for i in range(i,101,5):
#     print(i)


# str1.split()

# print(len(str2.split(",",3)))


# =====================08/04/2024========

# x = [[1,2,3],[4,5,6],[7,8,9]]

# # print(x[0][2])

# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j],end=" ")
#     print()    
    

# ============================09/04/2024=========

# x = ("jghkjhg",)

# print(x)
# print(type(x))

# x = (3,4,5,6,6,67)
# print(x.count(6))
# print(x.index(4))
# print(len(x))
# print(min(x)) 

# a = 78
# b = "jjj"
# c = 7687

# tpl = (a,b,c,7687567465)
# print(tpl)

# x[0]= 78

# del x
# print(x * 7)

# for i in x:
#     print(i)

# print(x[-1])

# tpl = tuple(x)

# print(type(tpl))
# print(tuple(x))

# tpl = tuple(range(1,100,5))
# print(tpl)

# print(i[x])
# for i in x:
#     print(i)
# print(x[3][2])


# y =[1,3,6,3,3,3,3]
# z =[1,3,6,76,3,3,3,3]

# x = ["a","b","c"]
# print("d" not in x)


# y = ["a","b","c"]
# z = ["A","B","C"]

# print(x >= z)
# print(x == z)
# print(y != x)



# mylist2 =[545,7545,54534,5454]

# print(mylist * 15)

# # x = mylist[:]
# x = mylist.copy()

# x[2] = 10
# print(id(x))
# print(id(mylist))

# print(mylist)
# print(x)


# print(max(mylist))
# print(min(mylist))

# print(mylist.count(3))

# =================================10/04/2024===========


# dec = {
#    "name":"raman",
#    "age": 25,
#    "rollno":10
# }

# dec2 = {"name":"pawan"}
# dec.update(dec2)
# print(dec)

# print(len(dec))

# x  = dec.copy()
# print(dec)
# print(x)
# print(id(dec))
# print(id(x))

# dec.setdefault("Email","abc123@gmail.com")

# mydec = dict(sorted(dec.items()))

# print(dec)

# dec.pop(2)
# dec.popitem()
# dec.clear()

# del dec

# print(dec)

# dec[2]= "gfhgfjg0000f"
# dec[3]="python"

# for i in dec:
#     print(i)

# for i in dec.values():
#     print(i)

# print(dec.get(5))


# def binary(array, target):
#     left, right = 0, len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] >= target:
#             return mid
#         elif array[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "Value Is Not Found"

# array = [10, 20, 30, 40, 50]
# print(binary(array,60))


# =======================15/04/2024===============

# dec1 = {
#     1:20,
#     2:30,
#     3:40
# }                      
# dec2 = {
#     4:20,
#     5:30,
#     6:40
# }

# x = {**dec1,**dec2}
# print(x)

# dec1.update(dec2)
# print(dec1)

# print(dec1 == dec2)
# print(dec1.keys())
# print(dec1.values())


# dect = {x : x*x for x in range(1,11)}
    
# print(dect)

# mask = {
#     "hindi":45,
#     "english":85,
#     "punjabi":96,
#     "computer":45
# }

# totle = 0
# for x in mask.values():
#     totle = totle + x

# xy  = totle / len(mask)    

# print(mask)
# print(xy)

# =====================16/04/2024=======

# arr = [10,20,30,40,50] 
# n = 40

# def search(arr,n,s):

#     for i in range(0,n):
#         if (arr[i] == s):
#             return i
#     return  -1
        
# arr = [10,20,30,40,50] 
# s = int(input("Enter Any Number: "))
# n = len(arr)       

# re = search(arr,n,s)
# if(re == -1):
#     print("NO")
# else:
#     print("Yes this Elenent in Array : ",s,"On Index Number",re)


# def hello():
#     print("Welcome in Function")

# hello()


# def is_even(x):
#    if( x % 2 == 0):
#        print("Number is Even")
#    else:       
#        print("Number Is Odd")

# is_even()





# ======================18/04/2024==========

# def num():
#     print("num function1")

# num()
# print()
         

# mylist=[10,34,54,95,434,343,994]


# x = lambda y:y%2==0
# num=int(input("Enter A Number : "))

# if(x(num)):
#     print("Number An Even")
# else:
#     print("Number Is Odd")    

# Define a lambda function to check if a number is even
# is_even = lambda x: x % 2 == 0

# Take user input
# num = int(input("Enter a number: "))

# Check if the number is even or odd and print the result
# if is_even(num):
#     print(num, "is an even number.")
# else:
#     print(num, "is an odd number.")




# def even(x):
#     return x%2==0  

# even_num =  list(filter(even,mylist))  


# def calc(a,b):
#     u = a+b
#     x = a-b
#     y = a*b
#     z = a/b
#     return u,x,y,z

# sum,sub,mul,div = calc()
# print(div)


# def tplfun(*a):
#     return a

# w = tplfun(1,2,5,3,6)
# print(w)
# print(type(w))




# def sum(a,b):
#     """ In this function do sum two value, 
#     function name is sum 
#     and  given tow arguments first a and 2nd b """
#     return a + b
    


# x = int(input("Enter A number : "))
# y = int(input("Enter A number : "))
# print(sum(x,y))

# help(sum)


# x = 10
# def num():
#     x #10
#     print("Num1 Value = ",x)
#     def num2():
#         x #20   10 to 20 
#         print("Num2 Value = ",x) #10
#         return
#     num2()
#     return
# num()



# def about(name,age,higth,surname):
#     print("my name is  : ",name)
#     print("my age is :",age)
#     print("my higth is :",higth)
#     print("my surname is :",surname)
#     # return

# about("balvinder",21,5.6,"kumar")



# =======================22/04/2024================

# x = 20
# def num():
#     global x 
#     print(x)
#     return
# num()
# print(x)


# def num(a,b):
#     """ 
#     kjhgfh
#     fkjhhkjhjhjkhj

#     iuguygt
#     sum function

#     """
#     return a + b

# print(num(10,20))
# help(num)


# def num(a,b="@gmail.com"):
#     return a + b

# print(num("hello123"))
 





# ========================13/05/2024==========
#(*n)

# def num(*n):
#     print(type(n))
#     return n
# print(num(10))

# def sum(*n):
#     a = 0
#     for x in n:
#         a = a + x
#     print(a) 

# y = sum(10,20,30) 
# print(y)     


# (**n)

# def str(**n):
#     print(type(n))
#     return n
# print(str(a=10,b=20))



# ========================14/05/2024===============

# def myfun(n,*s):
#     print("n value",n)
#     for a in s:
#         print(a)
# print(myfun(12,42,52,62))

# sum = lambda x: x%2==0
# y = sum(10)
# print()

# is_even = lambda y : y % 2==0
# y = float(10)
# print(is_even(y))


# y = lambda a : a%2==0     
# a = 11
# print(y(a))


# x = 12
# print(eval("20+56"))

# x = "Arg 1 mUst the bE a StrIan$g,the the object"

# y = x.count("the")
# print(y)


# y = x.find("the")
# y = x.rfind("the")
# y = x.capitalize()
# y = x.title()
# y = x.lower()
# y = x.upper()
# y = x.swapcase()
# a = x.lower()
# y = a.islower()

# a = x.upper()
# y = a.isupper()

# print(y)



# ========================15/05/2024=======

# x = ("a","b","c")

# y = " @ ".join(x)
# print(y)

# x = "   "
# y = " r "

# print(x.isspace())
# print(y.isspace())

# y = x.istitle()
# y = x.replace("the","in")
# y = x.strip()
# y = x.lstrip()
# y = x.rstrip()
# y = x.partition("Arg")

# print(y)

# X = "54675467"

# y = X.isalpha()
# y = X.isdigit()
# y = X.isalnum()

# print(y)

# =======================17/05/2024================
# x = 10
# x = 20
# x = "hgfhg the he the gjh the djhgh"

# y = x.rfind("the")
# y = x.isalnum()

# x = "76 + 56"
# print(x)

# print(eval("29 + 34"))

# UTF-8
# x = "pytåhon" 
# x = "pyjhgåjhågftåhon" 
# print(x.encode(encoding="ascii",errors="ignore"))
# print(x.encode(encoding="ascii",errors="replace"))
# print(x.encode(encoding="ascii",errors="namereplace"))
# y = x.startswith("hello")
# y = x.endswith("n")
# ascii
# print(y)




# str = "Python"
# print("o" not in str)

# ========================21/05/2024=================

# "HelloPython"

# def countstring(str):
#     upper = 0
#     lower = 0
#     for case in str:
#         if case.isupper():
#             upper = upper + 1
#         elif case.islower():
#             lower = lower + 1
#     return upper,lower
# str = str(input("enter a string : "))
# xuppre,xlower = countstring(str)
# print("upper string count", xuppre)
# print("lower string count", xlower)
                  

# x = "pythonihgdfutrd"

# y = slice(0,12,3)

# print(x[y])


# ================22/05/2024==================


# import re
# x = "Hello welnconme in python the"

# y = re.findall("[a-z]",x)
# y = re.findall("^hello",x)
# y = re.findall("\d",x)
# y = re.findall("python$",x)
# y = re.findall("p....n",x)
# y = re.findall("a?n",x)
# y = re.findall("in|Hello",x)
# y = re.findall("He.*n",x)
# y = re.findall("He.+n",x)
# y = re.findall("He.{67}e",x)


# print(y)
# if y:
#   print("Yes, string matching pattern")
# else:
#   print("No match")
# print(len(y))
# print(type(y))


# =================23/05/2024===================

# import re

# x = "Hello $ & We45lcomeIn 67 89 Python Class"

# y = re.findall("\AHello",x)
# y = re.findall(r"\bHello",x)
# y = re.findall(r"Hello\b",x)
# y = re.findall(r"\BHello",x)
# y = re.findall(r"come\B",x)
# y = re.findall("\d",x)
# y = re.findall("\D",x)
# y = re.findall("\s",x)
# y = re.findall("\S",x)
# y = re.findall("\w",x)
# y = re.findall("\W",x)
# y = re.findall("Class\Z",x)

# print(y)
# if y:
#   print("Yes, string matching pattern")
# else:
#   print("No match")
# print(len(y))
# print(type(y))

# ==============================27/05/2024==============

# x = "67 * 23"
# x = (67,78,5)

# print(eval(x))
# print(max(x))
# print(min(x))
# x = "35"

# print(round(2.46876788,5))
# print(round(2.46876788,5))
# print(int(x))
# print(type(int(x)))


# print(pow(2,3))

# import math

# print(math.ceil(-255.87687))
# print(math.ceil(255.87687))

# print(math.floor(-23.788))
# print(math.floor(23.788))

# print(math.sqrt(64))


# print(math.fabs(-6565.87))
# print(math.fabs(6565.87))

# import math

# x = 5

# print(math.factorial(x))


# print(math.gcd(15,45))

# x = 25 
# y = 2

# print(math.fmod(y,x))
# print(math.remainder(15,45))

# print(divmod(25,2))

# import random

# print(random.random())
# print(random.randrange(1,16,3))




# Python3 program to demonstrate fmod() function

# import math



# modulus of +ve integer number
# print(math.fmod(4, 5))
# print(4/5)
# print(math.fmod(43.50, 4.5))


# ===============================31/05/2024===============

from datetime import date
# from datetime import time
# from datetime import datetime

# a = datetime.time(datetime.now())

# # print(a.hour)
# # print(a.minute)
# # print(a.second)
# # print(a.microsecond)

# x = date.today()
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%w"))
# print(x.strftime("%d"))
# print(x.strftime("%b"))  
# print(x.strftime("%B"))
# print(x.strftime("%m"))
# print(x.strftime("%y"))
# print(x.strftime("%Y"))
# print(a.strftime("%H"))
# print(a.strftime("%I"))
# print(a.strftime("%p"))
# print(a.strftime("%M"))
# print(a.strftime("%S"))
# print(a.strftime("%f"))
# print(a.strftime("%z"))   
# print(a.strftime("%Z"))
# print(x.strftime("%j"))
# print(x.strftime("%U"))
# print(x.strftime("%W"))
# print(x.strftime("%c"))
# print(x.strftime("%x"))
# print(a.strftime("%X"))
# print(a.strftime("%%"))
# print(x.day)
# print(x.month)
# print(x.year)
# print(x.weekday())

# ===============================03/06/2024===============

# file = open("newfile.txt","r")

# file_read = file.read(3)

# print(file_read)

# file.close()

# file = open("newfile.txt","w")

# file_read = file.write("Python")

# print(file_read)

# file.close()

# file = open("newfile.txt","a")

# file_read = file.write("\nPython 5454")

# print(file_read)

# file.close()


# file = open("newfile.txt","r+")

# file_read = file.write("hello new data")

# print(file_read)

# file.close()

# file = open("newfile.txt","w+")

# file_read = file.write("welcome in python class")

# print(file_read)

# file.close()

# file = open("newfile.txt","a+")

# file_read = file.write("welcome in python class")

# print(file_read)

# file.close()



# ===============================04/06/2024===============

# file = open("newfile.txt","a")

# file_read = file.read()

# print(file.name)
# print(file.mode)

# print(file.readable())
# print(file.writable())

# file.close()

# print(file.closed)

# file = open("newfile.txt","r")

# file_read = file.read()
# line1 = file.readline()
# line1 = file.readline(50)
# line1 = file.readlines()

# print(line1)
# file.close()

# ===============================05/06/2024===============

lang = ["python","HTMl","java","c++","hello","CSS"] 
with open("list.txt" , "w") as mylist:
    for i in lang:
        mylist.write(f" {i} \n")

dis = open("list.txt","r") 
print(dis.read())  

dis.close()
