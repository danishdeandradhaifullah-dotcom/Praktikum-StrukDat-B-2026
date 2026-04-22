katalog = []
log_transaksi = []
riwayat_transaksi = set()

def tambah_buku(nama, harga, stok): 
    if harga <= 0:
         print("Harga tidak boleh kosong")
         harga = None
    if stok < 0:
        print("Stok tidak boleh negatif")
        stok = None
        
    return {
        "nama" : nama,
        "harga": harga,
        "stok": stok
    }

def proses_transaksi(katalog, nama_buku: str, jumlah_beli: int):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():

            if buku["stok"] >= jumlah_beli:
                total = buku["harga"] * jumlah_beli
                buku['stok'] -= jumlah_beli

                log_transaksi.append((buku['nama'], jumlah_beli, total))
                riwayat_transaksi.add(buku['nama'])

                print(f"Total yang harus dibayar: Rp. {total}")
                return
            
            else:
                print("Stok tidak mencukupi.")
                return
    
    print("Buku tidak ditemukan")

while True:

    print("\n==PyBook Store==")
    print("1. Tambah Buku")
    print("2. Tampilkan semua buku")
    print("3. Beli buku")
    print("4. Laporan penjualan")
    print("5. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == '1':
        nama = input("Nama buku: ")
        harga = float(input("Harga Buku: "))
        stok = int(input("Stok Buku: ")) 

        buku = tambah_buku(nama, harga, stok)
        if buku is not None:
            katalog.append(buku)

    elif pilihan == '2':
        print('\nDaftar Buku:')
        for buku in katalog:
            print(f"{buku['nama']} | Harga: {buku['harga']} | Stok: {buku['stok']}")

    elif pilihan == '3':
        nama = input("Nama buku: ")
        jumlah = int(input("Jumlah dibeli: "))
        proses_transaksi(katalog, nama, jumlah)

    elif pilihan == '4':

        total_pemasukan = 0
        frekuensi = {}

        for nama, jumlah, total in log_transaksi:
            total_pemasukan += total

            if nama in frekuensi:
                frekuensi[nama] += jumlah
            else:
                frekuensi[nama] = jumlah

        buku_terlaris = max(frekuensi, key = frekuensi.get) if frekuensi else None

        print('\nLaporan Penjualan')
        print(f"Total pemasukan: {total_pemasukan}")

        if buku_terlaris:
            print(f"Buku Terlaris: {buku_terlaris}")

    elif pilihan == '5':
        print("Terimakasih telah menggunakan pybook store")
        break

    else:
        print("Menu tidak valid")