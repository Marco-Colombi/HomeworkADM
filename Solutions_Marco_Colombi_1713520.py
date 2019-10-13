# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python

print("Hello, World!")

# Exercise 2 - Introduction - Python If-Else

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    else:
        print('Not Weird')
    
# Exercise 3 - Introduction - Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    
# Exercise 4 - Introduction - Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# Exercise 5 - Introduction - Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
    
# Exercise 6 - Introduction - Write a function 
# I just returned the boolean values of the conditions provided by the challenge

def is_leap(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

year = int(input())
print(is_leap(year))

# Exercise 7 - Introduction - Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end = "")

# Exercise 8 - Basic data types - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(coordinates)

# Exercise 9 - Basic data types - Find the Runner-Up Score!
#I used a sorted set of arr in order to create a sorted list withouth duplicates and then I printed the runner-up score which correspondes to the element with index = -2.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
    
# Exercise 10 - Basic data types - Nested Lists
#I used a sorted set (so there aren't going to be any duplicates) with every scores' values and then I used it in order to find the names of the students with the second lowest score (which correspondes to the element with index = 1). I also sorted the nested lists by the name variable (the default variable) in order to print the right names in alphabetically order.

if __name__ == '__main__':
    Physics_students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Physics_students.append([name, score])
        scores.append(score) 
    Physics_students.sort()
    for i in range(len(Physics_students)):
        if Physics_students[i][1] == sorted(set(scores))[1]:
            print(Physics_students[i][0])

#Exercise 11 - Basic data types - Finding the percentage
#I created a dictionary which has the names as keys and the scores as items, and then I print the scores' average of the entered guy

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(format(sum(student_marks.get(query_name))/3, '.2f'))
    
# Exercise 12 - Basic data types - Lists
#For every input I checked what command was entered and then I used it

if __name__ == '__main__':
    N = int(input())
    list = []
    for j in range(N):
        command = input().split(" ")
    if command[0] == 'insert':
        list.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(list)
    elif command[0] == 'remove':
        list.remove(int(command[1]))
    elif command[0] == 'append':
        list.append(int(command[1]))
    elif command[0] == 'sort':
        list.sort()
    elif command[0] == 'pop':
        if len(list) != 0:
            list.pop(-1)
    else:
        list.reverse()

# Exercise 13 - Basic data types - Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
    
# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
      return s.swapcase()

f __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    b += '!'
    print("Hello", a, b, "You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[(position + 1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# Exercise 18 - Strings - Find a string
#I just used a for loop which considers every possible string's substring of length of the original substring and I comparate everytime the string's substring with the original substring

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:(i+len(sub_string))] == sub_string:
        count += 1 
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Exercise 19 - Strings - String Validators
# I checked every single word in the string s and I checked every time if it was an alphanumeric (if not I skipped the check of alpha or digit), a lowercase or an uppercase character and I used separate counters to keep track of the character's type that I found

if __name__ == '__main__':
    s = input()
    alnum = 0
    alpha = 0
    digit = 0
    upper = 0
    lower = 0
    for i in s:
        if i.isalnum() == True:
            alnum += 1
            if i.isalpha() == True:
                alpha += 1
            else:
                digit += 1
        if i.islower() == True:
            lower += 1
        if i.isupper() == True:
            upper += 1
    if alnum > 0:
        print('True')
    else:
        print('False')
    if alpha > 0:
        print('True')
    else:
        print('False')
    if digit > 0:
        print('True')
    else:
        print('False')
    if lower > 0:
        print('True')
    else:
        print('False')
    if upper > 0:
        print('True')
    else:
        print('False')
        
# Exercise 20 - Strings - Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
          
# Exercise 21 - Strings - Text Wrap
 import textwrap
          
 def wrap(string, max_width):
  l = textwrap.wrap(string, width = max_width)
  for i in range(len(l)):
    print(l[i])
  return ""
          
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
          
# Exercise 22 - Strings - Designer Door Mat
#I used the variable "h" in order to know the times I had to print the '.I.' string, using two different for loops (both having length = (N//2)) in order to print the first half (where I directly used h) and the second half (where I used (N-h)) of the picture, and in the right middle of the two for loops I just printed the center line with the 'WELCOME' string 
          
NM = input().split(" ")
N = int(NM[0])
M = int(NM[1])
h = 1
for i in range(N//2):
  print(('.|.'*h).center(M, '-'))
  h += 2
print(('WELCOME').center(M, '-'))
h = 2
for i in range(N//2):
  print(('.|.'*(N-h)).center(M, '-'))
  h += 2
          
# Exercise 23 - Strings - String Formatting
# I just used the functions oct(), hex() and bin() in order to find the corresponding octal, hexadecimal and binary numbers of the first 'number' numbers and I printed them with the .rjust() function using len(bin(number)[2::]) as width, because the binary numbers are the first ones to get more digits

def print_formatted(number):
  width = len(bin(number)[2::])
  for i in range(1, number+1):
    print(str(i).rjust(width, " "), str(oct(i)[2:]).rjust(width, " "), (str(hex(i)[2:]).upper()).rjust(width, " "), str(bin(i)[2:]).rjust(width, " "))
          
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Exercise 24 - Strings - Alphabet Rangoli
# I used the list 'a' to keep track of the first half (middle letter included) of each row printed and I increased it everytime with the '-letter' to print in the next row. I also printed the previous specular value of the list 'a' in order to print the second half of each row. I used two different loops to print the first half (middle included) and the second half of the picture.

import string as stg
s = stg.ascii_lowercase

def print_rangoli(size):
  a = []
  a.append(s[size-1])
  print(a[0].center(size*4-3, '-'))
  a.append(str(a[0])+"-"+str(s[size-2]))
  for i in range(1, size):
    print((str(a[i])+"-"+str((a[i-1])[::-1])).center(size*4-3, '-'))
    a.append((str(a[i])+"-"+str(s[size-i-2])))
  for i in range(1, size):
    if i < size-1:
      print((str(a[n-i-1])+"-"+str((a[n-i-2])[::-1])).center(size*4-3, '-'))
    else:
      print(a[0].center(size*4-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Exercise 25 - Strings - Capitalize!
#I turned the string 's' into a list containing each words and the alternating white spaces too and the I used the .capitalize() function in order to capitalize the first letter of each word in the list 's'
          
import math
import os
import random
import re
import sys
          
def solve(s):
  s = s.split(" ")
  for i in range(len(s)):
    s[i] = (s[i].capitalize())
  return " ".join(s)

f __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
          
# Exercise 26 - Strings - The Minion Game
#I created a list containing every vowels and then I checked for each letter in the string if it weren't a vowel or yes: if it weren't, I incremented the Stuart counter with the length of the next n-letters in the string starting from the corresponding consonant found, which correspondes exactly with the numbers of all the possible words that Stuart can create starting from there; if it were, I did the same with the Kevin counter. Then I just checked who has the highest score.
          
 def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
      if vowels.count(string[i]) == 0:
        Stuart += (len(string)-i)
      else:
        Kevin += (len(string)-i)
    if Stuart > Kevin:
      print ('Stuart', Stuart)
    elif Kevin > Stuart:
      print ('Kevin', Kevin)
    else:
      print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Exercise 27 - Strings - Merge the Tools!
#I created the t-i strings using the textrap.wrap() function, and then I used the dict.fromkeys() function in order to remove the duplicates in each t-i strings.

import textwrap
          
def merge_the_tools(string, k):
  t = textwrap.wrap(string, width = k)
  for i in t:
    print("".join(list(dict.fromkeys(i))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Exercise 28 - Sets - Introduction to Sets
          
def average(array):
    return(sum(set(array))/len(set(array)))
          
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
          
# Exercise 29 - Sets - No Idea!
#Every time I checked if and how many times the element-i in the sets A and B figured in the list 'array' using the 'Counter(array)' only because it is faster than a simple 'array.count()' which gave me Runtime Error on the HackerRank site. Than I just added (if it was in the Set A) or subtracted (if it was in the Set B) to the happiness variable the number of times the element-i fiugured in 'array'
          
from collections import Counter
          
nm = list(map(int,input().split()))
array = list(map(int, input().split()))
countarray = Counter(array)
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for i in range(nm[1]):
  if list(A)[i] in countarray:
    happiness += countarray.get(list(A)[i])
  if list(B)[i] in countarray:
    happiness -= countarray.get(list(B)[i])
print(happiness)
          
# Exercise 30 - Sets - Symmetric Difference

M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
for i in sorted(a ^ b):
  print(i)

# Exercise 31 - Sets - Set .add()
          
N = int(input())
s = set()
for i in range(N):
  s.add(input())
print(len(s))
          
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
 
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
  command = list(input().split())
  if command[0] == 'pop':
    s.pop()
  elif command[0] == 'remove':
    s.remove(int(command[1]))
  else:
    s.discard(int(command[1]))
print(sum(s))
          
# Exercise 33 - Sets - Set .union() Operation

n_en = int(input())
en_students = set(map(int, input().split()))
n_fr = int(input())
fr_students = set(map(int, input().split()))
print(len(en_students | fr_students))

# Exercise 34 - Sets - Set .intersection() Operation
          
n_en = int(input())
en_students = set(map(int, input().split()))
n_fr = int(input())
fr_students = set(map(int, input().split()))
print(len(en_students & fr_students))

# Exercise 35 - Sets - Set .difference() Operation
          
n_en = int(input())
en_students = set(map(int, input().split()))
n_fr = int(input())
fr_students = set(map(int, input().split()))
print(len(en_students - fr_students))

# Exercise 36 - Sets - Set .symmetric_difference() Operation

n_en = int(input())
en_students = set(map(int, input().split()))
n_fr = int(input())
fr_students = set(map(int, input().split()))
print(len(en_students ^ fr_students))
          
# Exercise 37 - Sets - Set Mutations
#For every input I checked what command was entered and then I used it 
          
nA = int(input())
A = set(map(int, input().split()))
n = int(input())
for i in range(n):
  command = list(input().split())
  if command[0] == 'update':
    A.update(set(map(int, input().split())))
  elif command[0] == 'intersection_update':
    A.intersection_update(set(map(int, input().split())))
  elif command[0] == 'difference_update':
    A.difference_update(set(map(int, input().split())))
  else:
    A.symmetric_difference_update(set(map(int, input().split())))
print(sum(A))
          
# Exercise 38 - Sets - The Captain's Room
#I checked for every element in the 'sorted(set(l))' (so there aren't going to be duplicates) if it figured only one time inside the 'Counter(l)', (where l is the list containing all the room's number with the duplicates), because the room's number of the Captain figured only one time inside 'l'. I preferred to use the Counter(l) instead of l.count() beacause it was faster and it didn't give me runtime error

from collections import Counter
          
k = int(input())
l = list(map(int, input().split()))
lcount = Counter(l)
s = sorted(set(l))
for i in s:
    if lcount.get(i) == 1:
      print(i)
      break 
          
# Exercise 39 - Sets - Check Subset
#If the length of the difference between set B and set A is equal to the difference of the length of each set, then this means A is a Subset of B
          
T = int(input())
for i in range(T):
  nA = int(input())
  A = set(map(int, input().split()))
  nB = int(input())
  B = set(map(int, input().split()))
  if len(B - A) == nB - nA:
    print('True')
  else:
    print('False')

# Exercise 40 - Sets - Check Strict Superset
#Very similar to the previous one, I only added two things, an other condition where I wanted to check if the length of the difference between set A and set i-B is not equal to 0 (because this is the condition that differentiates a strict subset from a normal subset) and I kept track of the strict subsets' number: if it is equal to the number of all the sets B then every sets B is a strict subest of set A. 
          
A = set(map(int, input().split()))
n = int(input())
count = 0
for i in range(n):
  B = set(map(int, input().split()))
  if len(A - B) == len(A) - len(B) and len(A - B) != 0:
    count += 1
if count == n:
  print('True')
else:
  print('False')
          
# Exercise 41 - Collections - collections.Counter()
# I checked every time if the size wanted by the customer ('size_price[0]') was available using the Counter function, and if it was I added the price of it (size_price[1]) to the money earned by the shoes shop and I removed that size from the store.
          
from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
N = int(input())
money_earned = 0
for i in range(N):
  size_price = list(map(int, input().split()))
  if size_price[0] in Counter(shoes):
    money_earned += size_price[1]
    shoes.remove(size_price[0])
print(money_earned)

# Exercise 42 - Collections - DefaultDict Tutorial
#the first n-elements (nm[0]) were the letters of the group 'A', the next m-elements were the letters of the group 'B' . For every element of the group 'B' I chekced if it was also inside the group 'A' and then I printed in what position it appeared inside the group 'A'.
          
from collections import defaultdict
          
d = defaultdict(list)
nm = list(map(int, input().split()))
for i in range (sum(nm)):
  if i < nm[0]:
    d['A'].append(input())
  else:
    a = input()
    d['B'].append(a)
    if a in d['A']:
      l = [str(i+1) for i in range(len(d['A'])) if a == d['A'][i]]
      print(" ".join(l))
    else:
      print(-1)
          
# Exercise 43 - Collections - Collections.namedtuple()
# I added every time to the sum of the marks the mark of each student and then I did an average of it

from collections import namedtuple
          
N = int(input())
Students = namedtuple('Students', input())
marks_sum = 0
for i in range(N):
  a = list(input().split())
  b = (Students(a[0], a[1], a[2], a[3]))
  marks_sum += int(b.MARKS)
print(format(marks_sum/N, '.2f'))
          
# Exercise 44 - Collections - Collections.OrderedDict()
#I added every time the item entered ('a[0]') as a key and its price ('a[2]') as an item to the OrderedDict 'items'. P.s. 'a[1]' is only a white space, this is why I didn't consider it.
          
from collections import OrderedDict
          
n = int(input())
items = OrderedDict()
for i in range(n):
  a = list(input().rpartition(' '))
  items[a[0]] = items.get(a[0], 0) + int(a[2])
for k in items:
  print(k, items[k])
          
# Exercise 45 - Collections - Word Order
#In words I stored every time the word as a key and the number of times entered as an item, then I printed the lenght of words to know the number of different words entered and I printed for each words how many times it was entered.
          
from collections import OrderedDict
          
n = int(input())
words = OrderedDict()
for i in range(n):
  word = input()
  words[word] = words.get(word, 0) + 1
print(len(words.keys()))
for k in words:
  print(words[k], end = " ")

# Exercise 46 - Collections - Collections.deque()
#For every input I checked what command was entered and then I used it
          
from collections import deque
          
N = int(input())
d = deque()
for i in range(N):
  command = list(input().split())
  if command[0] == 'append':
    d.append(command[1])
  elif command[0] == 'pop':
    d.pop()
  elif  command[0] == 'popleft':
    d.popleft()
  else:
    d.appendleft(command[1])
print(" ".join(d))
          
# Exercise 47 - Collections - Company Logo
#I used the Counter function to know how many times each letter figured in the string s, than I took the times in descending order and I checked to which letters they reffered. I used the counter to stop at the third time in descending order.
          
import math
import os
import random
import re
import sys
          
from collections import Counter

if __name__ == '__main__':
    s = input()
    words = [a for a in s]
    words = Counter(words)   
    counter = 0
    for v in (sorted(set(words.values()))[::-1]):
      for k in sorted(words.keys()):
        if words.get(k) == v:
          print (k, v)
          counter += 1
        if counter == 3:
          break
      if counter == 3:
        break
          
# Exercise 48 - Collections - Piling Up!

from collections import deque

def pilingcubes(T,N):
  d = deque(list(map(int, input().split())))
  maximum = max(d)                 #I take the maximum value inside the deque
  for i in range(N):
    if d[0] > d[-1]:               #I take the biggest value between the leftmost and the rightmost element
      if d[0] <= maximum:          #I compared it to the maximum value
        maximum = d[0]             #If it's smaller than the maximum I turned the maximum into it for the next iteration
        d.popleft()                #I removed it, so for the next iteration it will no longer be inside the dequer
      else:
        return 'No'                #If it's bigger I end the function beacause it's not possible to stack the cubes
    else:
      if d[-1] <= maximum:
        maximum = d[-1]
        d.pop()
      else:
        return 'No'
  return 'Yes'                      #If all the iterations went good it's possible to stack the cubes

T = int(input())
for t in range(T):
  N = int(input())
  print(pilingcubes(T, N))
          
# Exercise 49 - Date time - Calendar Module
#I used the .weekday() to know what day it was (in terms of number) and I converted to its name using the .day_name() function.
          
import calendar
date = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].upper())
          
# Exercise 50 - Date time - Time Delta
# I used the .striptime() function to convert the two different timestamps and I converted the difference between them using the .totalseconds() function
          
import math
import os
import random
import re
import sys
from datetime import datetime
from datetime import timedelta

def time_delta(t1, t2):
  return str(int(abs((datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")-datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")).total_seconds())))
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Exercise 51 - Errors and Exceptions - Exceptions

T = int(input())
for i in range(T):
  try:
    ab = list(map(int, input().split()))   
  except ValueError as e:
    print("Error Code:", e)
    continue                             #If the first error occurred, I will not pass through the second one
  try: 
    print(ab[0]//ab[1])
  except ZeroDivisionError as e:
    print ("Error Code:", e)
          
# Exercise 52 - Built-ins - Zipped!
          
NX = list(map(int, input().split()))
marks = []
for i in range(NX[1]):
  marks.append(list(map(float, input().split())))  #I stored all the marks of different subjects into this nested lists
for x in zip(*marks):                     #I iterate over each marks obtained by each students
  print(format(sum(list(x))/NX[1], '.1f'))  

# Exercise 53 - Built-ins - Athlete Sort
#In order to order each athlete using the key 'k' I used the command key = lambda x: x[k]
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr = sorted(arr, key = lambda x: x[k])
    for athlete in arr:
      print(" ".join(map(str, athlete)))
          
# Exercise 54 - Built-ins - Ginorts
          
S = input()
uppercase = []
lowercase = []
digitodd = []
digiteven = []
for x in S:
  if x.isupper() == True:
    uppercase.append(x)      #Here I stored every uppercase letters
  elif x.islower() == True:
    lowercase.append(x)      #Here I stored every lowercase letters
  else:
    if int(x) % 2 != 0:
      digitodd.append(x)     #Here I stored every odd digit
    else:
      digiteven.append(x)    #Here I stored every even digit
lowercase.sort()             #I sort evere list that I've created before
uppercase.sort()         
digitodd.sort()
digiteven.sort()
print(''.join(lowercase)+''.join(uppercase)+''.join(digitodd)+''.join(digiteven)) #The I printed in the rigth order

# Exercise 55 - Map and lambda function
          
cube = lambda x: x**3       #I computed the cubes of each element

def fibonacci(n):
    if n == 0:              #For the first 3cases I created the appropriate list 
      l = []
      return l
    if n == 1:
      l = [0]
      return l
    elif n == 2:
      l = [0, 1]
      return l
    else:                    
      l = [0, 1]                #This list will contain the first n fibonacci numbers
      a = 0
      b = 1
      for i in range(2, n):     #For the next ones I used this for loop 
            if a < b:           #where I incremented the smaller between a and b and the appended it to the list
                a += b
                l.append(a)
            else:
                b += a
                l.append(b)
      return l
      

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Exercise 56 - Regex - Detect Floating Point Number
          
import re
T = int(input())
for i in range(T):
  N = input()
  floating_number = re.match(r'[+-]?\d*\.\d+$', N) #This regex wil find out every match with a floating number
  if floating_number:                           #If I found out a match then I will print 'True' or, if not, I will print 'No'
    print('True')
  else:
    print('False')

# Exercise 57 - Regex - Re.split()

regex_pattern = r"[.,]"

import re
print("\n".join(re.split(regex_pattern, input())))
          
# Exercise 58 - Regex - Group(), Groups() & Groupdict()
# I looked for the first match of an alphanumeric character followed by itself (\1)
          
import re
S = input()
alphanumeric = re.search(r'([a-zA-Z0-9])\1', S) 
if alphanumeric:               #If there was a match, I printed the first group of it, if there wasn't I printed (-1)
  print(alphanumeric.group(1)) 
else:
  print(-1)                   

# Exercise 59 - Regex - Re.findall() & Re.finditer()
#For this challenge I used both the positive lookabove and lookbehind in order to find 2 or more vowels between consonants
          
import re
S = input()
vowels = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', S, re.I)
if vowels:                   
  for x in vowels:
    print (x)
else:
  print(-1)

# Exercise 60 - Regex - Re.start() & Re.end()
#For this one I couldn't solve it whithout looking to the discussions section
          
import re
S = input()
k = input()
pattern = re.compile(k)              #I first created a pattern = k
match = pattern.search(S)            #The I looked for a match with this pattern
if match:                            #If there was 
  while match:                       #I created a loop that iterates for every match that is possible to find out
      a = (match.start(), match.end()-1)   #I created a tuple with the start and the end of each match
      print(a)                             #I printed the tuple
      match = pattern.search(S, match.start()+1)#For the next match I will look over S starting from the current match
else:                                 
  print('(-1, -1)') 

# Exercise 61 - Regex - Regex Substitution
#Even for this one I helped myself with looking to the discussion section in order to know how to write the repl inside the re.sub function. I used both the positive lookahead and the positive behind in order to find the right match they asked for
          
import re                            
N = int(input())
for i in range(N):
  a = input()       #I checked every single line 
  match = re.sub(r'(?<=\s)(&{2}|\|{2})(?=\s)', lambda x: 'and' if x.group(0)== '&&' else 'or', a)
  if match:   #If I found out a match for that line I printed it with the right substiutions
    print(match)
  else:       #If not, I'll print it as it was entered
    print(a)

# Exercise 62 - Regex - Validating Roman Numerals
         
regex_pattern = r"M{0,3}(C{1,3}[M,D]|D?C{0,3}L?)(X{1,3}[CL]|X{0,3}V?)(I{1,3}[XV]|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# Exercise 63 - Regex - Validating phone numbers
#For every phone numbers I just checked if there was or not a match, knowing that a phone number must begin with a digt in the range [7-9] and it must be followed by only other 9 digits
          
import re
N = int(input())
for i in range(N):
  S = input()
  phone = re.match(r'[7-9]\d{9}$', S)
  if phone:
    print("YES")
  else:
    print("NO")

# Exercise 64 - Regex - Validating and Parsing Email Addresses
#for each email address I checked if it matches the pattern's rules written excluding the '<' and the '>' characters in order to print the email address using the .formataddr(()) function provided by the challenge
          
import re
import email.utils
n = int(input())
for i in range(n):
  s = input().split()
  address = re.search(r'(?<=<)([a-z][\-\w\.]+@[a-z]+\.[a-z]{1,3})(?=>)', s[1], re.I) 
  if address:
    print (email.utils.formataddr((s[0], address.group(0))))

# Exercise 65 - Regex - Hex Color Code
#For each line I checked if there was a match, if it there was I printed it. I also used a negative lookbehind to not match alphanumeric characters at the beginning of each line
          
import re
N = int(input())
for i in range(N):
  a = input()
  match = re.findall(r'(?<!^)#(?:[\da-f]{3}){1,2}', a, re.I)
  if match:
    for x in match:
      print(x)

# Exercise 66 - Regex - HTML Parser - Part 1
          
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):       
        print("Start :", tag)                     
        for attr in attrs:                       #If there are any attributes I'll print them using the format provided
          print('->', attr[0], '>', attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:                       #If there are any attributes I'll print them using the format provided
          print('->', attr[0], '>', attr[1])

parser = MyHTMLParser()
N = int(input())
for i in range(N):
  parser.feed(input())

# Exercise 67 - Regex - HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    if len(data.split('\n')) > 1:          #If the list made by splitting each data string by '\n' has a length > 1
      print(">>> Multi-line Comment")      #This means that is a Multi-line comment
    else:
      print(">>> Single-line Comment")     #Otherwise means that is a Single-line comment
    print(data)
  
  def handle_data(self, data):
    if data != '\n':                       #I printed only the data not equal to '\n'
      print(">>> Data")
      print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
         
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):   #I considered only the start tags in order to avoid duplicates
    print(tag)
    for attr in attrs:                     #If there are any attributes I'll print them using the format provided
      print('->', attr[0], '>', attr[1])

parser = MyHTMLParser()
N = int(input())
for i in range(N):
  parser.feed(input())

# Exercise 69 - Regex - Validating UID
#For this one too I helped myself with looking to the discussions section, especially for the "".join(sorted(UID)) trick
          
import re
T = int(input())
for i in range(T):
  UID = input()
  if len(UID) == 10:  #I checked that the lenght of the UID is equal to 10
    a = re.search(r'[A-Z]{2,}', "".join(sorted(UID))) #I checked that UID contains at least 2 uppercase letters      
    b = re.search(r'\d{3,}', "".join(sorted(UID)))  #I checked that UID contains at least 3 digits
    c = not re.search(r'[^A-Z^\d]', "".join(sorted(UID)), re.I) #I checked that UID doesn't contain anything else than alphanumeric characters
    d = not re.search(r'(.)\1', "".join(sorted(UID))) #I checked that UID doesn't contain repetitive characters
    if a and b and c and d: #If all the previous conditions are accepted then the UID is valid
      print('Valid')
    else:
      print('Invalid')
  else:
    print('Invalid')
          
# Exercise 70 - Regex - Validating Credit Card Numbers
          
import re
N = int(input())
for i in range(N):
  card_number = input()
  a = re.match(r'^[4-6]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$', card_number) #I checked that the credit card number contains exactly characters with groups of maximum four digits
  b = not re.search(r'(\d)-?\1-?\1-?\1', card_number) #I checked that the credit card doesn't contain 4 or more consecutive digits
  if a and b: #If all the previous conditions are accepted then the UID is valid
    print('Valid')
  else:
    print('Invalid')

# Exercise 71 - Regex - Validating Postal Codes
          
regex_integer_in_range = r"^\d{6}$"  #matches a pattern made of exactly 6 digits
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  #matches all the alternating repetitive digit pairs

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Exercise 72 - Regex - Matrix Script

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
          
Coded_script = ''
for column in zip(*matrix):       #I took all the columns of the matrix
  Coded_script += "".join(column) #And I added them to this string, which represents the coded script written over one line
Decoded_script = re.sub(r'(?<=\w)([^\w]+)(?=\w)',  " ", Coded_script) #Than I substituted all the non alphanumeric characters between two words with a white space
print(Decoded_script)
          
# Exercise 73 - Xml - XML 1 - Find the Score
          
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
  n = 0
  for attr in node.iter(): #I checked every child of the root
    n += len(attr.attrib)  #and I added the number of attributes found in each child
  return n

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
          
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth
          
import xml.etree.ElementTree as etree
          
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1            #I incremented the level by 1 for each recursion (so in the first one it will be 0, the minimum)
    if level > maxdepth:  #If the level is greater than the maximum depth
      maxdepth = level    #this means that this level is the actual maximumdepth found out until now
    for child in elem:    #Than I just used a recursive function that work until there is another child
      depth(child, level) 

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
          
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators 
#didn't do it
# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory
#didin't do it
# Exercise 77 - Numpy - Arrays
          
import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Exercise 78 - Numpy - Shape and Reshape

import numpy
          
arr = numpy.array(list(map(int, input().split())))
print(numpy.reshape(arr, (3,3)))

# Exercise 79 - Numpy - Transpose and Flatten
          
import numpy
          
NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
arr = []
for i in range(N):
  column = list(map(int, input().split()))
  arr.append(column)
arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())

# Exercise 80 - Numpy - Concatenate
          
import numpy 
          
NMP = list(map(int, input().split()))
N = NMP[0]
M = NMP[1]
P = NMP[2]
array_1 = []
array_2 = []
for i in range(N+M):
  if i < (N-1):
    array_1.append(list(map(int, input().split())))
  else:
    array_2.append(list(map(int, input().split())))
array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)
print(numpy.concatenate((array_1, array_2), axis = 0))

# Exercise 81 - Numpy - Zeros and Ones
          
import numpy
          
dimensions = list(map(int, input().split()))
print(numpy.zeros(dimensions, dtype = numpy.int))
print(numpy.ones(dimensions, dtype = numpy.int))

# Exercise 82 - Numpy - Eye and Identity

import numpy
          
numpy.set_printoptions(legacy='1.13')
NM = list(map(int, input().split()))
print(numpy.eye(NM[0], NM[1]))
          
# Exercise 83 - Numpy - Array Mathematics
          
import numpy
          
NM = list(map(int, input().split()))
l_a = []
l_b = []
for i in range(NM[0]*2):
  if i < NM[0]:
    l_a.append(list(map(int, input().split())))
  else:
    l_b.append(list(map(int, input().split())))
a = numpy.array(l_a)
b = numpy.array(l_b)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))

