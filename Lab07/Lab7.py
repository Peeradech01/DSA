"""7.1"""

import random
from time import time

def summationpuls(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def summationmultiply(n):
    return (n/2)*(n+1)

def analyze_algo(n=1):
    stime = time()
    #summationpuls(n)
    # summationmultiply(n)
    #isIntersect_O2(randomList(n), randomList(n), randomList(n))
    isIntersect_O3(randomList(n), randomList(n), randomList(n))
    
    etime = time()
    elapsed = etime-stime
    print("execution time: ", elapsed)




"""7.2"""

from time import time

def  isIntersect_O2(a, b, c): #N2
    for i in a:
        for j in b:
            if i == j:
                return j in c
            
    return False


def  isIntersect_O3(a, b, c): #N3
    for i in a:
        for j in b:
            for k in c:
                if i == k == k:
                    return True
    return False

def randomList(n):
    array = list()

    while len(array) != n:
        data = int(random.random() * (n*10000000))
        array.append(data)

    return array


n = 1000
analyze_algo(n)
