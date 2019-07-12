def found(st):
    for ch in st:
        if int(ch)%2!=0:
            return True
    
    return False
def process(N):
    plus_min = 0
    minus_min = 0
    
    if found(str(N)):
        temp = N+1
        plus_min +=1
        while found(str(temp)):
            plus_min +=1
            temp +=1
        
        temp = N-1
        minus_min +=1
        while found(str(temp)):
            temp -=1
            minus_min +=1
    
    return minus_min if minus_min<=plus_min else plus_min
T = int(input())

for t in range(T):
    N = int(input())
    res  = process(N)
    print('Case #{}: {}'.format(t+1,res))