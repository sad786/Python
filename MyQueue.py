class MyQueue:
	class Node:
		def __init__(self,data):
			self.next = None
			self.data = data
		
	
	def __init__(self):
		self.first = None
		self.last = None
	
	def add(self,data):
		node = self.Node(data)
		
		if self.first is None:
			self.first = self.last = node
		else:
			self.last.next = node
			self.last = node
	
	def remove(self):
		if self.first is None:
			return None
		
		data = self.first.data
		self.first = self.first.next
		return data
	
	def __str__(self):
		st = ""
		
		temp = self.first
		while temp != None:
			st += str(temp.data)+" "
			temp = temp.next
		
		return st


if __name__=='__main__':

	mq = MyQueue()
	mq.add(50)
	mq.add(40)
	mq.add(30)
	mq.add(60)
	
	print(mq)
	
	mq.remove()
	
	print(mq)