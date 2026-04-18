# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# for i in range(1,5):
#     for j in range(1,9,3):
#         print(i,j)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to print a number is strong number or not 

# a = int(input("Enter Value:"))
# sum = 0
# for i in str(a):
#     fact = 1
#     r = int(i)
#     for j in range(r, 0, -1):
#         fact*= j
    
#     sum += fact
# if sum == a:
#     print("Strong Number")
# else:
#     print("Not Strong Number")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to take given input to get given output
# I/P = [12,'programe', 6+5j, 5.3, 'break', 9]
# O/P = {'programe':'oae', 'break':'ea'}

# a = eval((input("Enter Value:")))
# out = {}
# for i in a:
#     if type(i) == str:
#         vow = ""
#         for j in i:
#             if j in "AEIOUaeiou":
#                 vow += j
#         out[i] = vow
# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to take given input to get given output
# I/P = [12,'programe', 6+5j, 5.3, 'break', 9]
# O/P1 = {'programe':'prgrm', 'break':'brk'}
# O/P2 = {'programe':'PROGRAM', 'break':'BREAK'}

# a = eval(input("Enter Value: "))
# out1 = {}
# out2 = {}

# for i in a:
#     if type(i) == str:

#         con = ""
#         val = ""
#         for j in i:
#             if j not in "aeiouAEIOU":
#                 con += j
#             if 'a' <= j <= 'z':
#                 val += chr(ord(j) - 32)
#             else:
#                 val += j
#         out1[i] = con
#         out2[i] = val

# print("Final Output 1:", out1)
# print("Final Output 2:", out2)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to take given input to get given output
# I/P as l = [10,13,4,6]
# O/P as out = [23, 20, 29, 27]

# l = eval(input("Enter Value: "))
# out = []
# val = sum(l)
# for i in l:
#     out.append(val - i)

# print("Final Value:", out)


# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# WAP to take given input to get given output
# I/P as l = [1000, 700, 100, 300, 900, 200]
# O/P as out = [[1000], [700, 300], [900,100]]

# l = eval(input("Enter Value: "))
# out = []

# for i in range(len(l)):
#     val = [l[i]]
#     for j in range(i+1, len(l)):
#         if l[i] + l[j] == 1000:
#             val.append(l[j])
#     if sum(val) == 1000:
#         out.append(val)

# print("Final Value:", out)

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# ⭐ ⭐ ⭐ ⭐ ⭐
# ⭐ ⭐ ⭐ ⭐ ⭐
# ⭐ ⭐ ⭐ ⭐ ⭐
# ⭐ ⭐ ⭐ ⭐ ⭐
# ⭐ ⭐ ⭐ ⭐ ⭐

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         print("⭐", end = " ")
#     print("\n")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ⭐
#   ⭐
#     ⭐
#       ⭐
#         ⭐

