### Function in python 

#global variable

# def add():
#     print('function execution started')
#     return "Hey i terminated the function "
#     print('after the return keyword')
#     num1 = 100
#     num2 = 100
#     addition = num1 + num2
#     return addition


# calling function 
# output = add()
# print(output)

# return => it return value 
# 2. it terminate the execution function 


# input , process , output 

# len()  # built in function 

# ls = [52,41,63,96,85,74,85,52]

# count = 0 
# for item in ls:
#     count +=1

# print(count)
# print(len(ls))




# def apna_len(ls):    # parameter
#     count = 0
#     if type(ls)==list:
#         for item in ls:
#             count +=1 
#     return count

# ls = [52,41,63,96,85,74,85,52]


# print(apna_len(ls))
# print(len(ls))
 

# ls = [85,74,96,5,452,36,52,85,74,96,85,41,52,63,3,2,1,4]


# def filter_fun(ls):
#     for item in ls:
#         if item > 50:
#             print(item)


# filter_fun(ls)
# ls =[101,456,23,10,678,390,1000,3456,6]
# def apna_min(ls):
#     min1=ls[0]
#     for i in range(1,len(ls)):
#         if(min1>ls[i]):
#             min1=ls[i]
#     return min1

# print(apna_min(ls))

# print(min(ls))


# ls = [85,74,96,5,452,36,52,85,74,96,85,41,52,63,3,2,1,4]
# ls2 = [8,52,41,63,85,96,7,4,85,96,6,42]


# def even_finder(ls):
#     for item in ls:
#         if item % 2 == 0:
#             print(item)


# even_finder(ls)

# def square_finder(num):
#     return num ** 2 

# print(square_finder(8))

# lambda function 

# square = lambda x:x**2
# print(square(8))

# map
# map(functioon ,iterable ) 
# apna_map()