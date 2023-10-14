

# Say "Hello, World!" With Python


if __name__ == '__main__':
    print("Hello, World!")


# Python If-Else


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if 1 <= n <= 100:
        if n % 2 == 1:
            print("Weird")
        elif n % 2 == 0 and 2 <= n <= 5:
            print("Not Weird")
        elif n % 2 == 0 and 6 <= n <= 20:
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")


# Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    c = a + b
    d = a - b
    e = a * b
    
    print(c)
    print(d)
    print(e)


# Python: Division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    c = a//b
    d = a/b
    
    print(c)
    print(d)


# Loops


if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i ** 2)


# Write a function


def is_leap(year):
    leap = False
    
    if 1990 <= year <= 10**5:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))


# Print Function


if __name__ == '__main__':
    n = int(input())
    
    if 1 <= n <= 150:
        for i in range(1,n+1):
            print(i, end="")


# List Comprehensions


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    out = [];
    outTemp = [];
    
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    outTemp = [X,Y,Z];
                    out.append(outTemp);
                    
print(out);


# Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    
    print(arr[-2])


# Nested Lists


if __name__ == '__main__':
    
    out = []
    temp = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        scores.append(score)
        out.append(temp)
        temp = []
    
    scores = sorted(list(set(scores)))
    
    people = []
    
    for x in out:
        if x[1] == scores[1]:
            people.append(x[0])
    
    people.sort()
    
    for p in people:
        print(p)


# Finding the percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    
    for student_mark_key in student_marks.keys():
        if student_mark_key == query_name:
            voti = student_marks[student_mark_key]
    
    average = sum(voti)/len(voti)
    print("%.2f" % average)


# Lists


if __name__ == '__main__':
    N = int(input())
    
    lista = []
    
    for i in range (N):
        action=input().split();
        if action[0] == "insert":
            lista.insert(int(action[1]),int(action[2]))
        elif action[0] == "append":
            lista.append(int(action[1]))
        elif action[0] == "pop":
            lista.pop();
        elif action[0] == "print":
            print(lista)
        elif action[0] == "remove":
            lista.remove(int(action[1]))
        elif action[0] == "sort":
            lista.sort();
        elif action[0] == "reverse":
            lista.reverse();


# Tuples


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    hash_number = hash(tuple(integer_list))
    print(hash_number)


# sWAP cASE


def swap_case(s):
    
    strin = ""
    
    for letter in s:
        if letter.isupper() == True:
            strin += letter.lower()
        else:
            strin += letter.upper()
    
    return strin

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join


def split_and_join(line):
    
    line = line.split(" ")
    line = "-".join(line)
    
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?


def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations


def mutate_string(string, position, character):
    
    mutate = list(string);
    mutate[position] = character
    string = ''.join(mutate)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string


def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            found=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    found=0
                    break
            if found==1:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# String Validators


if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# Text Alignment


thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# solution found on the web


# Text Wrap


import textwrap

def wrap(string, max_width):
    
    string = textwrap.wrap(string,max_width)
    
    string = "\n".join(string)
    
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Designer Door Mat


n, m = map(int,input().split())

pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]

print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# solution found in the discussions


# String Formatting


def print_formatted(number):
    
    max_width = len(str(bin(number))[2:])
    
    for i in range(1,n+1):
        octt = str(oct(i))[2:]
        hexx = str(hex(i))[2:].upper()
        binn = str(bin(i))[2:]
        
        print(str(i).rjust(max_width),octt.rjust(max_width),hexx.rjust(max_width),binn.rjust(max_width))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# collections.Counter()


if __name__ == "__main__":
    
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    
    income = 0
    
    for i in range(m):
        size, price = map(int, input().split())
        
        for v in arr:
            if v == size:
                income += price
                arr.remove(v)
                break
            
    print(income)


# Introduction to Sets


def average(array):
    sett = set(array)
    
    averagee = sum(sett)/len(sett)
    
    return averagee

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# DefaultDict Tutorial


from collections import defaultdict

defdic = defaultdict(list)

n, m = list(map(int, input().split()))

l = []

for i  in range(1,n+1):
    defdic[input()].append(i)
    
