import sys
from random import *
def process(N,B,F):
    num = []
    for _ in range(N):
        r = int(random()*2)
        num.append(str(r))
        
    num = ''.join(num)
    
    print(num)
    sys.stdout.flush()
    response = input().strip()
    res = []
    i,j=0,0
    while i<len(num) and j<len(response):
        if num[i]==response[j]:
            i+=1
            j+=1
        else:
            res.append(i)
            i +=1
    
    print(res[0],res[1])
    sys.stdout.flush()
    response = input().strip()
    
T = int(input())
for t in range(T):
    N,B,F = [int(x) for x in input().split()]
    process(N,B,F)