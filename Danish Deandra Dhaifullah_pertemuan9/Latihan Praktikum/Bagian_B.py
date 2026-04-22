#BAGIAN B
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            return

        temp = self.head
        while True:
            print(temp.nama, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to First)")

    def delete_head(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

cLL = CircularLinkedList()

cLL.insert_tail("Andi")
cLL.insert_tail("Budi")
cLL.insert_tail("Citra")
cLL.insert_tail("Dina")

cLL.print_antrian()

cLL.insert_tail('Edo')
print('\nSetelah ditambah Edo: ')
cLL.print_antrian()

cLL.delete_head()
print('\nSetelah dihapus Andi: ')
cLL.print_antrian()