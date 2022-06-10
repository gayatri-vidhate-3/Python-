'''# 1) Python – Extract Unique values dictionary values
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
print(test_dict)
#print(test_dict.values())
new = []
for i in test_dict.values():
    for j in i:
        new.append(j)
print(list(set(new)))
--------------------------------------------
# 2)Python program to find the sum of all items in a dictionary
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600
input = {'a': 100, 'b':200, 'c':300}
#print((input.values()))
new =[]
for i in input.values():
    new.append(i)

print(sum(new))

# by using for loop
input = {'a': 100, 'b':200, 'c':300}
sum = 0
for i in input.values():
    sum = sum + i
print(sum)
--------------------------------------------
# 3)Python | Ways to remove a key from dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
print(test_dict)

# by using del
del test_dict['Mani']
print(test_dict)

# by using pop
test_dict.pop('Anuradha','No key found')
print(test_dict)

# by uisng items comprehension
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
res={key:value for key,value in test_dict.items() if key != 'Mani'}
print(res)
--------------------------------------------
#4) Ways to sort list of dictionaries by values in Python – Using itemgetter
lis = [{ "name" : "Nandini", "age" : 20}, { "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]
print(lis)

from operator import itemgetter
print(('after sorting by name ', sorted(lis,key = itemgetter('name'))))

print(sorted(lis,key = itemgetter('age','name')))

print ("The list printed sorting by age in descending order: ")
print(sorted(lis,key=itemgetter('age','name'),reverse=True))
--------------------------------------------
# 5)Ways to sort list of dictionaries by values in Python – Using lambda function
lis = [{ "name" : "Nandini", "age" : 20}, { "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]
print(lis)
print ("The list printed sorting by age: ")
x = sorted(lis,key= lambda i:i['age'])
print(x)

print ("The list printed sorting by age and name: ")
y = sorted(lis,key=lambda t:(t['age'], t['name']))
print(y)

print ("The list printed sorting by age in descending order: ")
z = sorted(lis,key=lambda a:a['age'],reverse=True)
print(z)
--------------------------------------------
# 6) Python | Merging two Dictionaries
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# merge dict using update() method
dict1.update(dict2)
print(dict1)

# code to merge dict using a single expression
new = {*dict1,*dict2}       #output==>{'a', 'b', 'c', 'd'}  not coorect
print(new)
new1 = {**dict1,**dict2}     #output ==>{'a': 10, 'b': 8, 'd': 6, 'c': 4}
print(new1)
--------------------------------------------
# 7)Python – Convert key-values list to flat dictionary
# The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]}
# Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}
dict1 = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
print(dict)

res = dict(zip(dict1['name'],dict1['month']))
print(res)
--------------------------------------------
#8) Python – Insertion at the beginning in OrderedDict
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

from collections import OrderedDict
dict1 = {'a':1, 'b':2}
dict1_ordered = OrderedDict(dict1)

dict1_ordered.update({'c': 3})
dict1_ordered.move_to_end('c',last=False)
print(dict1_ordered)
--------------------------------------------
# 9) Python | Check order of character in string using OrderedDict( )
--------------------------------------------
# 10)Dictionary and counter in Python to find winner of election
# Input :  votes[] = {"john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"};
# Output : John
votes ={'john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john'}

# normal method # but here john and johny having same votes but it gives o/p johny instead of john so not correct
print('The winner is:', max(votes))

# by using counter
from collections import Counter
votes =['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']
#it must be list/tuple not set/string
votes_counts = Counter(votes)
print(votes_counts)
max_votes = max(votes_counts.values())
x = [i for i in votes_counts.keys() if votes_counts[i]==max_votes]
print(x)
print(x[0])
--------------------------------------------
# 11)Python – Append Dictionary Keys and Values ( In order ) in dictionary
# nput : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]
# Explanation : All the keys before all the values in list.

test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
value = test_dict.values()
key = test_dict.keys()
new = []
for i in key:
    new.append(i)
for j in value:
    new.append(j)
print(new)

# another approach by list comprehension
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
new = []
value = test_dict.values()
key = test_dict.keys()
x = [new.append(i) for i in key ]
y = [new.append(j) for j in value]
print(new)

# by lambda
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
new = []
value = test_dict.values()
key = test_dict.keys()
list(map(lambda a:new.append(a),key))
list(map(lambda b:new.append(b),value))
print(new)

#simple approach
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
print(list(test_dict.keys())+list(test_dict.values()))
--------------------------------------------
# 12)Python | Sort Python Dictionaries by Key or Value
key_value = {}
# Initialize value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(key_value)

# sorting by keys using sorted function
print(sorted(key_value.values()))
for i in sorted(key_value.keys()):
    print((i,key_value[i]))
print('###############################################')

# Sorting the Keys and Values in alphabetical using the value
print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))

# sorting by keys using OrderedDict

from collections import OrderedDict
x = OrderedDict(sorted(key_value.items()))
print(x)
--------------------------------------------
# 13)Python – Sort Dictionary key and values List
# Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}
# Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]}
test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
print(test_dict)
new_dict = []
for i in sorted(test_dict.keys()):
    new_dict.append((i,sorted(test_dict[i])))

print(dict(new_dict))
--------------------------------------------
# 14) Handling missing keys in Python dictionaries
# initializing Dictionary
d = { 'a' : 1 , 'b' : 2 }
#print(d['c'])    # it will generate KeyError: 'c'
# therefore to handle the mjssing value below are the some approaches

# by using get
country_code = {'India' : '0091','Australia' : '0025','Nepal' : '00977'}
print(country_code)
print(country_code.get('India','Not Found'))
print(country_code.get('Japan','Not Found'))   # instead of error it will put the msg as not found

# : Using setdefault()
country_code = {'India' : '0091','Australia' : '0025','Nepal' : '00977'}
print(country_code)
print(country_code.setdefault('India','Not Found'))
print(country_code.setdefault('Japan','Not Found'))
--------------------------------------------
# 15) Python dictionary with keys having multiple inputs
import random as rn

# creating an empty dictionary
dict1 = {}

# Insert first triplet in dictionary
x,y,z = 10,20,30
dict1[x,y,z] = x + y - z

# Insert second triplet in dictionary
a,b,c = 5,2,4
dict1[a,b,c]=a*b-c

# print the dictionary
print(dict1)
--------------------------------------------
# 16) Print anagrams together in Python using List and Dictionary
# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'
--------------------------------------------
# 17) K’th Non-repeating Character in Python using List Comprehension and OrderedDict
# Input : str = geeksforgeeks, k = 3
# Output : r
# First non-repeating character is f,
# second is o and third is r.
###############################################
# unble to solve by dict way
###########################################
string = 'geeksforgeeks'
list = []
n = int(input('Enter the required kth non repeating values number: '))
for i in string:
    if i not in list:
        list.append(i)
    else:
        list.remove(i)

print(list[n-1])
--------------------------------------------
# 18) Check if binary representations of two numbers are anagram

# this is the code to check if two strings are anagram or not
from collections import Counter
str1 = input("Enter the First String = ")
str2 = input("Enter the Second String = ")
if(Counter(str1) == Counter(str2)):
    print("Two Strings are Anagrams")
else:
    print("Two Strings are not Anagrams")

# correct code for binary anagram
from collections import Counter
num1 = int(input('ENter a num1'))
num1 = bin(num1)[2:]
num2 = int(input('ENter a num2'))
num2 = bin(num2)[2:]
print(num1)
print(num2)

# append zeros in shorter string
zeros = abs(len(num1)-len(num2))
if (len(num1)>len(num2)):
    num2 = zeros * '0' + num2
else:
    num1 = zeros * '0' + num1

if (Counter(num1) == Counter(num2)):
    print("Two Strings are Anagrams")
else:
    print("Two Strings are not Anagrams")
--------------------------------------------
# 19)Python Counter to find the size of largest subset of anagram words
# Input:
# ant magenta magnate tan gnamate
# Output: 3
# Explanation
# Anagram strings(1) - ant, tan
# Anagram strings(2) - magenta, magnate,
#                      gnamate
# Thus, only second subset have largest
# size i.e., 3

from collections import Counter
input = 'ant magenta magnate tan gnamate'
input= input.split(" ")
print(input)

for i in range(0,len(input)):
    input[i]=''.join(sorted(input[i]))
    print(input[i])
    freqDict = Counter(input)

print(freqDict)
print (max(freqDict.values()))
--------------------------------------------
# 20) Python | Remove all duplicates words from a given sentence
# Input : Geeks for Geeks
# Output : Geeks for
#
# Input : Python is great and Java is also great
# Output : is also Java Python and great
input = 'Geeks for Geeks'
input = input.split(" ")
print(input)

for i in range(len(input)-1):
    if input[i] in input:
        x = ''.join(input[i])

    print(x, end = ' ')
--------------------------------------------
# 21) Python Dictionary to find mirror characters in a string
# change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
# Input : N = 3
#         paradox
# Output : paizwlc
# We mirror characters from position 3 to end.

s = 'paradox'
n = int(input('Enter a number'))

alph = 'abcdefghijklmnopqrstuvwxyz'
alph_reverse = 'zyxwvutsrqponmlkjihgfedcba'
new = dict(zip(alph,alph_reverse))
print(new)
prefix = s[0:n-1]
suffix = s[n-1:]
mirror = ''
for i in range(0,len(suffix)):
    mirror += new[suffix[i]]

print(prefix+mirror)
--------------------------------------------
# 22) Counting the frequencies in a list using dictionary in Python
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
#                   4, 4, 4, 2, 2, 2, 2]
# Output : 1 : 5
#          2 : 4
#          3 : 3
#          4 : 3
#          5 : 2
input = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

#first approach by me
from collections import Counter
total = Counter(input)
print(total)
for i in dict(total):
    print(i,':', total[i])


# geeks for geeks approach
count = {}
for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1 ,4, 4, 4, 2, 2, 2, 2]:
    count[i] = count.get(i, 0) + 1
print(count)
--------------------------------------------
#23) Python | Convert a list of Tuples into Dictionary
# Input : [('A', 1), ('B', 2), ('C', 3)]
# Output : {'B': [2], 'A': [1], 'C': [3]}
input = [('A', 1), ('B', 2), ('C', 3)]

# simplest way
print(dict(input))
d = {}

# second approach
for i in input:
    d[i[0]] = ([i[1]])
print(d)

--------------------------------------------
# 24)Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
# Input : s1 = ABHISHEKsinGH
#       : s2 = gfhfBHkooIHnfndSHEKsiAnG
# # Output : Possible
# Input : s1 = Hello
#       : s2 = dnaKfhelddf
# Output : Not Possible

#s1 = 'ABHISHEKsinGH'
#s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

s1 = 'Hello'
s2 = 'dnaKfhelddf'

from collections import Counter
dict1 = Counter(s1)
dict2 = Counter(s2)
print(dict1)
print(dict2)

result = dict1 & dict2
print(result)
if result == dict1:
    print('Possible')
else:
    print('Not POssible')
--------------------------------------------
# 25) Python dictionary, set and counter to check if frequencies can become same
# Input  : str = “xyyz”
# Output : Yes
# Input : str = “xxxxyyzz”
# Output : No

str = 'xyyz'
#str = 'xxxxyyzz'
from collections import Counter
x = Counter(str)
print(x)
print(set(x))
same = list(set(x.values()))
print(same)
if len(same)>2:
    print('No')
elif len(same) ==2 & (same[1]-same[0]>1):
    print('No')
else:
    print('Yes')
--------------------------------------------
# 26)Scraping And Finding Ordered Words In A Dictionary using Python
--------------------------------------------
#27)Possible Words using given characters in Python
# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal.
Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
--------------------------------------------'''
# 28)Python – Keys associated with Values in Dictionary
# Input : test_dict = {‘abc’ : [10, 30], ‘bcd’ : [30, 40, 10]}
# Output : {10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]}
test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}
res = list([test_dict,test_dict.values()])
#print(res)
d = {}
for i in test_dict:
    print(i)
    print(test_dict[i])
    for j in test_dict[i]:
        #print(test_dict[i])
        print(j)
        if j in test_dict[i]:
             d[i] = list([j])

print(d)

# not solved