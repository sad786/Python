def check(st):
    i,j = 0,len(st)-1
    while i<j:
        if st[i]!=st[j]:
            return False
        i+=1
        j-=1
    return True
def form_palin(st):
    char_list = list(st)
    char_list.sort()
    front,back,mid = '','',''
    i=0
    while i<len(char_list):
        front +=char_list[i]
        i+=1
        if i<len(char_list):
            back = char_list[i]+back
            i +=1
        if i<len(char_list):
            mid +=char_list[i]
            i +=1
    
    res1 = front+mid+back
    
    front,back,mid = '','',''
    
    i = len(char_list)-1
    while i>=0:
        front +=char_list[i]
        i-=1
        if i>=0:
            back = char_list[i]+back
            i -=1
        if i>=0:
            mid +=char_list[i]
            i-=1
    
    res2 = front+mid+back
    front,mid,back = '','',''
    i,m=0,len(char_list)-1
    while i<len(char_list) and m>=0:
        front+=char_list[i]
        i +=1
        if i<len(char_list) and i<m:
            back = char_list[i]+back
            i +=1
        if m>=0 and m>i:
            mid +=char_list[m]
            m-=1
        
    res3 = front+mid+back
    return res1,res2,res3
    
def process(ques,st):
    yes = 0
    for q in ques:
        l,r = q[0]-1,q[1]
        if check(st[l:r]):
            yes+=1
        else:
            res1,res2,res3 = form_palin(st[l:r])
            if check(res1) or check(res2) or check(res3):
                yes +=1
    return yes
    
T = int(input())

for t in range(T):
    N,Q = [int(x) for x in input().split()]
    st = input().strip()
    ques = []
    for _ in range(Q):
        ques.append([int(x) for x in input().split()])
    
    res = process(ques,st)
    print('Case #{}: {}'.format(t+1,res))