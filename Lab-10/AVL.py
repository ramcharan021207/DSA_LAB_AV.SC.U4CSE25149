print("CSE25149 T. Ramcharan")
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.getBalance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# Main Program
tree = AVLTree()
root = None

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = tree.insert(root, value)

print("Inorder Traversal:")
tree.inorder(root)
