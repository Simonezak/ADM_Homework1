

# Birthday Cake Candles


import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    
    count = 0
    max_value = max(candles)
    
    for value in candles:
        if value == max_value:
            count+=1
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# Number Line Jumps


import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    
    dist1 = x1
    dist2 = x2
    
    if v1 > v2:
        while dist1 < dist2:
            dist1+=v1
            dist2+=v2
            if dist1 == dist2:
                print("YES")
        
        if dist1 > dist2:
            print("NO")
    else:
        while dist1 > dist2:
            dist1+=v1
            dist2+=v2
            if dist1 == dist2:
                print("YES")
        
        if dist1 < dist2:
            print("NO")

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    kangaroo(x1, v1, x2, v2)


# Viral Advertising


import math
import os
import random
import re
import sys

def viralAdvertising(n):

    shared = 5
    liked = 2
    cumulative = 2
    
    for i in range(1,n):
        shared = liked*3
        liked = math.floor(shared/2)
        cumulative += liked
    
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# Recursive Digit Sum


import math
import os
import random
import re
import sys

def superDigit(n, k): 
    
    n = int(n)
    if n == 0:
        return 0
    if n*k%9 == 0:
        return 9
    else:
        return n*k%9
# solution found in the discussions

# i made this solution, but it seems it doesn't work for long inputs
'''    
    repeated_string = n * k
    
    while len(repeated_string)>1:
        repeated_string = digit(repeated_string)
    
    return repeated_string

def digit(n):
    repeated_int = sum(map(int, n.strip()))
        
    return str(repeated_int)
'''

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)


# Insertion Sort - Part 1


import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    
    n = n-1
    numbersort = arr[n]
    
    while arr[n-1] > numbersort :
        arr[n] = arr[n-1] 
        n-=1
        print(*arr)
        if n==0:
            break
    
    arr[n] = numbersort
    
    print(*arr)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Insertion Sort - Part 2


import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    
    for l in range(1,n):
        numbersort = arr[l]
        i = l-1
        
        while arr[i] > numbersort:
            if i == -1:
                break
            arr[i+1] = arr[i]
            i-=1
        
        arr[i+1] = numbersort
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
