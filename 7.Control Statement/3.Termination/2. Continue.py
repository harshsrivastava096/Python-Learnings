# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to print  number from 1 to 12 and skip 5

# for i in range(1, 12):
#     if i == 5:
#         continue
#     print(i, end=" ")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to extract all integer from given list by user 

# l = eval(input("Enter List : "))
# out = []
# for i in l:
#     if type(i) == int:
#         continue
#     out.append(i)
# print(out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to Extract all special character from given string by user

# a = input("Enter String : ")
# out = ""
# for i in a:
#     if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
#         continue
#     out+=i 
# print(out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to print 1 to 10 using while loop and continue statement and skip 3 and 8

# i = 1
# while i <= 10:
#     if i == 3 or i == 8:
#         i += 1
#         continue
    
#     print(i, end=" ")
#     i += 1

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to display the number names of the digits given by user as example is user gives 231 it will give output as Two Three Four

# a = input("Enter Number : ")
# val = {
#     '0': "Zero", 
#     '1': "One", 
#     '2': "Two", 
#     '3': "Three",
#     '4': "Four", 
#     '5': "Five", 
#     '6': "Six",
#     '7': "Seven", 
#     '8': "Eight", 
#     '9': "Nine"
# }
# for i in a:
#     print(val[i], end=" ")