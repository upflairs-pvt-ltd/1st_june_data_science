# # ls = [5,4,63,96,85,74,852,2]


# # output = list(map(lambda x:x**2,ls))
# # print(output)
# # def fun(item):
# #     return item**2

# # ls = []
# # for item in ls:
# #     square = fun(item)
# #     ls.append(square)


# ## EXCEPTION HANDLING 

# # try:
# #     name = input("plz enter your good name : ")
# #     age = int(input("plz enter your age : ")) 
# #     print("I am ",name,"and i am ",age,"year old")
# # except:
# #     print("error is occured but dont worry we will execute your remining lines")

# # else:
# #     print('error is not occured!')

# # finally:
# #     print("i will be always")





# # try:
# #     num1 = int(input('enter your first number : '))
# #     num2 = int(input('enter your second number : '))
# #     result = num1 / num2   # 
# #     print(result)
# # except ZeroDivisionError:
# #     print("Plz dont insert zero in second number!")

# # except ValueError:
# #     print('Plz enter a valid input or integer ')


# # print('I am important, plz execut me!')


# ls = [52,41,63,96,85,96,74,25,75,64,43,27]

# target = int(input("enter your target item : "))
# position = int(input("plz enter a position : "))

# for i in range(len(ls)):
#     if ls[i] == target:
#         print(i) 
#         break 



# print('I am important, plz execut me!')




# try:
#     tar = int(input("input your target item "))
#     pos = int(input("input your target item index "))
#     print(lst.index(tar))
#     print(lst[pos])
# except ValueError:
#     print("please enter an int value ")
# except IndexError:
#     print("index out of range please enter within the list size ", len(lst)-1)
# finally:
#     print("i am important")




# ls = [52,41,85,68,96,45,78,25,89,63]
# target = int(input("enter your no: "))
# position = int(input("enter your position: "))
# try:
#    position = ls.index(target)
#    print(position)
#    target = ls[position]
#    print(target)
# except IndexError:
#    print("Use the right index")
# except TypeError:
#    print("use the corret words")




# ls=[54,45,23,65,32,34,68,67]
# try:
#     target=int(input("Enter target: "))
#     position=int(input("please enter a position: "))

#     def targ(ls,t):
#         for i in range(len(ls)):
#             if ls[i]==t:
#                   return i
#         return "Not found"  


#     print(targ(ls,target))
 
#     def position1(t):
#         try:
#             return ls[position]
#         except IndexError: 
#             print("Invalid index.")   
#     print("Value at",position,"=",position1(po



# try:
#     age =int(input('enter age : ')) 
# except Exception as e:
#     print(e) 
# except:
#     print('hiii error aa gyi ') 

### DONE 






