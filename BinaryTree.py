

# this is binary search tree
class BinTree:
	def __init__(self):
		self.root = None
	
	# to represent a single node 
	class Node:
		def __init__(self,data):
			self.left = None
			self.data = data
			self.right = None
			
	
	#to insert element into binary search tree
	# O log(n) time 
	def insert(self,data):
		node = self.Node(data)
		
		if self.root is None:
			self.root = node
		
		else:
			temp = self.root
			pre = temp
			
			while temp != None:
				pre = temp
				
				if node.data<temp.data:
					temp = temp.left
				else:
					temp = temp.right
			
			if node.data<pre.data:
				pre.left = node
			else:
				pre.right = node
		
	#
	def traverseInorder(self,root):
		if root is None:
			return 
		
		self.traverseInorder(root.left)
		print(root.data,end=' ')
		self.traverseInorder(root.right)
		
		
	#to inorder traversing of binary search tree inorder ie first left node then parent and then right node
	# O(n) time 
	def inorder(self):
		if self.root is None:
			print("The Tree is Empty")
			return 
		
		print()
		temp = self.root
		self.traverseInorder(temp)
	

	def traversePreorder(self,root):
		if root is None:
			return
		
		print(root.data,end=' ')
		self.traversePreorder(root.left)
		self.traversePreorder(root.right)
	
	# to traverse tree in preorder i.e first Root , then left and right node
	# O(n) time 
	def preorder(self):
		if self.root is None:
			print("The Tree is Empty")
			return
		
		print()
		temp = self.root
		self.traversePreorder(temp)
		
	
	def traversePostorder(self,root):
		if root is None:
			return 
		
		self.traversePostorder(root.left)
		self.traversePostorder(root.right)
		print(root.data,end=' ')
		
	
	# to traverse the tree in postorder ie first left node then right node and then parent
	# O(n) time 
	def postorder(self):
		if self.root is None:
			print("The Tree is Empty")
			return 
		
		print()
		self.traversePostorder(self.root)
		
		

if __name__ =='__main__':
	bt = BinTree()
	
	bt.insert(50)
	bt.insert(60)
	bt.insert(70)
	bt.insert(40)
	bt.insert(30)
	
	bt.insert(15)
	bt.insert(55)
	bt.insert(66)
	bt.insert(60)
	bt.insert(34)
	bt.insert(20)
	bt.insert(53)
	bt.insert(52)
	bt.insert(64)
	
	print('Preorder of Tree is ->',end=' ')
	bt.preorder()
	
	print('Inorder of Tree is ->',end=' ')
	bt.inorder()
	
	print('Postorder of Tree is ->',end=' ')
	bt.postorder()