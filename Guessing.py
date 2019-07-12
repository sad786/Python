import sys
def process(A,B,N):
	l,b = A+1,B
	while N>0:
		mid = (l+b)//2
		print(mid)
		sys.stdout.flush()
		r = input()
		try:
			if r=='CORRECT':
				return
			elif r=='TOO_BIG':
				b = mid-1
			elif r=='TOO_SMALL':
				l = mid+1
			else:
				return r
		except ERROR:
			return
		N -=1
	
tc = int(input())
for _ in range(tc):
	l = list(map(lambda x:int(x),input().split()))
	N = int(input())
	r = process(l[0],l[1],N)