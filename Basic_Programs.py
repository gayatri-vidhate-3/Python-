'''#Q1 Python program to add two numbers
num1 = float(input('Enter a first number:'))
num2 = float(input('Enter a first number'))
print('The sum of {} and {} is:{}'.format(num1,num2,num1+num2))
-----------------------------------------------------------

#Q2 Maximum of two numbers in Python
num1 = float(input('Enter a first number:'))
num2 = float(input('Enter a first number'))
if num1 > num2:
    print('{} is greater'.format(num1))
else:
    print('{} is greater'.format(num2))

#OR
def large(a,b):
    if (a>b):
        return a
    else:
        return b

print('the large number is:',large(4,6))
print('the large number is:',large(8,6))

#OR
num1 = float(input('Enter a first number:'))
num2 = float(input('Enter a first number'))
print(max(num1,num2))
print(('The max among two is:',max((num1,num2))))

#OR
# Use of ternary operator
print(num1 if num1 >= num2 else num2)
#------------------------------------------------------------
#Q3Python Program for factorial of a number
num = int(input('Enter a number whose factorial need to find: '))
if num == 0 or num ==1:
    print('factorial of {} is 1'.format(num))
elif num < 0:
    print(('Factorial of non positive number is not possible'))
else:
    factorial = 1
    while num > 1:
        factorial *= num
        num -=1
    print('The factorial of {} is {}'.format(num,factorial))

#OR Using Ternary operator
def factorial(n):
    return 1 if (n==0 or n ==1) else n * factorial(n-1)

num = int(input('Enter a number whose factorial need to find: '))
print(factorial(num))

#OR By using In-built function:

from math import factorial as f # member aliasing
num = int(input('Enter a number whose factorial need to find: '))
print(f(num))
--------------------------------------------------------
#Q4 Python Program for simple interest Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

P = float(input('Enter the principle amount'))
T = float(input('Enter the time'))
R = float(input('Enter the rate'))
SI = (P * T * R)/100
print('the SI for {} amount for {} duration with {} rate of interest is {}'.format(P,T,R,SI))
--------------------------------------------------------------------------------
#Q5 Python Program for compound interest
# Formula to calculate compound interest annually is given by:
# A = P(1 + R/100)^t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span
P = float(input('Enter the principle amount'))
T = float(input('Enter the time'))
R = float(input('Enter the rate'))
A = P*((1 + R/100)**T)
CI = A - P
print('the CI for {} amount for {} duration with {} rate of interest is {}'.format(P,T,R,CI))
---------------------------------------------------------------
#Q6 Python Program to check Armstrong Number
#A number is thought of as an Armstrong number if the sum of its own digits raised to the power number of digits gives the number itself.
# For example, 0, 1, 153, 370, 371, 407 are three-digit Armstrong numbers and, 1634, 8208, 9474 are four-digit Armstrong numbers
# and there are many more.

num = int(input("Enter a number: "))
sum = 0
order = len(str(num))
x = num
while x > 0:
    digit = x % 10   #modulo operator - returns the remainder of dividing the left hand operand by right hand operand.
    print(digit)
    sum += digit ** order
    print(sum)
    x //= 10  #Floor division - division that results into whole number adjusted to the left in the number line

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

---------------------------------------------------------------------------------
#Q7 Python Program for Program to find area of a circle
# A = pi * r^2

from math import pi
radius = float(input('ENter a radius of circle:'))
area = pi * (radius **2)
print('Area of the circle for radius',radius,'is:',area)
---------------------------------------------------------
#Q 8 Python program to print all Prime numbers in an Interval
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for num in range(num1,num2+1):
    if num > 0:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num,'is prime')

--------------------------------------------------------
#Q9 Python program to check whether a number is Prime or not
num = int(input("Enter first number: "))
for i in range(2,num):
    if num % i ==0:
        print(num,'is not prime')
        break
else:
    print(num,'is prime')

----------------------------------------------------------
#Q 10 Python Program for n-th Fibonacci number

# by using while loop
num = int(input("Enter number: "))
i = 1
sum = 0
while i < num:
    sum += i
    print(sum, end=' ')
    i += 1

----------------------------------------------------------'''
'''
# Ladies class
# 1.Python program to add two numbers
n1 = int(input('Enter 1 st number'))
n2 = int(input('Enter 2nd number'))
sum = n1+n2
print('The sum of {} and {} is {}'.format(n1,n2,sum))
----------------------------------------------------------
# 2) Maximum of two numbers in Python
n1 = int(input('Enter 1 st number'))
n2 = int(input('Enter 2nd number'))
if n1 > n2:
    print(n1,'is the maximum among',n1, '&', n2)
else:
    print(n1, 'is the maximum among',n2,'&', n1)
----------------------------------------------------------
# 3) Python Program for factorial of a number
num = int(input('Enter a number whose factorial need to be calculated: '))
i = 1
fact = 1
while i < num+1:
    fact *= i
    i += 1

print('the factorial of',num,'is',fact)
----------------------------------------------------------
# 4) Python Program for simple interest
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

P = float(input('Enter a principle amount: '))
T = float(input('Enter a time: '))
R = float(input('Enter a rate: '))
SI = (P * R * T)/100
print('SI is :',SI)
----------------------------------------------------------
# 5) Python Program for compound interest
# Formula to calculate compound interest annually is given by:
# A = P(1 + R/100)^t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span
P = float(input('Enter the principle amount'))
T = float(input('Enter the time'))
R = float(input('Enter the rate'))
A = P * ((1 + (R/100))**T)
CI = (A - P)
print('CI is:',CI)
----------------------------------------------------------
# 6)Python Program to check Armstrong Number
k = input('Enter a number to check armstrong number or not :')
b=[]
for i in k:
    b.append(i)
#print(b)
sum = 0
for i in b:
        sum = sum + int(i)**len(b)
#print(cube)
if int(k)== sum:
    print(k,'is a armstrong number')
else:
    print(k, 'is not a armstrong number')
----------------------------------------------------------
# 7) Python Program for Program to find area of a circle
from math import pi
r = float(input('Enter the radius'))
area = pi * (r**2)
print('Area is:', area)
----------------------------------------------------------
# 8) Python program to print all Prime numbers in an Interval
num1 = int(input('Enter the number1 '))
num2 = int(input('Enter the number2 '))
for num in range(num1,num2+1):
    if num>0:
        for i in range(2,num):
            if (num%i) ==0:
                break
        else:
            print(num,'is prime number')
----------------------------------------------------------
# 9)Python program to check whether a number is Prime or not
num = int(input('Enter the number'))
for i in range(2,num):
    if num % i == 0:
        print(num,'is not a prime number')
        break
else:
    print(num, 'is  a prime number')
----------------------------------------------------------
# 10)Python Program for n-th Fibonacci number
num = int(input('enter the number for n-th Fibbonacci number: '))
a = 0
b = 1
if num < 0:
    print('Incorrect Input')
elif num ==0:
    print(a)
elif num == 1:
    print(b)
else:
    for i in range(2,num):
        c = a + b
        a = b
        b = c
    print(b)
----------------------------------------------------------
# 11) Python Program for How to check if a given number is Fibonacci number?
num = int(input('enter the number which need to check as Fibbonacci number: '))
a = 1
b = 1
c = 0
if (num == 0) or (num ==1):
    print(num,'is a Fibbonacci Number')
else:
    while num < c:
        c = a + b
        b = a
        a = c
    if c == a:
        print('yes')
    else:
        print('No')
----------------------------------------------------------
# 12) Python Program for n\’th multiple of a number in Fibonacci Series

----------------------------------------------------------
# 13) Program to print ASCII Value of a character
char  = input('Enter a char')
print('The ASCII value of',char,'is',ord(char))
----------------------------------------------------------
# 14) Python Program for Sum of squares of first n natural numbers
num = int(input('enter the number : '))
i = 0
sum = 0
while i < num+1:
    sum += i**2
    i += 1

print(sum)

#OR

num = int(input('enter the number : '))
sum = 0
for i in range(num+1):
    sum += i ** 2

print(sum)
----------------------------------------------------------
# 15) Python Program for cube sum of first n natural numbers
num = int(input('enter the number : '))
sum = 0
for i in range(num+1):
    sum += i ** 3

print(sum)
----------------------------------------------------------
#EXTRA Problems by me 
# print the fibonnaci series for given number of elemnts
num=int(input('Enter  number'))
a= 0
b = 1
if num<0:
    print('invalid')
elif num == 0:
    print(a)
elif num ==1:
    print(b)
else:
    for i in range(2,num):
        c = a+b
        b = a
        a = c
        print(c, end = ' ')
----------------------------------------------------------'''

