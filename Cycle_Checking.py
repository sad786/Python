def get_parent(list,ch):
	p = list[ch]
	return ch if p<=0 else p
	
def set_parent(list,ch1,ch2):
	p1,ch = 0,0
	v1,v2 = list[ch1],list[ch2]
	if abs(v1)<=v2:
		list[ch1] +=list[ch2]
		list[ch2] = ch1
		p1,ch = ch1,ch2
	else:
		list[ch2] +=list[ch1]
		list[ch1] = ch2
		p1,ch = ch2,ch1
	for i in range(1,len(list)):
		if list[i]==ch:
			list[i] = p1
			
			
n = int(input("Enter no of vertices in the Graph: "))

graph_set = [-1]*(n+1)	# -1 indicate that all the vertices are initialy parent of itself

edge_set = [] 	# it will store edges of the graph
for _ in range(n):
	u,v = [int(x) for x in input("Enter next edge").split()]	# get the edge from user
	edge_set.append([u,v])	# it will store all the edge info
	
for e in edge_set:
	u,v = e[0],e[1]
	parent1 = get_parent(graph_set,u)
	parent2 = get_parent(graph_set,v)
	if parent1==parent2:
		edge_set.remove(e)
	else:
		set_parent(list,parent1,parent2)
		
		
print("Minimum cost spanning tree is here ",edge_set)