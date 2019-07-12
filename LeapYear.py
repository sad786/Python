def getLeapYear(year):
	while True:
		if year%400==0:
			return year
		elif year%4==0 and year%100!=0:
			return year
		else:
			year +=1

if __name__=='__main__':
	leap_year_list = []
	cur_year = int(input("Enter any year :"))
	leap_year = getLeapYear(cur_year)
	
	for i in range(15):
		leap_year_list.append(leap_year)
		leap_year +=4
	print(leap_year_list)