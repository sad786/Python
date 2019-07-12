n = int(input())

print('* '*n)
for i in range(n):
	print('*')

print('* '*(n-1))

for i in range(n-1):
	print(' '*(n-1)+'  *')

print('* '*(n-1))