def tampilkan_history(self):
        current = self.head
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("null")