for a in range(m):
    l.append(input())
    
for b in l:
    if b in defdic.keys():
        print(*defdic[b])
    else:
        print(-1)


# Calendar Module


import calendar

if __name__ == '__main__':
    
    month , day , year = map(int, input().strip().split(' '))
    
    weekday = calendar.weekday(year,month,day)
    
    print(calendar.day_name[weekday].upper())


# Exceptions


if __name__ == '__main__':
    
    n = int(input())
    
    for i in range(n):
        try:
            a, b = map(int,input().strip().split(' '))

            print(a//b)
            
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)


# Collections.namedtuple()


from collections import namedtuple

n = int(input().strip())
values=" ".join(input().split())
students = namedtuple('student',values)

totalmarks = 0

for i in range(n):
    lista=input().split()
    student = students(lista[0], lista[1], lista[2], lista[3])
    totalmarks += int(student.MARKS)
    
print('{:.2f}'.format(totalmarks / n))


# Time Delta


import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    timeformat = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, timeformat)
    t2 = datetime.strptime(t2, timeformat)
    return str(int(abs((t1-t2).total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# No Idea!


if __name__ == "__main__":
    
    happiness = 0
    n,m = map(int, input().strip().split(' '))
    list2 = list(map(int, input().strip().split(' ')))
    list3 = list(map(int, input().strip().split(' ')))
    list4 = list(map(int, input().strip().split(' ')))
    
    for n in list2:
        if n in list3:
            happiness+=1
        elif n in list4:
            happiness-=1
    
    print(happiness)


# Collections.OrderedDict()


from collections import OrderedDict

n = int(input().strip())
ordereddic = OrderedDict()

for i in range(n):
    item, space, price = input().rpartition(' ') # found on the web
    ordereddic[item] = ordereddic.get(item, 0) + int(price)
    
for item, price in ordereddic.items():
    print(item, price)


# Symmetric Difference


if __name__ == '__main__':
    M = int(input().strip())
    a = set(map(int,input().strip().split(' ')))
    
    N = int(input().strip())
    b = set(map(int,input().strip().split(' ')))
    
    c = b.difference(a)
    d = a.difference(b)
    
    e = c.union(d)
    
    for value in sorted(e):
        print(value)


# Set .add()


if __name__ == '__main__':
    
    n = int(input().strip())
    sett= set()
    
    for i in range(n):
        country = input().strip()
        sett.add(country)
        
    print(len(sett))


# Word Order


from collections import Counter

if __name__ == '__main__':
    
    n = int(input().strip())
    
    words = []
    
    for i in range (n):
        
        word = str(input().strip())
        words.append(word)
    
    print(len(set(words)))
    
    count = Counter(words)
    
    print(*count.values())


# Set .discard(), .remove() & .pop()


if __name__ == '__main__':
    
    n = int(input().strip())
    
    lista = list(map(int, input().strip().split(' ')))
    
    m = int(input().strip())
    
    lista2 = lista[::-1]
    sett = set(lista2)
    

    for i in range(m):
        action = input().split()
        if action[0] == 'pop':
            sett.pop()
        elif action[0] == 'remove':
            sett.remove(int(action[1]))
        elif action[0] == 'discard':
            sett.discard(int(action[1]))
            
    print(sum(sett))


# Collections.deque()


from collections import deque

if __name__ == '__main__':
    d = deque()
    n = int(input().strip())
    action = []
    
    for i in range(n):
        
        action = input().split()
        if action[0] == 'append':
            d.append(int(action[1]))
        elif action[0] == 'appendleft':
            d.appendleft(int(action[1]))
        elif action[0] == 'pop':
            d.pop()
        elif action[0] == 'popleft':
            d.popleft()
            
    print(*d)


# Company Logo


from collections import Counter


if __name__ == '__main__':
    s = input()
    lista = list(sorted(s))
    
    count = Counter(lista)
    
    mostcommon = count.most_common(3)
    
    for a, b in mostcommon:
        print(a , b)


# Set .union() Operation


if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))
    m = int(input())
    french_students = set(map(int, input().split()))
    
    unionset = english_students.union(french_students)
    
    print(len(unionset))


# Piling Up!


import math
from collections import deque

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        m = int(input())
        blocks = deque(list(map(int, input().split())))
        answer=[]
        
        answer.append(math.inf)
        flag=1
        
        while flag!=0 and len(blocks)>0:
            blockmax = max(blocks[0], blocks[-1])
            if blockmax > answer[-1]:
                flag=0
            else:
                answer.append(blockmax)
                if blockmax==blocks[0]:
                    blocks.popleft()
                else:
                    blocks.pop()
        if len(blocks)==0:
            print("Yes")
        else:
            print("No")

# solution inspired by the discussions


# Set .intersection() Operation


if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))
    m = int(input())
    french_students = set(map(int, input().split()))
    
    intersectionset = english_students.intersection(french_students)
    
    print(len(intersectionset))


