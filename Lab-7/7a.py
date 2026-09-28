# queue using array.
# cse25149 Ramcharan
class Queue:
    def __init__(self, q_size):
        self.arr = [0] * q_size
        self.size = 0
        self.capacity = q_size
        self.front = 0
    def enqueue(self, x):
        
        if self.size == self.capacity:
            return
        
        self.arr[self.size] = x
        
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            return

        for i in range(1, self.size):
            self.arr[i-1] = self.arr[i]

        self.size -= 1
    def getFront(self):
        if self.size == 0:
            return -1
        
        return self.arr[self.front]
    def display(self):
        
        for i in range(self.front, self.size):
            print(self.arr[i], end=" ")
        print()

if __name__ == "__main__":
    q = Queue(4)
    print("cse25149 Ramcharan\n")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.getFront())
    q.dequeue()
    q.enqueue(4)
    q.display()