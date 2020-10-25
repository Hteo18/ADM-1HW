#Say "Hello, World!" With Python

print("Hello, World!")

#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2 !=0 or (n%2 ==0 and n in range(6,21)) :
    print("Weird")
elif n%2 ==0 and (n in range(2,5) or n > 20):
    print("Not Weird")


#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)
    
#Write a function

def is_leap(year):
    leap = False
    if (year%4 ==0 and year%100 !=0) or year%400 ==0:
        leap= True
    return leap

#Print Function

if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1), sep="")
    
#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ( [[a,b,c] for a in range (0,x+1) for b in range (0,y+1) for c in range (0,z+1)    if a+b+c != n ])
    
#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
a = set (arr)
a.remove(max(a)) 

print (max(a))

  

#Nested Lists

if __name__ == '__main__':
    l=[]
    miao=[]
    voti= set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        voti.add(score)

voti.remove(min(voti))
for persona in l:
    if persona[1]== min(voti):
         miao.append(persona[0])
print('\n'.join(sorted(miao)))

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print('%.2f' %(sum(student_marks[query_name])/3))

#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

#Lists

if __name__ == '__main__':
    N = int(input())
    l= []
    for i in range(N):
        a = input().split()
        if a[0]=="insert":
            l.insert(int(a[1]),int(a[2]))
        elif a[0]=="print":
            print(l)
        elif a[0]=="remove":
            l.remove(int(a[1]))
        elif a[0]== "append":
            l.append(int(a[1]))
        elif a[0]== "sort":
            l.sort()
        elif a[0]== "pop":
            l.pop()
        elif a[0]== "reverse":
            l.reverse()
            
     
#Map and Lambda Function

cube = lambda x: x**3
def fibonacci(n):
    if n == 0:
       return []
    elif n==1:
        return [0]
    elif n==2:
        return[0,1]
    elif n > 2 :
        l= [0,1,1]
        for i in range(n-3):
            l.append(l[i+2]+l[i+1])
        return l



#sWAP cASE

def swap_case(s):
    S=s.swapcase()
    return S

#String Split and Join

def split_and_join(line):
    # write your code here
  l=  line.split(" ")
  U= "-".join(l)
  return U
  



#What's Your Name?

def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")

#Mutations

def mutate_string(string, position, character):
    return string[:position]+ character+string[position+1:]

#Find a string

def count_substring(string, sub_string):
    count= 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count

#String Validators

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print("\n".join(map(str,[alnum, alpha, digit, lower, upper])))


        
#Text Alignment

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
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap



def wrap(string, max_width):
    s=str()
    o=len(string)//max_width
    for i in range(o):
        s=s+string[max_width*i:max_width*(i+1)]+'\n'
    s=s+str(string[o*max_width:])
    return s

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m= map(int, input().split())

for i in range(1,n,2):
    print((i*".|.").center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n,1,-2):
    print(((i-2)*".|.").center(m,"-"))

#Standardize Mobile Number Using Decorators

def wrapper(f):
   
    def fun(l):
        # complete the function
        
            f(["+91 "+i[-10:-5]+" "+i[-5:] for i in l])
        
    return fun
# I found help in the discussion


#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    c=Counter(candles)[max(candles)]
   
    return c 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Introduction to Sets

def average(array):
    s = set(arr)
    
    return sum(s)/len(s)

#No Idea!

n,m=map(int, input().split())
arr = input().split()

A= set(input().split())
B = set(input().split())
c = 0
for i in range(n):
    if arr[i] in A:
        c = c+1
    if arr[i] in B:
        c = c-1
print(c)


#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(input())
s= set()

for i in range(N):
    p = input()
    s.add(p)
print(len(s))


#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
     l= input().split()
     if l[0]=='pop':
        s.pop()
     elif l[0]=='discard':
        s.discard(int(l[1]))
     elif l[0]=='remove':
        s.remove(int(l[1]))
print(sum(s))


#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
M= int(input())
m= set(input().split())
N= int(input())
n= set(input().split())

a = m.symmetric_difference(n)

print(*sorted(map(int,a)), sep='\n')


#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
n = set(input().split())
B = int(input())
b = set(input().split())

s = n.union(b)
print(len(s))


#Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
n = set(input().split())
B = int(input())
b = set(input().split())

s = n.intersection(b)
print(len(s))


#Set .difference() Operation

N= int(input())
n = set(input().split())
B= int(input())
b= set(input().split())

s = n.difference(b)
print(len(s))


#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(input())
n= set(input().split())
B= int(input())
b= set(input().split())

s = n^b
print(len(s))


#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUTù
A= int(input())
a= set(input().split())
N = int(input())
for i in range(N):
    l=list( input().split())
    c = set(input().split())
    if l[0]== "intersection_update":
        a.intersection_update(c)
    elif l[0]== "update":
        a.update(c)
    elif l[0]== "symmetric_difference_update":
        a.symmetric_difference_update(c)
    elif l[0]=="difference_update":
        a.difference_update(c)