# Exercise 84 - Numpy - Floor, Ceil and Rint
          
import numpy
          
numpy.set_printoptions(sign=' ')
a = numpy.array(list(map(float, input().split(" "))))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
          
# Exercise 85 - Numpy - Sum and Prod
          
import numpy
          
NM = list(map(int, input().split()))
arr = []
for i in range(NM[0]):
  arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
print(numpy.prod(numpy.sum(arr, axis = 0)))
          
# Exercise 86 - Numpy - Min and Max
          
import numpy
          
NM = list(map(int, input().split()))
arr = []
for i in range(NM[0]):
  arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
print(numpy.max(numpy.min(arr, axis = 1)))
          
# Exercise 87 - Numpy - Mean, Var, and Std
          
import numpy
          
numpy.set_printoptions(legacy = '1.13')
NM = list(map(int, input().split()))
arr = []
for i in range(NM[0]):
  arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))

# Exercise 88 - Numpy - Dot and Cross
          
import numpy
          
N = int(input())
a = []
b = []
for i in range(N*2):
  if i < N:
    a.append(list(map(int, input().split())))
  else:
    b.append(list(map(int, input().split())))
a = numpy.array(a)
b = numpy.array(b)
print(numpy.dot(a,b))
          
# Exercise 89 - Numpy - Inner and Outer
          
