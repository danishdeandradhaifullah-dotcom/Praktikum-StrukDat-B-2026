class Node:
    def __init__(self,id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan ID: {id_buku}, Judul: '{judul}'")
            return 
        
        P = self.root
        Q = self.root

        while Q != None and new_node.id_buku != P.id_buku:
            P = Q
            if new_node.id_buku < P.id_buku:
                Q = P.left
            else:
                Q = P.right
                
        if new_node.id_buku == P.id_buku:
            return "Datanya duplikat"
        
        if new_node.id_buku < P.id_buku:
            P.left = new_node
            
        else:
            P.right = new_node

        print(f"[INSERT] Berhasil memasukkan ID: {id_buku}, Judul: '{judul}'")

    def search(self, id_buku):
        current = self.root

        while current:
            if id_buku == current.id_buku:
                print(f'\n[SEARCH] Mencari ID {id_buku}.... Ditemukan! Judul: {current.judul}')
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right

        print(f'[SEARCH] Mencari ID {id_buku}.... Data tidak ditemukan')
        return None
    
    def traversal_inorder(self,node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"ID: {node.id_buku} - '{node.judul}'",end="\n")
            self.traversal_inorder(node.right)

    def height(self, node = None):
        if node is None:
            node = self.root

        if node is None:
            return -1

        if node.left:
            leftHeight = self.height(node.left)
        else:
            leftHeight = -1

        if node.right:
            rightHeight = self.height(node.right)
        else:
            rightHeight = -1

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1
        
    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        print(f'\n[STATISTIK] ID Terkecil: {current.id_buku}')
        return current
    
    def get_max(self):
        current = self.root
        while current.right:
            current = current.right

        print(f'[STATISTIK] ID Terbesar: {current.id_buku}')
        return current

    
tree = BinarySearchTree()
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=" * 40)
tree.insert(50, "Dasar Pemrograman")
tree.insert(30, "Struktur Data")
tree.insert(70, "Kecerdasan Buatan")
tree.insert(20, "Matematika Diskrit")
tree.insert(40, "Basis Data")
tree.insert(60, "Jaringan Komputer")
tree.insert(80, "Sistem Operasi")
print("\n[INFO] Koleksi Buku (In-Order Traversal): ")
tree.traversal_inorder(tree.root)
tree.search(60)
tree.search(100)
tree.get_min()
tree.get_max()
print(f'\n[INFO] Tinggi (Height) Tree: {tree.height(tree.root)}')



