print("CSE25149 T. Ramcharan")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)

        return root

    # Search a node
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Find minimum value
    def minimum(self, root):
        while root.left:
            root = root.left
        return root.data

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self.minimum(root.right)
            root.right = self.delete(root.right, root.data)

        return root

# Main program
tree = BST()

while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        tree.root = tree.insert(tree.root, value)
        print("Node inserted successfully")

    elif choice == 2:
        key = int(input("Enter value to search: "))
        if tree.search(tree.root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter value to delete: "))
        if tree.search(tree.root, key):
            tree.root = tree.delete(tree.root, key)
            print("Node deleted successfully")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder Traversal:")
        tree.inorder(tree.root)

    elif choice == 5:
        print("Preorder Traversal:")
        tree.preorder(tree.root)

    elif choice == 6:
        print("Postorder Traversal:")
        tree.postorder(tree.root)

    elif choice == 7:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
