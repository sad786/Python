def process(N):
    temp = str(N)
    temp = temp.replace('4','2')
    res1 = int(temp)
    res2 = N-res1
    return res1,res2


T = int(input())
for t in range(T):
    N = int(input())
    res1,res2 = process(N)
    print('Case #{}: {} {}'.format(t+1,res1,res2))