def process(A):
	t,r,l,b = 0,len(A[0])-1,0,len(A)-1
	dir = 0
	while t<=b and l<=r:
		if dir==0 and l<=r:
			for i in range(t,r+1):
				print(A[t][i])
			dir =1
			t +=1
		if dir==1 and t<=b:
			for i in range(t,b+1):
				print(A[i][r])
			dir = 2
			r -=1
		if dir==2 and l<=r:
			i = r
			while i>=l:
				print(A[b][i])
				i -=1
			b -=1
			dir = 3
		if dir==3 and t<=b:
			i = b
			while i>=t:
				print(A[i][l])
				i -=1
			l +=1
			dir =0

r = int(input("Enter No. of Rows"))
c = int(input("Enter No. of Columns"))

num_list = []
while r>0:
	num_list.append(list(map(lambda x:int(x), input().split())))
	r -=1
process(num_list)