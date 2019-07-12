def process(ch):
    rs = ''
    for c in ch:
        if c=='E':
            rs = rs+'S'
        else:
            rs = rs+'E'
    
    return rs

T = int(input())

for t  in range(T):
    N = int(input())
    ch = input().strip()
    res = process(ch)
    print('Case #{}: {}'.format(t+1,res))
    