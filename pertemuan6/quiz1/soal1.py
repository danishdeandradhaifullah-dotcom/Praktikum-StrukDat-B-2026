def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Harga harus lebih dari nol")
        return None
    if stok < 0:
        print("Stok tidak boleh negatif")
        return None
    
    return {
        'nama': nama,
        'harga': harga,
        'stok': stok
    }

list = []
for i in range(3):
    nama = input("Nama buku: ")
    harga = float(input("Harga buku: "))
    stok = int(input("Stok buku: "))

    buku = tambah_buku(nama, harga, stok)

    if buku is not None:
        list.append(buku)

for b in list:
    print(f'{b['nama']} | Harga: {b['harga']} | Stok: {b['stok']}')


    
    
