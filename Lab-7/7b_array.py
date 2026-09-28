# cse25149 Ramcharan
class myQueue:
    def __init__(self, cap):
        self.arr = [0]*cap    
        self.front = 0 
        self.size = 0      
        self.capacity = cap    

    def enqueue(self, x):
        if self.size == self.capacity:
            print("Queue is full!")
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty!")
            return -1
        res = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return res

    def getFront(self):
        if self.size == 0:
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

if __name__ == "__main__":
    q = myQueue(5)
    print("cse25149 Ramcharan\n")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.getFront(), q.getRear())
    q.dequeue()
    print(q.getFront(), q.getRear())
    q.enqueue(40)
    print(q.getFront(), q.getRear())