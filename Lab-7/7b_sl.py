# cse25149 Ramcharan
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None


def enQueue(q, value):
    newNode = Node(value)

    if q.front is None:
        q.front = newNode
    else:
        q.rear.next = newNode

    q.rear = newNode
    q.rear.next = q.front


def deQueue(q):
    if q.front is None:
        return -1

    value = None

    if q.front == q.rear:
        value = q.front.data
        q.front = q.rear = None
    else:
        temp = q.front
        value = temp.data
        q.front = q.front.next
        q.rear.next = q.front

    return value
    

def front(q):
	front = q.front

	if front is None:
		return -1
	
	return front.data


def rear(q):
	rear = q.rear

	if rear is None:
		return -1

	return rear.data

def printQueue(q):
    if q.front is None:
        return

    curr = q.front
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == q.front:
            break
    print()

if __name__ == "__main__":
    q = Queue()
    print("cse25149 Ramcharan\n")
    enQueue(q, 14)
    enQueue(q, 22)
    enQueue(q, 6)
    enQueue(q, 20)
    
    print("Front value =", front(q))
    print("Rear value =", rear(q))

    printQueue(q)

    print("Deleted value =", deQueue(q))
    print("Deleted value =", deQueue(q))

    printQueue(q)