katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, ]

riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku = str, jumlah_beli = int):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():

            if buku['stok'] >= jumlah_beli:
                total = buku['harga'] * jumlah_beli
                buku['stok'] -= jumlah_beli

                print(f"Total yang harus dibayar: Rp {total}")
                riwayat_transaksi.add(buku['nama'])
                return
            
            else:
                print("Stok tidak mencukupi")
                return
        
    print("Buku tidak ditemukan")

for i in range(3):
    print(f'\nTransaksi {i+1}')
    nama = input("Nama buku: ")
    jumlah = int(input("Jumlah yang dibeli: "))
    proses_transaksi(katalog, nama, jumlah)

print("\nRiwayat Transaksi")
for b in riwayat_transaksi:
    print(b)

                
