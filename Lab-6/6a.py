# Ramcharan AV.SC.U4CSE25149
class Stack:
	def __init__(self, capacity):
		self.items = [None] * capacity
		self.capacity = capacity
		self.top = -1

	def push(self, value):
		if self.top == self.capacity - 1:
			print("Stack Overflow")
			return
		self.top += 1
		self.items[self.top] = value
		print(f"{value} pushed onto the stack")

	def pop(self):
		if self.top == -1:
			print("Stack Underflow")
			return
		value = self.items[self.top]
		self.items[self.top] = None
		self.top -= 1
		print(f"Popped element: {value}")

	def peek(self):
		if self.top == -1:
			print("Stack is empty")
		else:
			print(f"Top element: {self.items[self.top]}")

	def display(self):
		if self.top == -1:
			print("Stack is empty")
		else:
			print("Stack (top to bottom):", self.items[self.top::-1])

print("cse25149 Ramcharan\n") 
stack = Stack(5) 
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