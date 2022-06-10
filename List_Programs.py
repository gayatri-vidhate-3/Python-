'''#Q1 Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

l = [12, 35, 9, 56, 24]
l[0],l[-1] = l[-1],l[0]
print(l)

-------------------------------------------------
#Q2 Python program to swap two elements in a list as per the position given by user
def swap(list,pos1,pos2):
    print('Original List:',list)
    list[pos1],list[pos2] = list[pos2],list[pos1]

    return list

pos1 = int(input('enter pos1: '))
pos2 = int(input('Enter pos2: '))
print('The swapped list is:', swap([23, 65, 19, 90],pos1,pos2))
#---------------------------------------------
#Q3 Python | Ways to find length of list

list = [ 1, 4, 5, 7, 8 ]
# by using inbuilt
print(len(list))

# without inbuilt
count = 0
for i in list:
    count += 1

print(count)

#by using length_hint
from operator import length_hint
print(length_hint(list))
------------------------------------------------------------
#Q 4 Check if element exists in list in Python
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2]
# by using function and in
def check(list):
    i = int(input('Enter the element which you want to check: '))
    if i in list:
        print('Element',i,'exists in list')
    else:
        print('Element', i, "doesn't exists in list")

check(l)

#by using loop
i = int(input('Enter the element which you want to check: '))
for a in l:   # it tells how many time number exists in list
    if a == i:
        print('Element', i, 'exists in list')

#by using count we can count how many times it repeated
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
i = int(input('Enter the element which you want to check: '))

for a in l:
    if i in l:
        count = l.count(i)

print('Element', i, 'exists in list for ',count,'times')
--------------------------------------------------
#Q5 Different ways to clear a list in Python
# by using clear
list1 = [1, 2, 3]
list1.clear()
print(list1)

# Using “*= 0”
list1 = [1, 2, 3]
list1 *= 0
print(list1)

#by using delet
list1 = [1, 2, 3]
del list1[:]
print(list1)
---------------------------------------------------
#Q6 Reversing a List in Python

#by using builtin reversed
l = [10, 11, 12, 13, 14, 15]
l1 = []
for i in reversed(l):
    l1.append(i)
print(l1)

new_list = [i for i in reversed(l)]
print(new_list)

l.reverse()
print(l)

list = [10, 11, 12, 13, 14, 15]
print(list[::-1])
------------------------------------------------
#Q7 Python program to find sum of elements in list
list = [10, 11, 12, 13, 14, 15]

# by using  for loop
sum = 0
for i in list:
    sum += i
print('the sum of all elements from list is:',sum)

# by using while loop
list = [10, 11, 12, 13, 14, 15]
i = 0
add = 0
while (i < len(list)):
    add += list[i]
    i += 1
print('the addition of elements from list is:',add)

#by using lambda
from functools import reduce
print(reduce(lambda x,y: (x+y), list))

# by using sum method
print(sum(list))
------------------------------------------------------------------------
#Q8Multiply all numbers in the list
list = [1,2,3,4]

# by uisng lambda function
from functools import reduce
print(reduce(lambda x,y: x*y, list))

#by using loop
mult = 1
for i in list:
    mult *= i
print(mult)

# by using while loop
i = 0
multiplication = 1
while i < len(list):
    multiplication *= list[i]
    i += 1
print(multiplication)
-----------------------------------
#Q9 Python program to find smallest number in a list
list = [20, 10, -9, 20, 1, 100,-1,-8,-12]

# by using loop
a = list[0]
for i in list:
    if i <= a:
        a = i

print('the smallest is:',a)

# by using sort
list.sort()
print(list)
print(list[0])

# by using min
list1 = [20, 10, -9, 20, 1, 100,-1,-8]
print(min(list1))
---------------------------------------------------
#Q10 Python program to find largest number in a list
list = [20, 10, -9, 20, 1, 100,-1,-8,-12]

# by using sort
list.sort()
print(list[-1])

#by using loop
list1 = [20, 10,140, -9, 20, 1, 100,-1,-8,-12,120]
a = list1[0]
for i in list1:
    if i > a:
        a = i

print('the largest is:',a)

#by using max
print(max(list1))

# by taking input from user
list_new = []
num = int(input('Enter how many elements arethere in list: '))

for i in range(0,num):
    element = int(input('Enter elements'))
    list_new.append(element)

print(list_new)
print(max(list_new))
------------------------------------------------------------
#Q 11 Python program to find second largest number in a list
list1 = [20, 10,140, -9, 20, 1, 100,-1,-8,-12,120]

#by using sort
list1.sort(reverse=True)
print(list1)
print(list1[1])
--------------------
# by using max
print(max(list1))
new_list = list1
new_list.remove(max(list1))
print(new_list)
print(new_list[0])
-----------------------
#by user and function

def second_largest(list):
    large= max(list)
    list.remove(large)
    large= max(list)
    return large

li=[]                     #input of list
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("second largest in ",li,"is")        #smallest
print(second_largest(li))
-------------------------------
# another approach
list1 = [20, 10,140, -9, 20, 1, 100,-1,-8,-12,120]
temp_list = []
temp_list.append(max(list1))
list1.remove(max(list1))
temp_list.append(max(list1))
print(temp_list)
print(temp_list[1])
-----------------------------
#brute-force method
list1 = [11,22,1,2,5,67,21,32]
#assuming max_ is equal to maximum of element at 0th and 1st index
#and secondmax is the minimum among them
max_=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
for i in range(2,len(list1)):
   # if found element is greater than max_
   if list1[i]>max_:
      secondmax=max_
      max_=list1[i]
   #if found element is greator than secondmax
   else:
      if list1[i]>secondmax:
         secondmax=list1[i]
print("Second highest number is the list is : ",str(secondmax))

--------------------------------------------------------------------------
#Q 12 Python program to find N largest elements from a list
# Below is the whole one program:-

num = int(input('Enter the legnth of list: '))
list = []
for i in range(num):
    element = int(input('Enter the element:'))
    list.append(element)

print(list)
#list = [11,22,1,2,5,67,21,32]
list.sort(reverse=True)
print('The sorted list is:',list)

n= int(input('enter how many largest elements are required: '))
new_list = []
for i in range(n):
    new_list.append(list[i])

print('The new list with',n,'element is:',new_list)

#OR by using while loop
list = [11,22,1,2,5,67,21,32]
n= int(input('enter how many largest elements are required: '))
new_list = []
list.sort(reverse=True)
print(list)
i = 0
while i < n:
    new_list.append(list[i])
    i += 1

print(new_list)

#OR by using for loop
list = [11,22,1,2,5,67,21,32]
n= int(input('enter how many largest elements are required: '))
list.sort(reverse=True)
print(list)
new_list = []
for i in range(n):
    new_list.append(list[i])

print('The new list with',n,'element is:',new_list)
--------------------------------------------------
# simplest way
list = [11,22,1,2,5,67,21,32]
list.sort()
print(list)
n = int(input('Enter how many largest elements wants to see: '))
print(list[-n:])
-------------------------------------------------------------
#Q 13 Python program to print even numbers in a list
list = [11,22,1,2,5,67,21,32,13,55,24]
# using for loop
for i in list:
    if i % 2 ==0:
        print(i,end = ' ')

# using while loop
list = [11,22,1,2,5,67,21,32,13,55,24]
i = 0
while i < len(list):
    if list[i] % 2 == 0:
        print(list[i], end=' ')
    i += 1

# by list comprehention
even_nos = [i for i in list if i%2==0]
print(even_nos)

# by lambada
list1 = [11,22,1,2,5,67,21,32,13,55,24]
even = list(filter(lambda i: (i % 2 == 0), list1))
print(even)
----------------------------------------------------
#Q14 Python program to print odd numbers in a List
list = [11,22,1,2,5,67,21,32,13,55,24]
# using for loop
for i in list:
    if i % 2 !=0:
        print(i,end = ' ')

# using while loop
list = [11,22,1,2,5,67,21,32,13,55,24]
i = 0
while i < len(list):
    if list[i] % 2 != 0:
        print(list[i], end=' ')
    i += 1

# by list comprehention
odd_nos = [i for i in list if i%2 !=0]
print(odd_nos)

# by lambada
list1 = [11,22,1,2,5,67,21,32,13,55,24]
odd = list(filter(lambda i: (i % 2 != 0), list1))
print(odd)

------------------------------------------------------------------------
#Q15Python program to print all even numbers in a range
first= int(input('Enter first element'))
last= int(input('Enter last element'))
# using for loop
for i in range(first,last):
    if i % 2 ==0:
        print(i,end = ' ')
-----------------------------------------------'''
#Q 16
'''
# 1) Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

l = [12, 35, 9, 56, 24]
l[0],l[-1] = l[-1],l[0]
print(l)
-----------------------------------------------
# 2)Python program to swap two elements in a list
def swap(l,pos1,pos2):
    print('old list: ',l)
    l[pos1],l[pos2] = l[pos2],l[pos1]

    return l

pos1 = int(input('enter pos1: '))
pos2 = int(input('Enter pos2: '))
print('The swapped list is:', swap([23, 65, 19, 90],pos1,pos2))
-----------------------------------------------
# 3) Python | Ways to find length of list
list = [ 1, 4, 5, 7, 8 ]
# by using inbuilt
print(len(list))

# without inbuilt
count = 0
for i in list:
    count += 1

print(count)

#by using length_hint
from operator import length_hint
print(length_hint(list))
-----------------------------------------------
# 4) Python | Ways to check if element exists in list
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2]
i = int(input('Enter the element which you want to check: '))
if i in l:
    print(i,'exists in list')
else:
    print(i, 'doesn"t exists in list')

# by using for
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2]
i = int(input('Enter the element which you want to check: '))
for a in l:
    if a ==i:
        print(i, 'exists in list')
else:
    print(i, 'doesn"t exists in list')

#by using count we can count how many times it repeated
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
i = int(input('Enter the element which you want to check: '))
count = 0

for a in l:
    if i in l:
        count = l.count(i)
print('element',i,'exists in list for',count,'times')

# by list comprehension
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
i = int(input('Enter the element which you want to check: '))
print('Exist' if i in l else 'Not Exist')

-----------------------------------------------
# 5)Different ways to clear a list in Python
# by using clear
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
l.clear()
print(l)

# by using pop
for i in l:
    l.pop(i)

print(l)

# by using while and remove
i = 0
while i < len(l):
    l.remove(i)
    i += 1

print(l)

# Using “*= 0”
# Using “*= 0”
list1 = [1, 2, 3]
list1 *= 0
print(list1)

#by using delet
list1 = [1, 2, 3]
del list1[:]
print(list1)
-----------------------------------------------
# 6) Python | Reversing a List
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]

# by using reverse function
l.reverse()
print(l)

l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
new_list = l[::-1]
print(new_list)
-----------------------------------------------
# 7 )Python program to find sum of elements in list
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]

# by using sum function
print(sum(l))

# by using for loop
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
sum=0
for i in l:
    sum += i
print(sum)

# by using while loop
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
i = 0
sum =0
while i < len(l):
    sum += l[i]
    i += 1

print(sum)

# by using lambda comprehension
l = [ 1, 6, 3, 5, 3, 4 ,5,2,2,5,2]
from functools import reduce
print((reduce(lambda a,b: a+b,l)))
-----------------------------------------------
# 8)Python | Multiply all numbers in the list
l = [ 1, 2, 3, 4]
# by using for loop
mult = 1
for i in l:
    mult *= i
print(mult)

# by using while loop
l = [ 1, 2, 3, 4]
i = 0
mult = 1
while i < len(l):
    mult *= l[i]
    i += 1
print(mult)

# by using lambda
from functools import reduce
print(reduce(lambda x,y: x*y, l))
-----------------------------------------------
# 9) Python program to find smallest number in a list
l = [11,2,3,67,0,78,-1,3,44]

# by using inbuilt
print(min(l))

# by using for loop
list = [11,2,3,67,0,78,-1,3,44]
a = list[0]
for i in list:
    if i <= a:
        a = i

print(a)

# by using sort
list = [11,2,3,67,0,78,-1,3,44]
list.sort()
print(list[0])
-----------------------------------------------
# 10) Python program to find largest number in a list
l = [11,2,3,67,0,78,-1,3,44]
# by using max
print(max(l))

# by using sort
l.sort()
print(l [-1])

# by using for/while loop
l = [11,2,3,67,0,78,-1,3,44]
i = 0
max= l[0] # l[0] means first elemnt from list
print(max)
for i in l:
    if i >= max:
        max = i

print(max)

# by using while
l = [11,2,3,67,0,78,-1,3,44]
i= 0
max = l[0]
while i < len(l):
    if l[i] >= max:
        max = l[i]
    i += 1

print(max)
-----------------------------------------------
# 11) Python program to find second largest number in a list
l = [11,2,3,67,0,78,-1,3,44]

# by using sorting
l.sort()
print('second largest number',l[-2])

# by using set
l = [11,2,3,67,0,78,-1,3,44]
print(set(l))
l.remove(max(l))
print(l)
print(max(l))

# by using for
l = [11,2,3,67,0,78,-1,3,44]
max = l[0]
large = []
for i in l:
    if i > max:
        max = i
        large.append(i)

print(max)
print(large)
print('second largest:',large[0])
-----------------------------------------------
# 12) Python program to find N largest elements from a list
l = [11,2,3,67,0,78,-1,3,44]
 # first approach
l.sort(reverse=True)
print(l)
n = int(input('Enter a number :'))
print('The',n,'th','largest is : ',l[:n])

# second approach by using for loop
list = [11,22,1,2,5,67,21,32]
n= int(input('enter how many largest elements are required: '))
list.sort(reverse=True)
print(list)
new_list = []
for  i in range(n):
    new_list.append(list[i])

print(new_list)

# OR by using while loop
list = [11,22,1,2,5,67,21,32]
n= int(input('enter how many largest elements are required: '))
new_list = []
list.sort(reverse=True)
print(list)
i = 0
while i < n:
    new_list.append(list[i])
    i += 1

print(new_list)
-----------------------------------------------
# 13)Python program to print even numbers in a list
list = [11,22,1,2,5,67,21,32]
new = []
# by using for loop
for i in list:
    if i % 2==0:
        new.append(i)

print(new)

# by using while
list = [11,22,1,2,5,67,21,32]
new = []
i = 0
while i < len(list):
    if list[i] % 2 ==0:
        new.append(list[i])
    i += 1
print(new)

# by using list comprehension
list = [11,22,1,2,5,67,21,32]
nw = []
[nw.append(i) for i in list if i%2==0]
print(nw)

# by using lambda
l= [11,22,1,2,5,67,21,32]
print(list(filter(lambda a: (a % 2==0),l)))
-----------------------------------------------
# 14) Python program to print odd numbers in a List
l= [11,22,1,2,5,67,21,32]
list = [11,22,1,2,5,67,21,32]
new = []
# by using for loop
for i in list:
    if i % 2!=0:
        new.append(i)

print(new)

# by using while
list = [11,22,1,2,5,67,21,32]
new = []
i = 0
while i < len(list):
    if list[i] % 2 !=0:
        new.append(list[i])
    i += 1
print(new)

# by using list comprehension
list1 = [11,22,1,2,5,67,21,32]
nw = []
[nw.append(i) for i in list1 if i%2!=0]
print(nw)

# by using lambda
l= [11,22,1,2,5,67,21,32]
print(list(filter(lambda a: (a % 2!=0),l)))
-----------------------------------------------
# 15) Python program to print all even numbers in a range
# by using for loop
start= int(input('enter a starting number: '))
stop= int(input('enter a last number: '))
new = []
for i in  range(start,stop+1):
    if i %2 ==0:
        new.append(i)

print(new)

 # by using range
start= int(input('enter a starting number: '))
stop= int(input('enter a last number: '))
for i in range(start,stop+1,2):
    print(i,end=' ')
-----------------------------------------------
# 16) Python program to print all odd numbers in a range
# by using for loop
start= int(input('enter a starting number: '))
stop= int(input('enter a last number: '))
new = []
for i in  range(start,stop+1):
    if i %2 !=0:
        new.append(i)

print(new)

# by using range
start= int(input('enter only odd starting number: '))
stop= int(input('enter a last number: '))
if start % 2 == 0:
    new_start = start+1
    for num in range(new_start,stop+1,2):
        print(num, end=" ")
else:
    for num in range(start,stop+1,2):
        print(num, end=" ")
        
# by using list comprehension
start= int(input('enter a starting number which is odd only: '))
stop= int(input('enter a last number: '))
new = []
[new.append(i+2) for i in range(start,stop+1,2)]
print(new)
-----------------------------------------------
# 17) Python program to print positive numbers in a list
l = [12, -7, 5, 64, -14]

# by using list comprehension
new = []
[print(i,end = '') for i in  l if (i>0) ]
print('\n')
# or
[new.append(i) for i in  l if (i>0)]
print(new)

# by using for loop
l = [12, -7, 5, 64, -14]
for i in l:
    if i > 0:
        print(i, end= ' ')

# by suing while loop
l = [12, -7, 5, 64, -14]
i = 0
while i < len(l):
    if l[i]> 0:
        print(l[i], end = ' ')
    i += 1

# by using lambda
l = [12, -7, 5, 64, -14]
print(list(filter(lambda a: a>0,l)))
-----------------------------------------------
# 18)Python program to print negative numbers in a list
l = [12, -7, 5, 64, -14]

# by using list comprehension
new = []
[print(i,end = '') for i in  l if (i<0) ]
print('\n')
# or
[new.append(i) for i in  l if (i<0)]
print(new)

# by using for loop
l = [12, -7, 5, 64, -14]
for i in l:
    if i < 0:
        print(i, end= ' ')

# by suing while loop
l = [12, -7, 5, 64, -14]
i = 0
while i < len(l):
    if l[i]< 0:
        print(l[i], end = ' ')
    i += 1

# by using lambda
l = [12, -7, 5, 64, -14]
print(list(filter(lambda a: a<0,l)))
-----------------------------------------------
# 19)Python program to print all positive numbers in a range
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
# by using for loop
for i in range(start,stop+1,1):
    if i >0:
        print(i, end = " ")

# by using list comprehension
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
[print(i, end = " ")for i in range(start,stop+1,1) if i >0 ]

# by using while loop
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
i = 0
while i in range(start,stop+1,1):
    if i >0:
        print(i, end = " ")
    i += 1

start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
l = list(range(start,stop+1))
print(l)
print(list(filter((lambda a: a>0 ), l)))
-----------------------------------------------
# 20)Python program to print all negative numbers in a range
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
# by using for loop
for i in range(start,stop+1,1):
    if i <0:
        print(i, end = " ")

# by using list comprehension
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
[print(i, end = " ")for i in range(start,stop+1,1) if i <0 ]

# by using while loop
start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
i = start
while i in range(start,stop+1,1):
    if i <0:
        print(i, end = " ")
    i += 1

start= int(input('enter  starting number: '))
stop= int(input('enter a last number: '))
l = list(range(start,stop+1))
print(l)
print(list(filter((lambda a: a<0 ), l)))
-----------------------------------------------
# 21) Remove multiple elements from a list in Python
l = [12, -7, 5, 64, -14,11,12,23,-21,34,44]

# by using for loop

# remove even elements
removed_even=[]
for i in l:
    if i > 0:
        if i % 2 == 0:
            l.remove(i)
            removed_even.append(i)

print('new list after even elements removed',l)
print('removed even elemnts list',removed_even)

# list comprehension
l = [11, 5, 17, 18, 23, 50]
[l.remove(i) for i in l if i%2==0]
print('after removal of even elemnts from list:',l)
----------------------------------------------
# 22) Python – Remove empty List from List
l = [5, 6, [], 3, [],[], [], 6,3, 9]

# by using list comprehension
print(list(filter((lambda a:  a!=[]) ,l)))

# by using for loop
list = [5, 6, [], 3, [],[], [], 6,3, 9]
l = []
for  i in list:
    if i != []:
        l.append(i)

print(l)

# by using while loop
list = [5, 6, [], 3, [],[], [], 6,3, 9]
l = []
i = 0
while i < len(list):
    if list[i] != []:
        l.append(list[i])
    i += 1

print(l)
-----------------------------------------------
# 23) Python | Cloning or Copying a list
l = [12, -7, 5, 64, -14]

# by using slicing
new = []
new = l[:]
print(new)

# by using for loop
l = [12, -7, 5, 64, -14]
new=[]
for i in l:
    new.append(i)
print(new)

# by using while
l = [12, -7, 5, 64, -14]
new=[]
i = 0
while i<len(l):
    new.append(l[i])
print(new)

# by using cshallow copy
l = [12, -7, 5, 64, -14]
new = l.copy()
print(new)

# by using deep copy
l = [12, -7, 5, 64, -14]
new = l
print(new)

# by using list comprehension
l = [12, -7, 5, 64, -14]
new = []
[new.append(i) for i in l]
print(new)
-----------------------------------------------
# 24) Python | Count occurrences of an element in a list
l = [2,3,4,5,3,4,6,7,3,3,4,4,2]
# by using count function
print(l.count(2))
print(l.count(3))

# by using for loop
n = int(input('enter the elemnt : '))
count = 0
for i in l:
    if n == i:
        count += 1
print(count)

# by using while loop
n = int(input('enter the elemnt : '))
i = 0
count = 0
while i < len(l):
    if n == l[i]:
        count += 1
    i += 1
print(count)
-------------------------------------------
# 25) Python | Remove empty tuples from a list
tup = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]

l = []
for  i in tup:
    if i != ():
        l.append(i)

print(l)

# by using list comprehension
print(list(filter((lambda a:  a!=()) ,l)))

# by using while loop
list = [5, 6, (), 3, (),(), (), 6,3, 9]
l = []
i = 0
while i < len(list):
    if list[i] != ():
        l.append(list[i])
    i += 1

print(l)
-------------------------------------------
# 26)Python | Program to print duplicates from a list of integers

# by using counter function from counter module
from collections import Counter
l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = Counter(l1)
print(d)

# using count method
l = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
new = []
for i in l:
    n = l.count(i)
    if n > 1 :
        if new.count(i) == 0:
            new.append(i)
print(new)
------------------------------------------
# 27) Python program to find Cumulative sum of a list
l = [10, 20, 30, 40, 50]
# by using for loop
new = []
sum = 0
for i in l:
    sum += i
    new.append(sum)
print(new)

# by using while loop
l = [10, 20, 30, 40, 50]
i = 0
new =[]
sum = 0
while i < len(l):
    sum += l[i]
    new.append(sum)
    i += 1
print(new)

------------------------------------------
# 28)Python | Sum of number digits in List
l = [11, 22, 33, 41, 56]
new = []
for i in l:
    sum = 0
    for j in str(i):
        sum += int(j)
    #print(sum)
    new.append(sum)
print(new)
-----------------------------------------------
# extra one problem for sum of digits of number
n=123
sum=0
while(n>0):
    sum+=n%10
    n=n//10
print("Sum of digits is " ,sum)
-----------------------------------------------
# 29) Break a list into chunks of size N in Python
my_list = ['geeks', 'for', 'geeks', 'like','geeky','nerdy', 'geek', 'love','questions','words', 'life']
n = int(input('enter by how much chunks wants to divide the list'))
output = []
new = []
x = len(my_list)
for i in range(0,x,n):
    new = my_list[i:i+n]
    output.append(new)

print(output)
-----------------------------------------------
# 30)Python | Sort the values of first list using second list

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print('zipped list: ', list(zip(list2,list1)))
z =sorted(zip(list2,list1))
print('Sorted list: ', list(z))
sorted(z)
-----------------------------------------------'''