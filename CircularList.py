from LinkedList import *

def make_circle(list1,node):
	temp = list1.head
	while temp.next != None:
		temp = temp.next
	
	temp.next = node
	

def find_loop(list1):
	
	first = list1.head
	
	while first!= None:
		second = first.next
		
		while second != None:
			if first == second:
				return first
			
			second = second.next
	
	return None

list1 = LinkedList()

list1.append('A')
list1.append('B')
list1.append('C')
list1.append('D')
list1.append('E')

make_circle(list1,list1.get(3))


print("The Circular Loop is ",find_loop(list1))
