import sys
def get_min_hour(N,P,sl):
	hours = max(sl)
	for i in range(len(sl)-P):
		p_list = sl[i:P+i]
		temp_hour = 0
		max_el = max(p_list)
		for l in p_list:
			if l<max_el:
				temp_hour +=max_el-l
		
		if temp_hour<=0:
			return 0
		elif temp_hour<hours:
			hours = temp_hour
	
	return hours
		
	

tc = int(input())

for i in range(tc):
	N,P = [int(s) for s in input().split()]
	sl = [int(s) for s in input().split()]
	min_hour = get_min_hour(N,P,sl)
	print('Case #{}: {}'.format(i+1,min_hour))
	sys.stdout.flush()
	
	
#######################################################	
def solve(students_needed, skills):
    skills.sort()
    min_hours = float('+inf')

    for i in range(0, len(skills) - students_needed + 1):
        _range = skills[i: i + students_needed]
        hours_needed = (max(_range) * students_needed) - sum(_range)
        if min_hours > hours_needed:
            min_hours = hours_needed
    return min_hours


def main():
    T = int(input())
    for case_n in range(1, T + 1):
        N, P = map(int, raw_input().split(' '))
        Si = map(int, raw_input().split(' '))
        result = solve(P, Si)
        print 'Case %s: %s' % (case_n, result)
main()

###########################################################
	