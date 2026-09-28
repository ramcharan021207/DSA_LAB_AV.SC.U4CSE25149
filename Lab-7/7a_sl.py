# cse25149 Ramcharan
class Node:
    def __init__(self, key):
        self.key = key    
        self.next = None  

class MyQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0     

    def enqueue(self, x):
        temp = Node(x) 
        
        if self.rear is None:
            self.front = temp  
            self.rear = temp
        else:
            self.rear.next = temp 
            self.rear = temp       
        
        self.size += 1  

    def dequeue(self):
        if self.front is None:
            return None  
        res = self.front.key

        self.front = self.front.next

        if self.front is None:
            self.rear = None
        
        self.size -= 1  
        return res  


    def getFront(self):
        if self.front is None:
            return None
        return self.front.key  

    def getRear(self):
        if self.rear is None:
            return None
        return self.rear.key  

    def isEmpty(self):
        return self.front is None  

    def getSize(self):
        return self.size  


# Example 
if __name__ == "__main__":
    queue = MyQueue()
    print("cse25149 Ramcharan\n")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print(queue.dequeue())  

    print(queue.getFront())  
    print(queue.getRear())  

    print(queue.isEmpty())  
    
    print(queue.getSize())  
    
    print(queue.dequeue())  
    print(queue.dequeue())  

    print(queue.isEmpty())