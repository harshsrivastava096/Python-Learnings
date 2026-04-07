# ©️Check if number is positive or negative

# num = int(input("Enter number: "))
# if num >= 0:
#     print("Positive")
# else:
#     print("Negative")


# ©️Check if number is even or odd

# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# ©️Check if number is divisible by 10
# num = int(input("Enter number: "))
# if num % 10 == 0:
#     print("Divisible by 10")
# else:
#     print("Not divisible by 10")


# ©️Check if age is adult or minor
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# ©️Check greater among two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")


# ©️Check if number is 3-digit or not
# num = int(input("Enter number: "))
# if 100 <= abs(num) <= 999:
#     print("3-digit number")
# else:
#     print("Not a 3-digit number")


# ©️Check if a character is vowel or consonant
# ch = input("Enter character: ").lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# ©️Check if a number is multiple of 3 or not
# num = int(input("Enter number: "))
# if num % 3 == 0:
#     print("Multiple of 3")
# else:
#     print("Not a multiple of 3")


# ©️Check if string length is greater than 5
# text = input("Enter string: ")
# if len(text) > 5:
#     print("Length > 5")
# else:
#     print("Length <= 5")


# ©️Check profit or loss
# cp = int(input("Enter cost price: "))
# sp = int(input("Enter selling price: "))
# if sp > cp:
#     print("Profit")
# else:
#     print("Loss or No Profit") 


# ©️Write a program to check that given number is Special character using NESTED IF-ELSE statement
# a = input("Enter a character: ")
# if a.isalpha():
#     print("It is only Alphabets")
# else:
#     if a.isdigit():
#         print("It is Digits")
#     else:
#         if a.isalnum():   
#             print("It is Combination of Alphabet and Digit")
#         else:
#             if any(c.isalpha() for c in a):
#                 if any(c.isdigit() for c in a):
#                     print("It is Combination of Alphabet, Digit and Special Character")
#                 else:
#                     print("Combination of Alphabet and Special Character")
#             else:
#                 if any(c.isdigit() for c in a):
#                     print("It is Combination of Digit and Special Character")
#                 else:
#                     print("It is Special Characters")


# ©️Write a program to check greated among three numbers using NESTED IF-ELSE statement
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b:
#     if a > c:
#         print("Greatest is:", a)
#     else:
#         print("Greatest is:", c)
# else:
#     if b > c:
#         print("Greatest is:", b)
#     else:
#         print("Greatest is:", c)


# ©️WAP to print reverse of str if it is start with Uppercase and end with digit 
# a = input("Enter a string: ")
# if a[0].isupper():
#     if a[-1].isdigit():
#         b = a[::-1]
#         print("Reversed string:", b)
#     else:
#         print("String does not end with a digit")
# else:
#     print("String does not start with an uppercase letter")


# ©️Write a program to check greated among Four numbers using NESTED IF-ELSE statement
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a > b:
#     if a > c:
#         if a > d:
#             print("Greatest is:", a)
#         else:
#             print("Greatest is:", d)
#     else:
#         if c > d:
#             print("Greatest is:", c)
#         else:
#             print("Greatest is:", d)
# else:
#     if b > c:
#         if b > d:
#             print("Greatest is:", b)
#         else:
#             print("Greatest is:", d)
#     else:
#         if c > d:
#             print("Greatest is:", c)
#         else:
#             print("Greatest is:", d)




