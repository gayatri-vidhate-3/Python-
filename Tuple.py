'''# 1)Python program to Find the size of a Tuple
Tuple1 = ("A", 1, "B", 2, "C", 3)

# by using inbuilt function__sizeof__
#Python also has an inbuilt __sizeof__() method to determine the space allocation of an object without any additional garbage value.
print(str(Tuple1.__sizeof__()) + ' bytes')
#o/p ==>  72 bytes

# by using inbuilt function getsizeof()
#The sys.getsizeof() function includes the marginal space usage, which includes the garbage collection overhead for the object.
# Meaning it returns the total space occupied by the object in addition to the garbage collection overhead for the spaces being used.
import sys
print(str(sys.getsizeof(Tuple1)) + str(' bytes'))
# o/p ==> 96 bytes
----------------------------------------------------------
# 2)Python – Maximum and Minimum K elements in Tuple
tup = (5, 20, 3, 7, 6, 8)
new_tup = (sorted(tup))
print(new_tup)
print(type(new_tup))
n = int(input('enter how many max and min elemnts required from tuple'))
print(tuple(new_tup[:n] + new_tup[-n:]))
----------------------------------------------------------
# 3) Create a list of tuples from given list having number and its cube in each tuple
list1 = [1, 2, 3]

# by using for loop and zip
cube =[]
for i in list1:
    cube.append(i**3)
print(cube)
print(list(zip(list1,cube)))

# by using list comprehension
list1 = [1, 2, 3]
res = [(val, pow(val, 3)) for val in list1]
print(res)
----------------------------------------------------------
#4) Python – Adding Tuple to List and vice – versa
list1 = [5, 6, 7]
tup = (1,2)

# adding tuple to list
x = list1+list(tup)
print(x)

# adding list to tuple
y = tuple (list(tup) + list1)
print(y)
----------------------------------------------------------
# 5) Python – Closest Pair to Kth index element in Tuple
----------------------------------------------------------
#6) Python – Join Tuples if similar initial element
# Input : test_list = [(5, 6), (6, 7), (6, 8), (6, 10), (7, 13)]
# Output : [(5, 6), (6, 7, 8, 10), (7, 13)]
----------------------------------------------------------

# 7) Python – Extract digits from Tuple list
# Input : test_list = [(15, 3), (3, 9)]
# Output : [9, 5, 3, 1]

# static
list = [(15, 3), (3, 9),(11,2),(11,6)]
temp1=[]
temp2 =[]
for i in list:
    temp1.append(i[0])
    temp1.append(i[1])

new = []
[temp2.append(x) for x in str(temp1)]
#print(temp2)
for i in temp2:
    if i.isdigit():
        new.append(i)

print(set(new))

# dynamic and most appropriate
a=[(15, 3), (3, 9)]
b=[]
for i in a:
    for j in str(i):
        if j.isdigit() and int(j) not in b:
            b.append(int(j))
print(b)
----------------------------------------------------------
# 8)Python – All pair combinations of 2 tuples
# Input : test_tuple1 = (9, 2), test_tuple2 = (7, 8)
# Output : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8, 2)]

tuple1 = (9, 2)
tuple2 = (7, 8)

key1 =[]
key2= []
new = []
for i in tuple1:
    for j in tuple2:
        new.append((i,j))
        new.append((j,i))

print(sorted(new))
----------------------------------------------------------
# 9)Python – Remove Tuples of Length K
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3
# Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)]

l = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = int(input('Enter what should be the length of tuple to get removed: '))

# by using for loop
for i in l:
    if len(i) ==k:
        l.remove(i)
print(l)

# by using lambda
l = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = int(input('Enter what should be the length of tuple to get removed: '))

print(list(filter(lambda x: len(x) != k, l)))
----------------------------------------------------------
# 10)Sort a list of tuples by second Item
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
#
# Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
# Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]

l = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# l = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
(x) = [(i[0],i[1]) for i in l]
print('Old:', x)
l.sort(key=lambda a:a[1])
print('New:', l)
----------------------------------------------------------
# 11) Python program to Order Tuples using external List
# Input : test_list = [(‘Gfg’, 10), (‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)],
# ord_list = [‘Geeks’, ‘best’, ‘CS’, ‘Gfg’]
# Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)]

test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'CS', 'Gfg', 'best']
new = []
test_list = dict(test_list)
for i in ord_list:
    new.append((i,test_list[i]))

print(new)
----------------------------------------------------------
# 12)Python – Flatten tuple of List to tuple
# Input : test_tuple = ([5], [6], [3], [8])
# Output : (5, 6, 3, 8)
tuple1 = ([5], [6], [3], [8])
new = []
for i in str(tuple1):
    if i.isdigit():
        new.append((i))

print(new)
print(tuple(map(int,new)))   # used to convert string to int
----------------------------------------------------------
# 13) Python – Convert Nested Tuple to Custom Key Dictionary
# Input : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’, ‘value’, ‘id’]
# Output : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]
#
# Input : test_tuple = test_tuple = ((1, ‘Gfg’), (2, 3)), keys = [‘key’, ‘value’]
# Output : [{‘key’: 1, ‘value’: ‘Gfg’}, {‘key’: 2, ‘value’: 3}]

# res = [{key: val for key, val in zip(keys, sub)}for sub in test_tuple]
# print(res)

#static approach but as per the requirement
a = ((1, 'Gfg', 2), (3, 'best', 4))
keys = ['key', 'value', 'id']
#Output =[{'key': 1, 'value': 'Gfg', 'id': 2}, {'key': 3, 'value': 'best', 'id': 4}]
d=dict(zip(keys,a[0]))
e=dict(zip(keys,a[1]))
print(d)
print(e)
f=[d,e]
print(f)

#dynamic approach
test_tuple = ((1, 'Gfg', 2), (3, 'best', 4))
keys = ['key', 'value', 'id']
new = []
for sub in test_tuple:
    for key, val in zip(keys, sub):
        new.append({key: val})   # not correct
print(new)
----------------------------------------------------------'''