# Set .difference() Operation


if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))
    m = int(input())
    french_students = set(map(int, input().split()))
    
    differenceset = english_students.difference(french_students)
    
    print(len(differenceset))


# Set .symmetric_difference() Operation


if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))
    m = int(input())
    french_students = set(map(int, input().split()))
    
    symmetricdifferenceset = english_students.symmetric_difference(french_students)
    
    print(len(symmetricdifferenceset))


# Set Mutations


if __name__ == '__main__':

    n = int(input())
    sett = set(map(int, input().split()))
    m = int(input())
    
    for i in range(m):
        action = input().split()
        
        newset = set(map(int, input().split()))
        
        if action[0] == 'intersection_update':
            sett.intersection_update(newset)
        elif action[0] == 'update':
            sett.update(newset)
        elif action[0] == 'symmetric_difference_update':
            sett.symmetric_difference_update(newset)
        elif action[0] == 'difference_update':
            sett.difference_update(newset)
    
    print(sum(sett))


# The Captain's Room


if __name__ == '__main__':
    n = input()
    rooms_list = list(input().split())


    for v in list(rooms):
        rooms_list.remove(v)
        
    captainroom = rooms.difference(set(rooms_list)).pop()
        
    print(captainroom)


# Check Subset


if __name__ == '__main__':
    
    n = int(input().strip())
    
    for i in range(n):
        a = int(input())
        set1 = set(map(int, input().split()))
        b = int(input())
        set2 = set(map(int, input().split()))
        
        if len(set1.difference(set2)) == 0:
            print("True")
        else:
            print("False")


# Check Strict Superset


if __name__ == '__main__':
    sett = set(map(int, input().split()))
    n = int(input())

    isallstrict = 0

    for i in range(n):
        exsubset = set(map(int, input().split()))
        newset = exsubset.difference(sett)
        isallstrict += len(newset)

    if isallstrict == 0:
        print("True")
    else:
        print("False")


# Zipped!


if __name__ == '__main__':
    
    n,m = map(int,input().strip().split(' '))
    
    all_marks = []
    
    for i in range(m):
        lista = list(map(float, input().strip().split(' ')))
        all_marks.append(lista)
    
    
    for value in list(zip(*all_marks)):
        print( sum(value)/len(value) )


# Athlete Sort


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    first_multiple_input = input().strip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    rows = [input() for _ in range(n)]
    k = int(input().strip())
    
    for row in sorted(rows, key=lambda row: int(row.split()[k])):
        print(row)
        
    # couldn't solve alone, solution found on the web


# ginortS


string = input()
sorted_string = ''.join(sorted(string, key=lambda char: (char.isdigit(), char.isdigit() and int(char) % 2 == 0, char.swapcase())))
print(sorted_string)

# inspired by the discussions


# Detect Floating Point Number


from re import match, compile

n = int(input().strip())

pattern = compile('^[-+]?[0-9]*\.[0-9]+$')

for i in range(n):
    print(bool(pattern.match(input().strip())))


# Map and Lambda Function


cube = lambda x: x**3

