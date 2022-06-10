'''
# 1) Python program to check if a string is palindrome or not
string = input('Enter a string which wanted to search whether palindrome or not: ')
if string[:] == string[::-1]:
    print(string,'is Palindrome')
else:
    print(string, 'is not Palindrome')

# another approach
string = input('Enter a string which wanted to search whether palindrome or not: ')
rev = "".join(reversed(string))
if string == rev:
    print(string,'is Palindrome')
else:
    print(string, 'is not Palindrome')

# third approach
string = input('Enter a string which wanted to search whether palindrome or not: ')
w = ""
for i in string:
    w += i

#print(w)
if string == w:
    print(string,'is Palindrome')
else:
    print(string, 'is not Palindrome')
-----------------------------------------------------------------
# 2) Python program to check whether the string is Symmetrical or Palindrome
# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome
#
# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome
string = input('Enter a string which wanted to search whether palindrome or symmetrical: ')
x = len(string)
a = x//2
#print(a)

if string[:(a)] == string[(a):]:
    print(string, 'The entered string is symmetrical')
elif string[:(a)] != string[(a):]:
    print(string, 'The entered string is not symmetrical')

if string[:] == string[::-1]:
    print(string, 'is Palindrome')
else:
    print(string, 'is not Palindrome')
-----------------------------------------------------------------
#3) Reverse words in a given String in Python
# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

string = 'geeks quiz practice code'
words = string.split(' ')
print(words)

# reversed the words
new_string = " "
for i in words:
    new_string = words[::-1]
print(new_string)   # output is like :- ['code', 'practice', 'quiz', 'geeks'] which is not as per the expectations

# used to convert list of strings to string
final_string=" "
for i in new_string:
    final_string += i + ' '
print(final_string)

# second approach which simplest and best
string = 'geeks quiz practice code'
words = string.split(' ')
new = ' '
new = ' '.join(reversed(words))
print(new)
-----------------------------------------------------------------
# 4) Ways to remove i’th character from string in Python
# The original string is : GeeksForGeeks
# The string after removal of i'th character(3rd index) : GeksForGeeks

# first way
string = 'GeeksForGeeks'
n = int(input('Enter the charcters index: '))
new = string[:n] + string[n+1:]
print(new)

# second approach
string = 'GeeksForGeeks'
n = int(input('Enter the charcters index: '))
new = ''
for i in range(len(string)):
    if i != n:
        new += string[i]

print(new,end = '')

# 3rd approach
string = 'GeeksForGeeks'
n = int(input('Enter the charcters index: '))
new_str = ''.join([string[i] for i in range(len(string)) if i != 2])
print(new_str)
-----------------------------------------------------------------
# 5)Python | Check if a Substring is Present in a Given String
MyString1 = "A geek in need is a geek indeed"
MyString2 = "geek"

# first approach
if MyString2 in MyString1:
    print('Yes',MyString2,'is present in',MyString1)

# second approach
MyString1 = "A geek in need is a geek indeed"
MyString2 = "geek"

if (MyString2.find(MyString1) != -1):
    print("NO")
else:
    print("YES")
-----------------------------------------------------------------
# 6) Python – Words Frequency in String Shorthands
# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
#
# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

# first approach simple
#test_str = 'Gfg is best'
test_str = 'Gfg Gfg Gfg'
test_str = test_str.split(' ')
print(test_str)
d = {}
for key in test_str:
    d[key] = test_str.count(key)                        # <==****************************************************

print(d)

# by using counter
from collections import Counter
test_str = 'Gfg is best'
test_str = test_str.split(' ')
x = Counter(test_str)
print(x)
-----------------------------------------------------------------
#7)Python – Convert Snake case to Pascal case
# The original string is : geeksforgeeks_is_best
# The String after changing case : GeeksforgeeksIsBest
string = 'geeksforgeeks_is_best'
s = string.title().replace("_","")
print(s)
-----------------------------------------------------------------
# 8)Find length of a string in python (4 ways)
# Input : ' h e l   l  o '
# Output :14

# by using len
input = ' h e l   l  o '
print(len(input))

# by using for loop
input = ' h e l   l  o '
count = 0
for i in range(len(input)):
    count += 1
print(count)

# by using while loop
input = ' h e l   l  o '
i = 0
counter = 0
while i < len(input):
    counter += 1
    i += 1
print(counter)
-----------------------------------------------------------------
# 09) Python program to print even length words in a string
# Input: s = "This is a python language"
# Output: This
#         is
#         python
#         language
s = "This is a python language"
s = s.split(' ')
for i in s:
    if len(i) %2==0:
        print(i)
-----------------------------------------------------------------
# 10) Python program to accept the strings which contains all vowels
# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'o' are not present
#
# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present
input = 'ABeeIghiObhkUul'
input = input.lower()
print(input)
vowel ={ 'a','e','i','o','u' }
count = 0
for i in vowel:
    if i in input:
        count +=1

if count == len(vowel):
    print('Accepted')
else:
    print('Rejected')
-----------------------------------------------------------------
# 11) Python | Count the Number of matching characters in a pair of string
# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4
str1 = 'abcdef'
str2 = 'defghia'
count = 0
for i in str2:
    if i in str1:
        count += 1
print('The number of matching characters are:', count)
-----------------------------------------------------------------
# 12)Remove all duplicates from a given string in Python
# Input : geeksforgeeks
# Output : efgkors

# first way
input = 'geeksforgeeks'
new = ''
not_in = ""
for i in range(len(input)):
    if (input[i] in input):
        if (input.count(input[i]) > 1):
            new += input[i]
        else:
            not_in += input[i]

final_new = new + not_in
print(final_new)
print(set(final_new))

# second way
input = 'geeksforgeeks'
input = set(input)
print(input)

# third way
input = 'geeksforgeeks'
input = set(input)
new =''
for i in input:
    new = " ".join(i)
    print(new,end='')
-----------------------------------------------------------------
#13) Python – Least Frequent Character in String
# The original string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f
string = 'GeeksforGeeks'
from  collections import  Counter
x = Counter(string)
print(x)
res = min(x,key=x.get)            # <==****************************************************
print(res)
-----------------------------------------------------------------
# 14) Python | Maximum frequency character in String
# The original string is : GeeksforGeeks
# The maximum of all characters in GeeksforGeeks is : e
string = 'GeeksforGeeks'
l = []
for i in string:
    x = string.count(i)
    #print((i,x))
    l.append((i,x))
print(l)
temp = []
for i in l:
    temp.append((i[1],i[0]))
    temp.sort()

print(temp[-1])

print('The maximum of all characters is:',temp[-1][1])
-----------------------------------------------------------------
#15) Python | Program to check if a string contains any special character

string = 'Geeks$For$Geeks'
# string = 'Geeks For Geeks'
l = '[@_!#$%^&*()<>?/\|}{~:]'
for i in string:
    if i in l:
        print("String is not accepted as",i,'is special character present in it')
        break
else:
    print('The string is accpeted as no special character')
-----------------------------------------------------------------
# 16) Generating random strings until a given string is generated
-----------------------------------------------------------------
# 17) Find words which are greater than given length k
# Input : str = "string is fun in python"
#         k = 3
# Output : string python
str = "string is fun in python"
k = int(input('Enter the kth value: '))
str = str.split(" ")
new = []
for i in str:
    if len(i) >k:
        new.append(i)
print(new)
-----------------------------------------------------------------
#18)Python program for removing i-th character from a string
# Input : Peter
#         i = 4
# Output : Pete

# first approach
string = 'Peter'
k = int(input('Enter the kth value: '))
new =""
for i in range(len(string)):
    if i != k :
        new += string[i]

print(new)

# simplest way
string = 'Peter'
k = int(input('Enter the kth value: '))
new =""
new = string[:k] + string[k+1:]
print(new)
-----------------------------------------------------------------
# 19)Python program to split and join a string
# Split the string into list of strings
# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']
#
#
# Join the list of strings into a string based on delimiter ('-')
# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

#1] Split the string into list of strings
# by using for loop
string =  'Geeks for Geeks'
string =string.split()
new = []
for i in string:
    new.append(i)
print(new)

# by using while loop
string =  'Geeks for Geeks'
string =string.split()
new = []
i = 0
while i< len(string):
    new.append(string[i])
    i+= 1

print(new)

# 2]Join the list of strings into a string based on delimiter ('-')
string =['Geeks', 'for', 'Geeks']
new =""
new ="-".join(string)
print(new)
-----------------------------------------------------------------
# 20) Python | Check if a given string is binary string or not
# str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

# string = "01010101010"
# string = "geeks101"
string ="101ggg"
test = '01'
for i in string:
    if i not in test:
        print('No')
        break
else:
    print('Yes')
-----------------------------------------------------------------
#Q21 Python program to find uncommon words from two Strings
# Input : A = "apple banana mango"
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

# first approach
list_A = "apple banana mango orange"
list_B = "banana fruits mango pineapple"
A = list_A.split()
B = list_B.split()

list = []
for i in A:
    if i not in B:
        list.append(i)

for j in B:
    if j not in A:
        list.append(j)

print(list)

# Second Approach
A = "apple banana mango"
B = " banana fruits mango"
new1 = A + B
new1 = new1.split()
print(new1)
new = []
for i in new1:
    print(i)
    if new1.count(i) == 1:
        new.append(i)

print(new)
-----------------------------------------------------------------
# 22) Python – Replace duplicate Occurrence in String
# The original string is : Gfg is best . Gfg also has Classes now. Classes help understand better .
# The string after replacing : Gfg is best . It also has Classes now. They help understand better .
test_str = 'Gfg is best. Gfg also has Classes now. Classes help understand better'

print(str(test_str))

repl_dict = {'Gfg': 'It', 'Classes': 'They'}

# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
test_list = test_str.split(' ')
res = set()

for idx, ele in enumerate(test_list):
    print(idx,ele)
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
-----------------------------------------------------------------
# 23) Python – Replace multiple words with K
# The original string is : Geeksforgeeks is best for geeks and CS
# String after multiple replace : Geeksforgeeks is gfg gfg geeks and gfg
test_str = 'Geeksforgeeks is best for geeks and CS'
test_str= test_str.split(" ")
word_list = ["best", 'CS', 'for']
repl_wrd = 'gfg'
new = " "
for i in test_str:
    #print(i)
    if i not in word_list:
        new += i + " "
    else:
        new += (i.replace(i,'gfg')) + " "

print(new)
-----------------------------------------------------------------
# 24) Python | Permutation of a given string using inbuilt function
# Input :  str = 'ABC'
# Output : ABC
#          ACB
#          BAC
#          BCA
#          CAB
#          CBA
string = 'ABC'
from itertools import permutations
perm = permutations(string)

for i in list(perm):
         print (''.join(i))
-----------------------------------------------------------------
# 25) Python | Check for URL in a String
-----------------------------------------------------------------
#26) Execute a String of Code in Python
# code = """ def factorial(num):
#                for i in range(1,num+1):
#                    fact = fact*i
#                return fact
#            print(factorial(5))"""
# Output:
# 120

def excecute():
    LOC = """
def fact(n):
    i = 1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(fact(5))
    """
    exec(LOC)

excecute()
-----------------------------------------------------------------
 # 27)String slicing in Python to rotate a string
# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"
s = "GeeksforGeeks"
d = 2
new = ''

new = s[d:] + s[0:d]
print('For left Rotation:',new)

new = s[-d:] + s[0:-d]
print('For right Rotation:',new)
-----------------------------------------------------------------
# 28) String slicing in Python to check if a string can become empty by recursive deletion
-----------------------------------------------------------------
# 29)Python Counter| Find all duplicate characters in string
# Input : geeksforgeeeks
# Output : e g k s

string = 'geeksforgeeeks'

new  = {}
for i in string:
    if string.count(i) >1:
        new[i] = string.count(i)

print(new.keys())  # this gives o/p like ==> dict_keys(['g', 'e', 'k', 's'])

# to convert dict of keys to only letters
for i in new.keys():
    print(i, end=" ")

-----------------------------------------------------------------
# 30) Python – Replace all occurrences of a substring in a string
# nput : test_str = “geeksforgeeks”
# s1 = “for”
# s2 = “abcd”
# Output : test_str = “geeksabcdgeeks”
test_str = 'geeksforgeeks'
s1 = 'for'
s2 = 'abcd'

x = test_str.replace(s1,s2)
print(x)
-----------------------------------------------------------------'''