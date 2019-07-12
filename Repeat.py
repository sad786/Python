''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def get_first(num_list):
    for i in range(n-1):
        for j in range(i+1,n):
            if num_list[i]==num_list[j]:
                res = num_list[j]
                break	
def main():
    n = int(input().strip())

    res = -1
    num_list = []
    
    for _ in range(n):
		num_list.append(int(input()))
	print(get_first(num_list),end='')

main()
