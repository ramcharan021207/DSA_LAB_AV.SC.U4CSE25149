class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		node = Node(data)
		node.next = self.top
		self.top = node
		print(f"{data} pushed onto the stack.")

	def pop(self):
		if self.top is None:
			print("Stack Underflow")
			return
		data = self.top.data
		self.top = self.top.next
		print(f"{data} popped from the stack.")

	def peek(self):
		if self.top is None:
			print("Stack is empty")
		else:
			print("Top element:", self.top.data)

	def display(self):
		if self.top is None:
			print("Stack is empty")
			return
		current = self.top
		print("Stack elements:")
		while current is not None:
			print(current.data, end=" ")
			current = current.next
		print()

print("cse25149 Ramcharan\n") 
stack = Stack()

stack.push(10) 
stack.push(20) 
stack.push(30) 
stack.push(40) 
stack.push(50) 
stack.display() 
stack.pop() 
stack.pop() 
stack.display() 
stack.peek() 
stack.pop() 
stack.pop() 
stack.pop() 
stack.pop() 