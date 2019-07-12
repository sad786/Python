import math
alpha = ('A','B','C','D','E','F','G','H',
			'I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V',
            'W','X','Y','Z')
def gcd(a,b):
	if a>b:
		a,b = b,a
	if a<=0:
		return b
	return gcd(b%a,a)

def next_prime(n):
	n = n+1
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return next_prime(n)
	return n

def process(N,msg_list):
	primes = {3:0,2:0}
	prime = 3
	index = 1
	while True:
		index %=26
		prime = next_prime(prime)
		if prime>N:
			break
		primes[prime]=index
		index +=1
	
	result = []
	
	dividend = 0
	for i in range(len(msg_list)-1):
		dividend = gcd(msg_list[i],msg_list[i+1])
		al_index = msg_list[i]//dividend
		alp = primes[al_index]
		result.append(alpha[alp])
	
	result.append(alpha[primes[dividend]])
	last = msg_list[len(msg_list)-1]
	al_index = last//dividend
	result.append(alpha[primes[al_index]])
	return ''.join(result)
	

if __name__=='__main__':
	T = int(input())
	for t in range(T):
		N,L = [int(x) for x in input().split()]
		list = [int(x) for x in input().split()]
		res = process(N,list)
		print('Case #{}: {}'.format(t+1,res))