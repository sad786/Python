n = int(input())
for i in range(n):
	print('  '*(n-i-1)+chr(65+i),end=' ')
	if i>0:
		print('  '*(2*i-1)+chr(65+i),end='')
	print()
for i in range(n-1):
	print('  '*(i+1)+chr(65+n-i-2),end='')
	if i<n-2:
		print('  '*(2*(n-i-2)-1)+' '+chr(65+n-i-2))