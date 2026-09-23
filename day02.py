#identity tokens and statement
a = 45
b = 35
c = 20
print(a + b + c)

#keywords
import keyword 
print(keyword.kwlist)
print(len(keyword.kwlist))

#Identifiers
num1 = 10 
n2m = 20 
n_m = 30
_num4 = 40
# 3num = 30
# n@m = 40 
# for = 30
a = 30 
A = 20
print(a)
print(A)
#variables 
name = 'rakesh'
age = 23

#assignment 
a = 40 
b = 50

#multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)
a = b = c = 10
print(a, b, c)

#reassignment
z = 10
z = 20 
z = 30
print(z)

#deleting variable
a = [1,2,3]
b = a 
del a 
# print(a)
print(b)

#swapping variables
a = 10
b = 20 
a,b = b,a 
print(a, b)

#without third variable
#using + and - 
a = 10
b = 20
a = a + b 
b = a - b 
a = a - b 
print(a, b)

#using * and /
a = 10
b = 20
a = a * b 
b = a / b 
a = a / b
print(a, b)

#using ^. A^A = 0, A^0 = A. (A^B)^C  = A^(B^C) 
a = 10  #^ cannot be used for float
b = 20
a = a ^ b 
b = a ^ b  #(a^b) ^ b = a ^ b ^ b = a ^ 0 = a
a = a ^ b  # (a^b) ^ a = a ^ b ^ a = b
print(a, b)

#single line comment
'''multi
line
comment
'''