def fibonacci(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            nextt = fib[i - 1] + fib[i - 2]
            fib.append(nextt)
        return fib
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Re.split()


regex_pattern = r"[,.]*"

import re
print("\n".join(re.split(regex_pattern, input())))


# Group(), Groups() & Groupdict()


import re


pattern = re.compile(r"([A-Za-z0-9])\1")
n = re.search(pattern,input())

if n is not None:
    print(n.group()[0])
else:
    print(-1)


# Re.findall() & Re.finditer()


import re

i = input()

n = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAIEOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',i)

if len(n) > 0:
    for a in n:
        print(a)
else:
    print(-1)


# Re.start() & Re.end()


import re

str1 = str(input().strip())
str2 = str(input().strip())

print(str1,str2)

m = re.search(r'','')


# Regex Substitution


import re

n = int(input().strip())
substitutes = {'&&': 'and', '||': 'or'}

for i in range(n):
    strtemp = input()
    strnew = re.sub(r'(?<= )(?P<operator>&{2}|\|{2})(?= )', lambda x: substitutes.get(x.group('operator')), strtemp)
    print(strnew)

# couldn't solve alone, solution inspired by the discussions


# Validating Roman Numerals


regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$' # solution inspired by the discussions


# Validating phone numbers


import re

n = int(input().strip())

for i in range(n):
    if re.match(r'[789]\d{9}$', input()):
        print("YES")
    else:
        print("NO")


# Validating and Parsing Email Addresses


import email.utils
import re

email.utils.formataddr(('name', '<user@hackerrank.com>'))
pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'

n = int(input().strip())
    
for i in range(n):
    emailadd = email.utils.parseaddr(input().strip())
    ao = re.match(r'[a-zA-Z]([\w\.\-])+@([a-zA-Z])+\.([a-zA-Z]){1,3}$',emailadd[1])
    if ao:
        print(email.utils.formataddr(emailadd))


# Hex Color Code


import re

n = int(input().strip())

pattern = r'(#[a-fA-F\d]{3,6})\S'

for i in range(n):
    ao = re.findall(pattern, input())
    for data in ao:
        print(data, sep="\n")


# HTML Parser - Part 1


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for i in attrs:
            print ('->', i[0], '>', i[1])
    def handle_endtag(self, tag):
        print ('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for j in attrs:
            print ('->', j[0], '>', j[1])
            
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())


# HTML Parser - Part 2


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(comment)
    def handle_data(self, data):
        if data == '\n': 
            return
        print('>>> Data')
        print(data)    
        
        
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)


# Detect HTML Tags, Attributes and Attribute Values


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for i in attr:
            print(f'-> {i[0]} > {i[1]}')
   
html=""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
                
parser = MyHTMLParser()
parser.feed(html)

# couldn't solve alone, solution inspired by the discussions


# XML 1 - Find the Score


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    
    return sum(len(el.attrib) for el in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# Validating UID


import re

n = int(input().strip())

for i in range(n):
    uid = input()
    if re.search("[a-zA-Z0-9]", uid) and re.search("[\d]{3,}[A-Z]{2,}", ''.join(sorted([*uid]))) and len(set(uid)) == 10: #quest'ultimo per verificare se ci sono valori ripetuti
        print('Valid')
    else:
        print('Invalid')


# Validating Credit Card Numbers


import re

n = int(input().strip())

pattern = r"^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$"

for i in range(n):
        card_number = input("")
        if re.match(pattern, card_number):
            print("Valid") 
        else:
            print("Invalid")

# solution inspired by the discussions


# XML2 - Find the Maximum Depth


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    
    if level > maxdepth:
        maxdepth =level
    for x in elem:
        depth(x, level)
    
# exploration of the tree

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# Standardize Mobile Number Using Decorators


def wrapper(f):
    def fun(l):
        return f([('+91 '+ number[-10:-5] + ' ' + number[-5:]) for number in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


# Validating Postal Codes


regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# Decorators 2 - Name Directory


import operator

def person_lister(func):
    def inner(people):
        return [func(p) for p in sorted(people, key = lambda x: (int(x[2])))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# Matrix Script


import math
import os
import random
import re
import sys

n,m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(input()))
    
matrix = list(zip(*matrix))

result = ''.join([c for s in matrix for c in s])
print(re.sub(r'(?<=[^\W_])([\W]+?)(?=[^\W_])',' ', result))

# couldn't solve alone, solution taken by the discussions


# Arrays


import numpy

def arrays(arr):
    arr2 = arr[::-1]
    arr2 = numpy.array(arr2, float)
    return arr2

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# Shape and Reshape


import numpy

ao = list(map(int,input().strip().split(' ')))

ae = numpy.reshape(ao, (3,3))

print(ae)


# Transpose and Flatten


import numpy

n,m = map(int,input().split())
arr = []

for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
    
ao = numpy.array(arr)
ae = numpy.transpose(ao)
ai = ao.flatten()

print(ae)
print(ai)


# Concatenate


import numpy

n, m, o = map(int,input().strip().split(' '))

arr1 = []
arr2 = []

for i in range(n):
    row = list(map(int,input().split()))
    arr1.append(row)
    
for i in range(m):
    row = list(map(int,input().split()))
    arr2.append(row)
    
ao = numpy.concatenate((arr1,arr2), axis=0)

print(ao)


# Zeros and Ones


import numpy

arr = list(map(int,input().strip().split(' ')))

ao = numpy.zeros(arr, dtype=numpy.int)
    
ae = numpy.ones(arr, dtype=numpy.int)

print(ao,ae, sep= '\n')


# Eye and Identity

import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().strip().split(' '))

ao = numpy.eye(n,m)


# Array Mathematics


import numpy

n, m = map(int, input().strip().split(' '))

a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

a = numpy.array(a)
b = numpy.array(b)


print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))

