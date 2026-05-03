class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        print("\n[INFO] Membangun Struktur Gudang...")
        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")
        print("[INFO] Struktur berhasil dibuat.\n")

    def traverse_preorder(self,node):
        if node is not None:
            print(f"{node.data}", end=" - ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self,node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(f"{node.data}", end=" - ")
            self.traverse_inorder(node.right)

    def traverse_postorder(self,node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(f"{node.data}", end=" - ")

    def get_leaf_nodes(self,node):
        if node is not None:
            if node.left is None and node.right is None:
                print(f"{node.data}", end=", ")
            self.get_leaf_nodes(node.left)
            self.get_leaf_nodes(node.right)



tree = BinaryTree()
print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("=" * 36)

tree.insert_manual()
print("\nHasil Audit:")
print('1. Pre-Order: ',end="")
tree.traverse_preorder(tree.root)
print('\n2. In-Order: ',end="")
tree.traverse_inorder(tree.root)
print('\n3. Post-Order: ',end="")
tree.traverse_postorder(tree.root)

print(f"\n\n[DATA] Gudung Ujung (Leaf Nodes): ",end="")
tree.get_leaf_nodes(tree.root)
print()
print(f"=" * 36)
print("Audit Selesai!")
