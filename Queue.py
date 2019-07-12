
class Queue:

	#constructor of Queue
	def __init__(self):
		self.__head = None
		self.__last = None
	
	
	#to represent a single element
	class Node:
		def __init__(self,data):
			self.next = None
			self.data = data
	
	
	
	# insert element to the last
	def add(self,data):
		node = self.Node(data)
		node.next = None
		
		if self.__head is None:
			self.__head = node
			self.__last = node

		else:
			self.__last.next = node
		
			self.__last = node
			
	
	
	#delete first element from the queue
	def delete(self):
		if self.__head is None:
			return None
		elif self.__head is self.__last:
			el = self.head.data
			self.__head = self.__last = None
			return el
		
		
		el = self.__head.data
		self.__head = self.__head.next
		return el
		
	

	#return element as a String
	def __str__(self):
		st = ""
		
		temp = self.__head
		
		while temp != None:
			st += str(temp.data)+" "
			temp =  temp.next
		
		return st
		
		
		
if __name__=='__main__':
	queue = Queue()
	
	queue.add(15)
	queue.add(20)
	queue.add(30)
	queue.add(50)
	queue.add(60)
	
	print(queue)
	
	print("Deleting the element",queue.delete())
	
	print(queue.head.data)