# n = int(input("Enter Number : "))
# for i in range (1, n+1):
#     for j in range (1, n+1):
#         if i == j:
#             print("⭐", end = " ")
#         else:
#             print(" ", end = " ")
#     print("\n")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# ⭐ 
# 🟢 ⭐ 
# 🟢 🟢 ⭐ 
# 🟢 🟢 🟢 ⭐ 
# 🟢 🟢 🟢 🟢 ⭐

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             print("⭐", end = " ")
#         elif i > j:
#             print("🟢", end = " ")
#         else:
#             print(" ", end = " ")
#     print("\n")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# 🟠 🟠 🟠 🟠 ⭐ 
# 🟠 🟠 🟠 ⭐ 🟢 
# 🟠 🟠 ⭐ 🟢 🟢 
# 🟠 ⭐ 🟢 🟢 🟢 
# ⭐ 🟢 🟢 🟢 🟢 

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i+j < n + 1:
#             print("🟠", end = " ")
#         elif i+j == n + 1:
#             print("⭐", end = " ")
#         elif i+j > n + 1:
#             print("🟢", end = " ")
#         else:
#             print(" ", end = " ")
#     print("\n")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# 1️⃣ 🕖 🕖 🕖 🕖
# 🕖 1️⃣ 🕖 🕖 🕖
# 🕖 🕖 1️⃣ 🕖 🕖
# 🕖 🕖 🕖 1️⃣ 🕖
# 🕖 🕖 🕖 🕖 1️⃣

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print("1️⃣", end = "  ")
#         elif i > j:
#             print("🕖", end = " ")
#         elif i < j:
#             print("🕖", end = " ")
#         else:
#             print(" ", end = " ")
#     print("\n")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# 0  0  0  0  0  
# 0           0  
# 0           0  
# 0           0  
# 0  0  0  0  0  

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n:
#             print("0", end="  ")
#         elif j == 1 or j == n:
#             print("0", end="  ")
#         else:
#             print(" ", end="  ")
#     print("")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# *       * 
#   *   *       
#     *     
#   *   *   
# *       * 

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             print("*", end=" ")
#         elif i + j == n + 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#     +     
#     +     
# + + + + + 
#     +     
#     +     

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == ((n+1)//2):
#             print("+", end=" ")
#         elif j == ((n+1)//2):
#             print("+", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
# * * * * * * * * *
# * *           * *
# *   *       *   *
# *     *   *     *
# *       *       *
# *     *   *     *
# *   *       *   *
# * *           * *
# * * * * * * * * *

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n:
#             print("*", end=" ")
#         elif j == 1 or j == n:
#             print("*", end=" ")
#         elif i == j:
#             print("*", end=" ")
#         elif i + j == n + 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, 2*n):
#         if j == (n - i + 1):
#             print("*", end="")
#         elif j == (n + i - 1):
#             print("*", end="")
#         elif i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#         *
#       *   *  
#     *   *   *
#   *   *   *  *  
# *   *       *  *

# n = int(input("Enter Number : "))
# for i in range (1, n+1):
#     for j in range(n-i):
#         print(" ", end = "")
#     for k in range(i):
#         if i == n and k == 2:
#             print(" ", end = "")
#         else:
#             print("* ", end = "")
#     print("")
            
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(j, end=" ")
#     print("")


# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# n = int(input("Enter Number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i, end=" ")
#     print("")
      
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#         5
#       5 4 
#     5 4 3 
#   5 4 3 2
# 5 4 3 2 1

# n = int(input("Enter Number :"))
# for i in range (1, n+1):
#     for j in range( n - i):
#         print(" ", end = " ")
#     for k in range (n, n-i, -1):
#         print(k, end = " ")
#     print()
      
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
# A B C D E
#   A B C D
#     A B C
#       A B 
#         A  

# n = int(input("Enter Value : "))
# for i in range (n):
#     for j in range(i):
#         print("  ", end="")
#     for k in range(n - i):
#         print(chr(65 + k), end=" ")
#     print()
      
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
# 1
# 4  9 
# 3  4  5 
# 16 25 36 49
# 5  6  6  8  9

# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         for j in range(i):
#             print(i + j, end=" ")
#     else:
#         for j in range(i):
#             print((i + j) ** 2, end=" ")
#     print()
      
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#   * * *
#  *     *
# * * * * *
# *       *
# *       *

# n = 5  
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 and j >= 2 and j <= 4:
#             print("*", end=" ")
#         elif i == 2 and (j == 2 or j == 5):
#             print("*", end=" ")
#         elif i == 3:
#             print("*", end=" ")
#         elif i >= 4 and (j == 1 or j == 5):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
      
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

#©️WAP to Print Pattern :
#   * * *
# *       *
# *       *
# *       *
#   * * *  

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i == 1 or i == n) and (j >= 2 and j <= n-1):
#             print("*", end=" ")
#         elif i > 1 and i < n and (j == 1 or j == n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end = " ")
#     print("")


# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
#   * * * * 
#     * * * 
#       * * 
#         * 

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i < j:
#             print("*", end = " ")
#         else: 
#             print(" ", end = " ")
#     print("")
    
# 🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶🔶

# ©️WAP to Print Pattern :
# ⭐ ⭐ ⭐ ⭐ ⭐ 
# ⭐ ⭐ ⭐ ⭐ 
# ⭐ ⭐ ⭐ 
# ⭐ ⭐ 
# ⭐ 

# n = int(input("Enter Number :"))
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         print("⭐", end = " ")
#     print("\n")
