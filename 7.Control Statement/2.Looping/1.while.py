# ©️Write a program to print reverse of given number
# a = int(input("Enter a number: "))
# reverse = 0
# while a > 0:
#     digit = a % 10
#     reverse = reverse * 10 + digit
#     a = a // 10
# print("Reversed number:", reverse)


# ©️Write a program to print sum of given number
# a = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     digit = a % 10
#     sum = sum + digit
#     a = a // 10
# print("Sum of digits:", sum)


# ©️Write a program product of individual digit which are even
# a = int(input("Enter a number: "))
# prod = 1
# while a > 0:
#     digit = a % 10
#     if digit % 2 == 0:  
#         prod = prod * digit
#     a = a // 10
# print("Product of even digits:", prod)


# ©️Write a program to print sum of n natural number
# a = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= a:
#     sum = sum + i
#     i += 1
# print("Sum of n natural numbers:", sum)


# ©️Write a program to find the factorial of a number 
# a = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= a:
#     fact = fact * i
#     i += 1
# print("Factorial:", fact)


# ©️Write a program to print every char form the string
# a = input("Enter a string: ")
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1



# ©️Write a program to print every Lower Case Char from the string
# a = input("Enter a string: ")
# i = 0
# string = ""
# while i < len(a):
#     if a[i].islower():  
#         string += a[i]
#     i += 1
# print("Lowercase characters:", string)


# ©️Write a program to print integer type of value from the already given list
# a = [10, "hello", 25, 3.5, "hi", 50, True]
# i = 0
# b = []
# while i < len(a):
#     if type(a[i]) is int:   
#         b.append(a[i])
#     i += 1
# print("Integers:", b)


# ©️Write a program to print integer type of value from the User given list
# a = input("Enter elements: ").split()
# i = 0
# b = []
# while i < len(a):
#     if a[i].isdigit():
#         b.append(int(a[i]))
#     i += 1
# print("Integers:", b)


# ©️WAP to extract uppercase character from string
# a = input("Enter String: ")
# i = 0
# b = " "
# while i < len(a):
#     if a[i].isupper():
#        b = a[i]
#     i += 1
# print("Uppercase: ", b)


# ©️WAP to extract uppercase, lowercase, digit and special character seperately from string into 4 different output string
# a = input("Enter Number: ")
# i = 0
# Uppercase = ""
# Lowercase = ""
# Digit = ""
# Special = ""
# while i < len (a):
#     val = a[i]
#     if val.isupper():
#         Uppercase += val
#     elif a[i].islower():
#         Lowercase += val
#     elif a[i].isdigit():
#         Digit += val
#     else:
#         Special += val
#     i += 1
# print("Uppercase:", Uppercase)
# print("Lowercase:", Lowercase)
# print("Digits:", Digit)
# print("Special:", Special)


# ©️WAP to print sum of integer in given list
# a = input("Enter Number: ").split()
# i = 0
# sum = 0
# while i < len(a):
#     if a[i].isdigit():
#         sum = sum + int(a[i])
#     i += 1
# print("Sum of Integers: ", sum)


# ©️WAP to convert all Lowercase char to Uppercase Char in user given input without using any in-built function
# a = input("Enter String: ")
# i = 0
# String = ""
# while i < len(a):
#     val = a[i]
#     if 'a' <= val <= 'z':
#         String += chr(ord(val) - 32)
#     else:
#         String += val
#     i += 1
# print("Converted String:", String)

# ©️WAP to convert all Lowercase char to Uppercase Char and vice verse in user given input without using any in-built function
# a = input("Enter String: ")
# i = 0
# String = ""
# while i < len(a):
#     val = a[i]
#     if 'a' <= val <= 'z':
#         String += chr(ord(val) - 32)                     #Every Lowercase is 32 Greater than Uppercase
#     elif 'A' <= val <= 'Z':                              # ord -> Gives ASCII value of that character
#         String += chr(ord(val) + 32)                     # ch -> Converts ASCII value to character
#     else:
#         String += val
#     i += 1
# print("Converted String:", String)
