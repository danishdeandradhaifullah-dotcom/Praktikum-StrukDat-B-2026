def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.data,end=" ")
        inOrder(node.right)