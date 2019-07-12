import sys
def process(n):
	first = 1
	print(first,end=' ')
	for i in range(2,n+1):
		first = i+first
		print(first,end=' ')
if __name__=='__main__':
	n = int(input("Enter the term: "))
	if n<=0:
		print('Please Provide valid input')
		sys.exit()
	process(n)