class BinaryTree:
    def __init__(self,size):
        self.tree = [None]*size
        self.size = size
    def insert_root(self,data):
        self.tree[0] = data
    def insert_left(self,parent_index,data):
        child_index = 2*parent_index + 1
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range.")
    def insert_right(self,parent_index,data):
        child_index = 2*parent_index + 2
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("index out of range")
    def pre_trav(self,index=0):
        if index>self.size or self.tree[index] == None:
            return
        print(self.tree[index],end=" ")
        self.pre_trav(2*index+1)
        self.pre_trav(2*index+2)
    def In_trav(self,index=0):
        if index>self.size or self.tree[index] == None:
            return None
        self.In_trav(2*index+1)
        print(self.tree[index],end=" ")
        self.In_trav(2*index+2)
    def post_trav(self,index=0):
        if index>self.size or self.tree[index] == None:
            return
        self.pre_trav(2*index+1)
        self.pre_trav(2*index+2)
        print(self.tree[index],end = " ")
    def level_trav(self):
        for value in self.tree:
            if value is not None:
                print(value,end=" ")
bt = BinaryTree(20)
bt.insert_root(10)
bt.insert_left(0,5)
bt.insert_right(1,8)
bt.insert_right(0,16)
bt.insert_left(2,15)
bt.insert_right(2,20)
bt.insert_right(6,14)
print("Preorder")
bt.pre_trav()
print("Inorder")
bt.In_trav()
print("Postorder")
bt.post_trav()