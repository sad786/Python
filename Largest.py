def process(num):
	bi = bin(num)
	one = bi.count('1')
	
	temp = num -1
	while bin(temp).count('1') != one:
		temp -=1
	
	smallest = temp
	
	temp = num +1
	
	while bin(temp).count('1') != one:
		temp +=1
	
	largest = temp
	
	return smallest,largest
	


if __name__=='__main__':
	num = int(input("Enter any number :"))
	print(process(num))