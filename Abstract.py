
class Parent:
	def __init__(self):
		print("I am Parent id ",id(self))
	
	
	def method(self,obj1):
		print("I am Parent method")
		
class Child(Parent):
	def __init__(self):
		super.__init__()
		print("I am Child id ",id(self))
		

	def method(self,obj1):
		print("Hello I am Overriden Method")
		super.__init__().method(obj1)
		

obj = Child()
obj.method(obj)