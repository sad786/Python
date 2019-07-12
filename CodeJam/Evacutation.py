alpha = ('A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V',
            'W','X','Y','Z')
T = int(input())
def process(party_list):
	result = []
	sm = sum(party_list)
	while sm>0:
		res = ''
		maj = getMajority(party_list,False)
		res +=alpha[maj]
		party_list[maj]-=1
		maj = getMajority(party_list,True)
		if maj>=0:
			party_list[maj]-=1
			res +=alpha[maj]
		sm -=len(res)
		result.append(res)
	return ' '.join(result)
	
def getMajority(party_list,check):
	maj_index = 0
	if check==True:
		    same = True
		for e in party_list:
			if e!=0 and e!=party_list[maj_index]:
				same = False
				break
		if same==True:
			return -1
    for i in range(1,len(party_list)):
        if party_list[i]>party_list[maj_index]:
            maj_index = i
    return maj_index
for t in range(T):
    N = int(input())
    party_list = [int(x) for x in input().split()]
    res = process(party_list)
    print('Case #{}: {}'.format(t+1,res))