# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Find len of a given Collection without len function

# a = input("Enter string: ")
# count = 0
# for i in a:
#     count += 1
# print("Length:", count)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Extract Vowel from string  

# a = input("Enter string: ")
# vowels = ""
# for i in a:
#     if i in "aeiouAEIOU":
#         vowels += i
# print("Vowels are:", vowels)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to replace space " " with  "_" {underscore} from: I/p : py ti hi 

# a = input("Enter string: ")
# String = ""
# for i in a:
#     if i == " ":
#         String += "_"
#     else:
#         String += i
# print("Converted String:", String)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Check a given string is palindrome or not without slicing

# a = input("Enter string: ")
# String = ""
# for i in a:
#     String = i + String
    
# print("Reverse String:", String)

# if a == String:
#     print("It is a Palindrome")
# else:
#     print("It is not Palindrome")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to remove all duplicates from list given by user and print only unique value

# a = input("Enter elements: ").split()

# for i in range(len(a)):
#     count = 0

#     for j in range(len(a)):
#         if a[i] == a[j]:
#             count += 1
    
#     if count == 1:
#         print(a[i], end=" ")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to remove one of the duplicates from list given by user 

# a = input("Enter elements: ").split()
# for i in range(len(a)):
#     for j in range(i):
#         if a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=" ")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Extract all int which are multiple of 5 and three digit in it from the given list

# a = eval(input("Enter String:"))
# String =[]
# for i in a:
#     if type(i) == int and i % 5 == 0 and 100 <= i <= 999:
#         String += [i]
# print("Final String:", String)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = 12, 3.4, "Hi", "Python", 5+6j, "harsh"
# O/P = {'Hi': 2, 'Python': 6, 'harsh': 5}

# a = eval(input("Enter Value :"))
# out = { }
# for i in a:
#     if type(i) == str:
#         out[i] = len(i)
# print("Final String:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to print user input as a Dictionary value such as input like: 11, 5.2, 'data', 8, 'science', 9

# a = eval(input("Enter Value :"))
# out = { }
# for i in a:
#     if type(i) == str:
#         out[i] = i[0] + i[-1]
# print("Final String:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = "aPPLe#754" 
# O/P = {'a': 'A', 'P': 'p', 'L': 'l', 'e': 'E'}

# a = eval(input("Enter Value :"))
# out = { }
# for i in a:
#         if "a" <= i <= "z":
#             out[i] = chr(ord(i)-32)
#         elif "A" <= i <= "Z":            
#              out[i] = chr(ord(i)+32)
# print("Final String:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Create a string with Uppercase character from A to Z 

# a = ""
# for i in range(65, 91):   
#     a = a + chr(i)
# print("Final Value:", a)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P= "hi hello how are you" 
# O/P = {'hi':2,'hello':5,'how':3,'are':3,'you':3}

# a = eval(input("Enter String: "))
# out = {}
# for i in a.split():
#     out[i] = len(i)
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = ['python.py','pro.html','pro3.py','google.com'] 
# O/P = ['py','html','py','com']  

# a = eval(input("Enter Value: "))
# out = []
# for i in a:
#     r = i.split(".")
#     out += [r[-1]]
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = ['python.py','pro.html','pro3.txt','google.com'] 
# O/P = {'html':'pro','py':'python','txt':'pro3','com':'googlr}  

# a = eval(input("Enter Value: "))
# out = {}
# for i in a:
#     r = i.split(".")
#     out[r[-1]] = r[0]
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = abcabacbcc 
# O/P = a3b3c4

# a = input("Enter Value:")
# out = ""
# for i in a:
#     if i not in out:
#         val = a.count(i)
#         out+= i + str(val)
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = [12,10,16,22,24,12,6,16] 
# O/P = [10,22,24,6]

# a = input("Enter Value: ")
# a = a.strip("[]")
# val = a.split(",")
# out = []
# for i in val:
#     if val.count(i) == 1:
#         out.append(int(i))  
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = 'abcaabccbbb'
# O/P = {'a':3,'b':5,'c':3}

# a = input("Enter Value: ")
# out = {}
# for i in a:
#     if a not in out:
#         out[i] = 1
#     else:
#         out[i]+=1
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# I/P = ['p1.py','file.txt','pro.py','google.com','data.txt'] 
# O/P = {'py':['p1','pro1'],'txt':['file','data'],'com':['google']}

# a = input("Enter Value: ")
# a = a.strip("[]")  
# val = a.split(",")
# out = {}
# for i in val:
#     b = i.split(".")
#     if b[1] not in out:
#        out[b[1]] = [b[0]]
#     else:
#        out[b[1]].append(b[0])
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to take and get given output
# s = 'aaabbaabcc' 
# out = 'a3b2a2b1c2' 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to find factorial of a given number 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to check a given number is perfect number or not 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to check a given number is armstrong or not 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to consider a dict consist of stud name with result and ectract key value pair from dict 
# only if stud scored more than 80 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️ WAP to extract key value pair from dict only if key is of string type 
#   d = {'Taj':'T5','Pallavi':'T4','vishu':'T23'} 
# out = {'T23':'vishu','T4':'Pallavi','T5':'Taj'} 



# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶
