def process(num):
	suffix = None
	
	if "." in num:
		suf = num[num.index(".")+1:]
		suffix = int(suf)/(10**len(suf))
		#print(suffix)
		
		num = int(num[:num.index(".")])
		
	else:
		num = int(num)
	
	bin_pre = []
	while num>0:
		bin_pre.insert(0,str(num%2))
		num //= 2
	
	
	if not(suffix is None):
		bin_pre.append(".")
		count = 0
		while count<20 and suffix>0:
			suffix = suffix*2
			ab = int(suffix)
			suffix =  suffix - ab
			bin_pre.append(str(ab))
			count +=1
		
		if count==20:
			return "Error"
	
	return ''.join(bin_pre)
	



if __name__=='__main__':
	num = input("Enter any decimal number: ").strip()
	
	binary = process(num)
	
	print(binary)