print(ao)


# Floor, Ceil and Rint


import numpy
numpy.set_printoptions(legacy='1.13')

arr = list(map(float, input().strip().split(' ')))

numpy.array(arr,float)

ao = numpy.floor(arr)
ae = numpy.ceil(arr)
ai = numpy.rint(arr)

print(ao,ae,ai, sep='\n')


# Sum and Prod


import numpy

n, m = map(int, input().strip().split(' '))

arr = []

for i in range (n):
    arr_temp = list(map(int, input().strip().split(' ')))
    arr.append(arr_temp)
    
arr = numpy.array(arr)

ao = numpy.sum(arr, axis = 0)
ae = numpy.prod(ao)

print(ae)


# Min and Max


import numpy

n, m = map(int, input().strip().split(' '))

arr = []

for i in range (n):
    arr_temp = list(map(int, input().strip().split(' ')))
    arr.append(arr_temp)
    
arr = numpy.array(arr)

ao = numpy.min(arr, axis = 1)
ae = numpy.max(ao)

print(ae)


# Dot and Cross


import numpy

n= int(input().strip())

arr1 = []
arr2 = []

for i in range (n):
    arr_temp = list(map(int, input().strip().split(' ')))
    arr1.append(arr_temp)
    
for i in range (n):
    arr_temp = list(map(int, input().strip().split(' ')))
    arr2.append(arr_temp)
    
arr1 = numpy.array(arr1)
arr2 = numpy.array(arr2)

result = numpy.dot(arr1,arr2)

print(result)


# Inner and Outer


import numpy

arr1 = list(map(int, input().strip().split(' ')))
    
arr2 = list(map(int, input().strip().split(' ')))

arr1 = numpy.array(arr1)
arr2 = numpy.array(arr2)

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))


# Polynomials


import numpy

p = list(map(float,input().strip().split(' ')))

o = float(input().strip())

print(numpy.polyval(p,o))


# Linear Algebra


import numpy

n = int(input().strip())

arr = []

for i in range (n):
    arr_temp = list(map(float, input().strip().split(' ')))
    arr.append(arr_temp)
    
arr = numpy.array(arr)

print(round(numpy.linalg.det(arr), 2))


# Mean, Var, and Std


import numpy

n, m = map(int, input().strip().split(' '))

arr = []

for i in range (n):
    arr_temp = list(map(int, input().strip().split(' ')))
    arr.append(arr_temp)
    
arr = numpy.array(arr)

ao = numpy.mean(arr, axis = 1)
ae = numpy.var(arr, axis = 0)
ai = round(numpy.std(arr), 11)

print(ao,ae,ai, sep='\n')
