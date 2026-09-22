def main():
    print("CSE25149  T.RAMCHARAN REDDY\n")
    my_LinkedList = None
    while True:
        print(
            "1.create\n2.insert at beginning\n3.insert at end\n4.insert at certain position\n5.delete first node\n6.delete last node\n7.delete specific node\n"
            "8.count\n9.display\n10.exit"
        )
        option = input("Enter your choice: ")
        if option == "1":
            my_LinkedList = LinkedList()
            print("linked list successfully created")
        elif my_LinkedList is None:
            print("please create the linked list first (option 1)")
        elif option == "2":
            my_LinkedList.insert_begin(int(input    ("Enter the data: ")))
            print("element is inserted")
        elif option == "3":
            my_LinkedList.insert_end(int(input("Enter the data: ")))
            print("element inserted")
        elif option == "4":
            my_LinkedList.insert_position(
                int(input("Enter the data: ")), int(input("Enter the position: "))
            )
        elif option == "5":
            my_LinkedList.delete_begin()
        elif option == "6":
            my_LinkedList.delete_end()
        elif option == "7":
            my_LinkedList.delete_position(int(input("Enter position: ")))
        elif option == "8":
            count = my_LinkedList.size()
            print("the size of linked list is {}".format(count))
        elif option == "9":
            my_LinkedList.display()
        elif option == "10":
            print("exiting the program")
            break
        else:
            print("option not defined")


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_begin(data)
            return
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def size(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count

    def insert_position(self, data, pos):
        # positions are 1-indexed: pos=1 means new head
        n = self.size()
        if pos < 1 or pos > n + 1:
            print("position not available")
            return
        if pos == 1:
            self.insert_begin(data)
            print("element inserted")
            return
        node = Node(data)
        temp = self.head
        count = 1
        while count < pos - 1:
            temp = temp.next
            count += 1
        node.next = temp.next
        temp.next = node
        print("element inserted")

    def display(self):
        if self.head is None:
            print("The linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def delete_begin(self):
        if self.head is None:
            print("The Linked list is empty")
            return
        self.head = self.head.next
        print("first node deleted")

    def delete_end(self):
        if self.head is None:
            print("The Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            print("last node deleted")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        print("last node deleted")

    def delete_position(self, pos):
        # positions are 1-indexed: pos=1 means head
        if self.head is None:
            print("Empty linked list")
            return
        n = self.size()
        if pos < 1 or pos > n:
            print("position does not exist")
            return
        if pos == 1:
            self.head = self.head.next
            print("node at position is deleted")
            return
        temp = self.head
        count = 1
        while count < pos - 1:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
        print("node at position is deleted")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    main()