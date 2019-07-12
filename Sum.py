num_list = [int(x) for x in input().split()]
sum = int(input("Enter the sum: "))
low = 0
hi = len(num_list)-1
found = False
while low<hi:
	s = num_list[low]+num_list[hi]
	if s==sum:
		found = True
		break
	elif s<sum:
		if num_list[low]<num_list[hi]:
			low +=1
		else:
			hi -=1
	else:
		if num_list[low]>num_list[hi]:
			low +=1
		else:
			hi -=1


print(found)