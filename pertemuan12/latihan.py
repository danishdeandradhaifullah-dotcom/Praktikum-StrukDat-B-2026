class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self,data):
        self.root = Node(data)

    def insert_left(self,parent_node,data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self,parent_node,data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.data,end=" ")
        inOrder(node.right)

tree = BinaryTree()
tree.insert_root("F")
tree.insert_left(tree.root, "B")
tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D")
tree.insert_left(tree.root.left.right, "C")
tree.insert_right(tree.root.left.right, "E")
tree.insert_right(tree.root, "G")
tree.insert_right(tree.root.right, "I")
tree.insert_left(tree.root.right.right,"H")



inOrder(tree.root)



        