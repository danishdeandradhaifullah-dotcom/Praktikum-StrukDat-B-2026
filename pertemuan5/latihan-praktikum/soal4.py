# 4. Diberikan data buku dalam bentuk dictionary:
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]
# a. Ubah jumlah buku menjadi 8.
transaksi[0]["jumlah"] = 8
print(transaksi)
# b. Tambahkan 2 produk baru.
transaksi.append({"produk": "Mousepad", 'harga': 30000, 'jumlah': 10 })
transaksi += [{"produk": "Laptop","harga": 10000000,"jumlah": 7}]

# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan.
for i, pendapat in enumerate (transaksi, start=1):
    produk = pendapat["produk"]
    hasil = pendapat['harga'] * pendapat["jumlah"]
    print(f"{i}. Produk: {produk} | Total: {hasil}", end=" ")

# Tampilkan ringkasan seperti ini:
# Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
