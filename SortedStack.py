class Stack:
	class Node:
		def __init__(self,data):
			self.data = data
			self.next = None
	
	def __init__(self):
		self.top = None
	
	
	# to know whether stack is empty
	def isEmpty(self):
		return self.top is None
	
	
	#to push element onto the stack
	def push(self,data):
		node = self.Node(data)
		
		if self.isEmpty():
			self.top = node
		else:
			pre = self.top
			temp = self.top
			
			while temp != None and temp.data<=node.data:
				pre = temp
				temp = temp.next
			
			if pre == self.top:
				node.next = self.top
				self.top = node
			else:
				node.next = pre.next
				pre.next = node
	
	

	# to remove element from stack
	def pop(self):
		if self.isEmpty():
			reurn -1
		
		data = self.top.data
		self.top = self.top.next
		return data
		
	
	#to know the top element
	def peek(self):
		return -1 if self.isEmpty() else self.top.data
	
	
	#to print data to teh console
	def __str__(self):
		st = ""
		temp = self.top
		
		while temp != None:
			st += str(temp.data)+" "
			temp = temp.next
		
		return st


if __name__=='__main__':
	st = Stack()
	st.push(50)
	st.push(40)
	st.push(90)
	st.push(5)
	
	st.push(50)
	st.push(40)
	st.push(90)
	st.push(5)
	
	st.push(50)
	st.push(40)
	st.push(90)
	st.push(5)
	
	print(st)
	print('top of the stack is ',st.peek())