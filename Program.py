n = int(input())

house_list = {}

while n>1:
	s = input().split()
	h1 = int(s[0])
	h2 = int(s[2])
	
	if h1 in house_list.keys():
		house_list[h1].append(h2)
	else:
		house_list[h1] = [h2]
	
	if h2 in house_list.keys():
		house_list[h2].append(h1)
	else:
		house_list[h2] = [h1]
	n -=1
	
n = int(input())