import numpy
          
a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a,b))
print(numpy.outer(a,b))

# Exercise 90 - Numpy - Polynomials
          
import numpy
          
polynomial = numpy.array(input().split(), float)
x = int(input())
print(numpy.polyval(polynomial, x))

# Exercise 91 - Numpy - Linear Algebra
          
import numpy
          
N = int(input())
matrixA = []
for i in range(N):
  matrixA.append(list(map(float, input().split())))
matrixA = numpy.array(matrixA)
print(round(numpy.linalg.det(matrixA), 2))

# ===== PROBLEM2 =====

# Exercise 92 - Challenges - Birthday Cake Candles
          
import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
  return ar.count(max(ar)) #for this one I just used the easy and fast .count() and .max() functions in order to solve the challenge  
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
          
# Exercise 93 - Challenges - Kangaroo
#I checked what Kangaroo is going to start at an advantage and if it was slower than the other one. If it was, I added for each iteration their speed to their position until the faster one reached or outmatched the slower one. 
          
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
  if x1 > x2 and v2 > v1: 
    while x1 > x2 :
      x1 += v1
      x2 += v2
      if x1 == x2 :      #In the case they are the same position at the same time I will return Yes 
        return 'YES'
  elif x1 < x2 and v2 < v1:
    while x2 > x1 :
      x1 += v1
      x2 += v2
      if x1 == x2:
        return 'YES'    
  elif x1 == x2 :        #This is the only case that doesn't need an iteration
    return 'YES'
  return 'NO'            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Exercise 94 - Challenges - Viral Advertising
