n = int(input())


print('* '*n)

for i in range(n-1):
	print('*'+'  '*(n-2)+' *')
print('* '*n)

for i in range(n-1):
	print('  '*(n-1)+'*')

print('* '*n)


