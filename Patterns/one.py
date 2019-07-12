n = int(input())

for i in range(n-1):
	print('*'+'  '*(n)+'*')
	
print(' *'*(n+1))
for i in range(n):
	print('  '*n+' *')