#1 
history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0,keyword)

tambah_pencarian_array("Bing.com")

print(history_array)

#2
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node
        
    def tampilkan_history(self):
        current = self.head
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("null")

history = HistoryLinkedList()
history.tambah_pencarian_linked("python.org")
history.tampilkan_history()



