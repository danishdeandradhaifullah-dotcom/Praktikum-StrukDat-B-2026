    def height(self, node = None):
        if node is None:
            node = self.root

        if node is None:
            return -1

        if node.left:
            leftHeight = self.height(node.left)
        else:
            leftHeight -= 1

        if node.right:
            rightHeight = self.height(node.right)
        else:
            rightHeight -= 1

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1