katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
{'nama': 'Python for Beginners', 'harga': 50000, 'stok': 10} ]

def cari_buku(katalog, keyword = str):
    keyword = keyword.lower()

    list = []

    for i in katalog:
        if keyword in i['nama'].lower():
            list.append(i)

    if len(list) == 0:
        print("Buku tidak ditemukan")

    return list

keyword = input('Masukkan keyword: ')

hasil = cari_buku(katalog, keyword)

for x in hasil:
    print(f"Nama: {x['nama']} | Harga: Rp {x['harga']} | Stok: {x['stok']}")


        