a = set(map(int,a))
print(sum(a))


#The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
K = int(input())
r = input()
c = Counter(r.split())
s = set(r.split())
for i in s:
    if c[i]==1:
     print(int(i))

#Check Subset

T = int(input())

for i in range(T):
    A = int(input())
    a= set(input().split())
    B = int(input())
    b = set(input().split())
    if a.intersection(b)== a:
        print("True")
    else:
        print("False")

#Check Strict Superset

A = set(input().split())
n = int(input())
c=0
for i in range(n):
    N = set(input().split())
    if len(A)>len(N) and A.intersection(N)== N:
        c+=1
if c==n:
    print("True")
else:
    print("False")

#Arrays



def arrays(arr):
    a= numpy.array(arr[::-1],float)
    return a

#Shape and Reshape

import numpy
l=input().split()
l = list(map(int,l))
a= numpy.array(l)
a.shape=(3,3)
print(a)


#Transpose and Flatten

import numpy
N,M = map(int,input().split())

arr= numpy.array([input().split() for i in range(N)],int)
print(numpy.transpose(arr))
print(arr.flatten())




#Concatenate

import numpy
N,M,P= map(int,input().split())
A = numpy.array([input().split() for i in range(N)],int)
B = numpy.array([input().split() for i in range(M)],int)

print(numpy.concatenate((A,B),axis= 0))

#Zeros and Ones

import numpy
N=list(map(int,input().split()))
print(numpy.zeros((N),int))
print(numpy.ones((N),int))


#Eye and Identity

import numpy
N,M=map(int,input().split())
numpy.set_printoptions(sign=' ')
print(numpy.eye(N,M,dtype=numpy.float))


#Array Mathematics

import numpy
N,M=map(int,input().split())
a= numpy.array([input().split() for i in range(N)],int)
b = numpy.array([input().split() for i in range(N)],int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))

#Floor, Ceil and Rint

import numpy
A= numpy.array(input().split(),float)
numpy.set_printoptions(sign=' ')
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep = "\n")

#Sum and Prod

import numpy
N,M=map(int,input().split())
A = numpy.array([input().split() for i in range(N)], int)

a = numpy.sum(A, axis= 0)
print( numpy.prod(a))


#Min and Max

import numpy
N,M=map(int,input().split())
A = numpy.array([input().split() for i in range(N)], int)

a = numpy.min(A, axis= 1)
print(numpy.max(a))

#Mean, Var, and Std

import numpy
N,M=map(int,input().split())
A = numpy.array([input().split() for i in range(N)],int)
numpy.set_printoptions(legacy='1.13')

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis= 0))
print(numpy.std(A, axis=None))

#Dot and Cross

import numpy
N=int(input())
A = numpy.array([input().split() for i in range(N)], int)
B = numpy.array([input().split() for i in range(N)], int)

print( numpy.dot(A,B))

#Inner and Outer

import numpy
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))

#Polynomials

import numpy
P = numpy.array(input().split(),float)
x = float(input())
print(numpy.polyval(P,x))

#Linear Algebra

import numpy
N = int(input())
A = numpy.array([input().split() for i in range(N)], float)
print(round(numpy.linalg.det(A),2))


#Calendar Module

import calendar
MM, DD, YYYY= map(int,input().split())
G = calendar.weekday(YYYY,MM,DD)
if G==0:
    print("MONDAY")
elif G==1:
    print("TUESDAY")
elif G==2:
    print("WEDNESDAY")
elif G==3:
    print("THURSDAY")
elif G==4:
    print("FRIDAY")
elif G==5:
    print("SATURDAY")
elif G==6:
    print("SUNDAY")


#Exceptions

N=int(input())
for i in range(N):
    try:
        A,B=map(int,input().split())
        print(A//B)
    except Exception as e:
        print("Error Code:",e)
#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1!=v2 and (x1-x2)%(v2-v1)==0 and (x1-x2)/(v2-v1)>0:
        return "YES"
    else:
        return "NO"
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

#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    c=k*sum(map(int,n))
    if c%9==0:
        return 9
    else:
        return c%9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cond=5
    like=2
    cumulato=2
    for _ in range(n-1):
        cond=3*(cond//2)
        like=cond//2
        cumulato=cumulato+like
    return cumulato

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    F=arr[-1]
    while F< arr[n-2] and n-2>=0:
        arr[n-1]= arr[n-2]
        print(*arr)
        n=n-1
    arr[n-1]=F
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        I=arr[i]
        pos = i-1
        while pos>=0 and I<arr[pos]:
            arr[pos+1]= arr[pos]
            pos=pos-1
        arr[pos+1]=I
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


