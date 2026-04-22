#1
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien D", 2)
print(antrean_array)


#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def tampilkan_antrean(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

    def insert_at_position(self, nama_pasien, posisi):

        newNode = Node(nama_pasien)

        if posisi == 1:
            newNode.next = self.head
            self.head = newNode
            return

        currentNode = self.head
        count = 1

        while currentNode.next and count < posisi - 1:
            currentNode = currentNode.next
            count += 1

        newNode.next = currentNode.next
        currentNode.next = newNode


node1 = Node("Danish")
node2 = Node("Jonathan")
node3 = Node("Islam")
node4 = Node("Fatih hamzah")

node1.next = node2
node2.next = node3
node3.next = node4


history = AntreanLinkedList()
history.head = node1

history.tampilkan_antrean()

history.insert_at_position("Gledis", 2)

history.tampilkan_antrean()

    



