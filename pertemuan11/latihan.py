class Node:
    def __init__(self,nama,keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self,nama,keluhan):
        new_pasien = Node(nama,keluhan)
        if self.tail is None:
            self.head = self.tail = new_pasien
            self._size += 1
            return
        self.tail.next = new_pasien
        self.tail = new_pasien
        self._size += 1

    def isEmpty(self):
        if self._size == 0:
            return "Iya, Antrian masih kosong"
        return self._size == 0
    
    def dequeue(self):
        if self.isEmpty():
            return "Antrian masih kosong"
        temp = self.head
        self.head = temp.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        return (f"Dokter memanggil {temp.nama} (keluhan: {temp.keluhan})")
    
    def peek(self):
        if self.isEmpty():
            return "Antrian masih kosong"
        return (f"Pasien berikutnya {self.head.nama} - {self.head.keluhan}")
    
    def size(self):
        return (f"Jumlah pasien menunggu: {self._size} orang")
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return self._size
    
    def printQueue(self):
        global noAntrian
        temp = self.head
        while temp:
            print(f"{temp.nama} terdaftar dengan keluhan: {temp.keluhan} (No. Antrian {noAntrian})", end="\n")
            temp = temp.next
            noAntrian += 1
        print()
    
    def newest(self):
        global noAntrian
        return (f"{self.tail.nama} terdaftar dengan keluhan: {self.tail.keluhan} (No. Antrian {noAntrian}) ")

noAntrian = 1
antrian = Queue()
print("=" * 36)
print("  SISTEM ANTRIAN POLI UMUM")
print("  RS Sehat Bersama")
print("=" * 36)

print(f"\nApakah antrian kosong?: {antrian.isEmpty()}",)
antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")
antrian.printQueue()
print(antrian.size())
print(antrian.peek())
print(antrian.dequeue())
antrian.enqueue("Dodi", "nyeri perut")
print(antrian.newest(), end="\n")
print("\nAntrian saat ini")
antrian.printQueue()
print(antrian.dequeue())
print(antrian.size())
print(f"Sesi poliklinik selesai. Antrian dikosongkan {antrian.clear()}")
print(f"{antrian.isEmpty()}")


        