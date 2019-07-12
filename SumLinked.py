class Node:
	def __init__(self,data):
		self.next = None
		self.data = data
	
	def insert(self,data):
		node = Node(data)
		node.next = self
		return node

	
	def __str__(self):
		st = ""
		while self!=None:
			st +=" "+str(self.data)
			self = self.next
	
		return st
		

def give_sum(list1,list2):
	c = 0
	sum_list = None
	
	while list1!=None and list2!=None:
		ts = list1.data +list2.data + c
		
		list1 = list1.next
		list2 = list2.next
		
		print(ts)
		
		if ts>9:
			c = ts%9
			ts = ts//10
		else:
			c = 0
		
		node = Node(ts)
		node.next = sum_list
		sum_list = node
		
	while list1 != None:
		node = Node(list1.data)
		node.next = sum_list
		sum_list = node
		
		list1 = list1.next
	
	while list2!=None:
		node = Node(list2.data)
		node.next = sum_list
		sum_list = node
		
		list2 = list2.next
	
	if c>0:
		node = Node(c)
		node.next = sum_list
		sum_list = node
		
	return sum_list
	
	
list1 = Node(5)
list1 = list1.insert(1)
list1 = list1.insert(3)

print(list1)

list2 = Node(6)
list2 = list2.insert(0)
list2 = list2.insert(7)

print(list2)

print("The sum is ",give_sum(list1,list2))