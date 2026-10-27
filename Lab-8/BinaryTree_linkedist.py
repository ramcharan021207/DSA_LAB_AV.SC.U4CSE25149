class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def in_order_trav(node):
        if node is None:
            return
        in_order_trav(node.left)
        print(node.data, end = ' ')
        in_order_trav(node.right)
def pre_order_trav(node):
        if node is None:
            return
        print(node.data, end=' ')
        pre_order_trav(node.left)
        pre_order_trav(node.right)
def post_order_trav(node):
        if node is None:
            return 
        post_order_trav(node.left)
        post_order_trav(node.right)
        print(node.data, end=' ')
def level_order_trav(self):
      
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
in_order_trav(root)