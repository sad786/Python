n = int(input())

cap_list = {}

while n>0:
	s = input().strip()
	k,v = int(s[0]),int(s[2])
	keys = cap_list.keys()
	if k in keys:
		cap_list[k].append(v)
	else:
		cap_list[k] = [v]
	n -=1
	
n = int(input())

pair_list = []
while n>0:
	pair_list.append(input().strip())
	n -=1

	
final_list = []
max = 0
	
for p in pair_list:
	p1 = int(p[0])
	p2 = int(p[2])
	i = 0
	for e in cap_list[p1]:
		edges =0
		if p2==e:
			final_list.insert(i,1)
		else:
			edges +=1
			if p2 in 
		