import math

# to get nth prime number
# O(n*m) where n is the input and m is sqare root of the input
def getNPrime(n):
	if n<=0:
		return -1
	
	pr = 2
	count =0
	while n>1:
		pr +=1
		sq = int(math.sqrt(pr))
		
		is_prime = True
		for i in range(2,sq+1):
			count +=1
			if pr%i==0:
				is_prime = False
				break
		
		if is_prime:
			n -=1
	print('total count is ',count)
	return pr

# to get nth fibonacci number
# O(n) time
def fib(n):
	t1,t2 = 0,1
	next = t1+t2
	for i in range(1,n):
		next = t1+t2
		t1 = t2
		t2 = next
	
	#print(arr)
	return next


# to call suitable function 
# as per the input	
def process(input):
	if input%2==0:
		return getNPrime(input//2)
	else:
		n = input//2 + 1
		#print(n)
		return fib(n)
	
	


#exeution start from here
if __name__=='__main__':
	num = int(input("Enter the number"))
	
	print('The nth term of series is ',process(num))