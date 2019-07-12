
class Stack:

	def __init__(self):
		self.__top = None
		self.size = 0
		self.min = None
		
	#to represent a single element
	class Node:
		def __init__(self,data):
			self.data = data
			self.below = None
			self.next_min = 0;


	#to insert element at the top
	def push(self,data):
		
		node = self.Node(data)
		
		node.below = self.__top
		self.__top = node
		
		if self.min is None:
			self.min = node
			node.next_min = None
		elif self.min.data > node.data:
			node.next_min = self.min
			self.min = node	
		else:
			temp = self.min
			while temp.next_min != None and temp.data<node.data:
				temp  = temp.next_min
			
			if temp.next_min is None:
				node.next_min = temp.next_min
				temp.next_min = node
			else:
				node.next_min = temp
				temp = self.min
				
				while temp.next_min!=node.next_min:
					temp = temp.next_min
				
				temp.next_min = node
			
		
		self.size +=1
	
	#to delete element from the top of the stack
	def pop(self):
		if self.__top is None:
			return None
		
		el = self.__top.data
		
		self.__top = self.__top.below
		self.size -= 1
		return el
	
	
	#to know the top element 
	def peek(self):
		if self.__top is None:
			return None
		
		return self.__top.data
		
	
	#to know the last element 
	def last(self):
		if self.__top is None:
			return None
		
		temp = self.__top
		
		while temp.below != None:
			temp = temp.below
		
		return temp.data
	
	
	
	#to print all minimum element
	def printMin(self):
		temp = self.min
		
		while temp != None:
			print(temp.data,end=' ')
			temp = temp.next_min
	
	#to know the minimum element of the stack
	def getMin(self):
		if self.min is None:
			return -1
		
		return self.min.data
	
	
	#to print element to the console
	def __str__(self):
	
		st = " --------"
		
		temp = self.__top
		
		while temp != None:
			
			st += "\n |  "+str(temp.data)+"  |\n --------"
			
			temp = temp.below
		
		return st
	
	
if __name__== "__main__":

	stack = Stack()
	stack.push(50)
	stack.push(60)
	stack.push(40)
	stack.push(30)
	stack.push(99)
	stack.push(46)
	stack.push(37)
	stack.push(78)
	stack.push(60)
	
	print(stack)
	
	print('After deleting the top element ',stack.pop())
	
	print(stack)
	
	print('size of the stack',stack.size)
	
	print('top element of the stack ',stack.peek())
	
	print('last element of the stack ',stack.last())
	
	stack.printMin()