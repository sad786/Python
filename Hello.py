import sys
def process(A,B,N):
    res = (A+B)//2
    print(res)
    sys.stdout.flush()
    inp = input()
    if inp=='TOO_SMALL':
        A = res+1
    elif inp=='TOO_BIG':
        B = res-1
    else:
        return
    process(A,B,N-1)
    
T = int(input())
for _ in range(T):
    A,B = [int(x) for x in input().split()]
    N = int(input())
    process(A+1,B,N)