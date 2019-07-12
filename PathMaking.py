def process(R,C):
    if abs(R-C)<=1 or R==C:
        return 'IMPOSSIBLE',None
    
    ir = R//2
    ic = C//2
    lc,lr,rr,rc = 0,0,ir,ic
    path = []
    last = R-1
    init = 1
    sm = 0
    while sm<(R*C):
        path.append((rr+1,rc+1))
        path.append((lr+1,lc+1))
        rc +=1
        if lc==ic:
            rr = last
            rc =0
            last -=1
        if rc==ic:
            lr = init
            init +=1
            lc = -1
        lc +=1
        sm +=2
    
    if R%2!=0:
        path.pop()
    return 'POSSIBLE',path
    
    
T = int(input())
for t in range(T):
    R,C = [int(x) for x in input().split()]
    res,path = process(R,C)
    print('Case #{}: {}'.format(t+1,res))
    if path is not None:
        for p in path:
            print(p[0],p[1])