#For each day I calculated the people who liked the product, which is given by int(shared/2), and added it to the total of likes and then I just multiplied the likes of the day for three to know the total of people who knew about the product
          
import math
import os
import random
import re
import sys

def viralAdvertising(n):
  likes = 0
  shared = 5
  for i in range(n):          
    likes += int(shared/2)    
    shared = (int(shared/2)*3)
  return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Exercise 95 - Challenges - Recursive Digit Sum
#I tried to reduce the k if it was a product of 10 (multiply by 10 or by 1 it's the same for the purpose of this challenge)        
import math
import os
import random
import re
import sys

def superDigit(n, k):
  while k % 10 == 0:
      k = k / 10
  P = sum(list(map(int, list(str(n)*int(k))))) #Then I calculated the value P following the rules of the challenge
  while P > 9:  #While P > 9 i used the recursive function with n = P and k = 1
    P = superDigit(P, 1)
  return P 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
          
# Exercise 96 - Challenges - Insertion Sort - Part 1

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
  if arr[-1] < arr[-2]:  #In the beginning I picked the rightmost value if it was not smaller than the previous value
    s = arr[-1]
    arr.pop(-1)
    arr.insert((n-1), arr[-1])
    print(" ".join(list(map(str, arr))))
  for i in range(1, n-1): #Than I iterated backwards in order to find the right position of the previous rightmost value
    if s < arr[n-i-2]:    #Every time that I didn't find out it, I moved the left value to the right 
      arr.pop(n-i-1)      #and eliminated the previous right value
      arr.insert((n-i-1), arr[n-i-2])
      print(" ".join(list(map(str, arr))))
    else:
      arr.pop(n-i-1)    #I did a similar thing when I found it, adding the rightmost value and removing the next right value
      arr.insert((n-i-1), s)
      return print(" ".join(list(map(str, arr))))
  arr.pop(0)             #If I didn't find the right position of the rightmost value in the iteration
  arr.insert(0, s)       #I just added it to the leftmost position 
  print (" ".join(list(map(str, arr))))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
          
    insertionSort1(n, arr)
          
# Exercise 97 - Challenges - Insertion Sort - Part 2

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
   for i in range(1,n):       #Every time I checked if a certain value was smaller than the previous one
        if arr[i]<arr[i-1]:
            a=arr[i]          #If it was, i picked it and I moved it to its right position
            arr.pop(i)
            for j in range(0,n):
                if a<arr[j]:
                    arr.insert(j,a)
                    break
        print(' '.join(list(map(str, arr))))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
