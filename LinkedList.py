class LinkedList:
	def __init__(self):
		self.head = None
	
	# to represent a single node
	# where element will be stored
	class Node:
		def __init__(self,data):
			self.data = data
			self.next = None
	
	
	#to insert element at the last 
	# O(n) time 
	def append(self,data):
		node = self.Node(data)
		node.next = None
		if self.head is None:
			self.head = node
		else:
			temp = self.head
			while not(temp.next is None):
				temp = temp.next
			temp.next = node
	
	
	#to insert element at specified position
	# O(n) average time
	def insert(self,data,pos=0):
		node = self.Node(data)
		if self.head is None:
			self.head = node
		
		elif pos<=1:
			node.next = self.head
			self.head.next = node
		else:
			cur = self.head
			while pos>2 and cur.next != None:
				cur = cur.next
				pos -=1
			
			node.next = cur.next
			cur.next = node
	
	
	# returns the length of the LinkedList
	# ( number of elements contained in the list)
	# O(n) time 
	def size(self):
		count = 1
		list = self.head
		while list.next!= None:
			list = list.next
			count +=1
		
		return count
	
	
	# to remove middle element of the LinkedList
	# ( 5->2->3 ) 2 will be removed
	# O(n/2) time 
	def remove_middle(self):	
		s = self.size()
		if s==1:
			data = self.head.data
			self.head = None
			return data
		
		cur = self.head
		for _ in range(1,s//2 - 1):
			cur = cur.next
		
		data = cur.next.data
		cur.next = cur.next.next
		
		return data

	
	def get(self,pos=0):
		
		temp = self.head
		while pos>1:
			temp = temp.next
			pos -=1
		
		return temp
		
	# this function will remove all the duplicate elements
	# worst case time O(n2) and average case time O(n)
	def unique():
		if self.head is None:
			return self
		
		list = self.head
		while list!= None:
			data = list.data
			pre = list
			curr = list.next
			while curr != None:
				if curr.data == data:
					pre.next = curr.next
				else:
					pre = curr

				curr = curr.next
			
			list = list.next
		
	# to print the list onto the console
	# this will return the string format of element 
	def __str__(self):
		st = ""
		list = self.head
		while list!= None:
			st += str(list.data)+" "
			list = list.next
		
		return st


if __name__=='__main__':
	list = LinkedList()
	list.append(8)
	list.insert(50,9)
	list.append(40)
	list.append(70)
	
	print(list)