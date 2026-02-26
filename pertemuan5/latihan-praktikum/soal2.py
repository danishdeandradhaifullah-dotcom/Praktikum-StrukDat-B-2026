# 2. Diberikan sebuah list yang berisi beberapa tuple. Setiap tuple berisi (Nama, Nilai): kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)] a. Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75,
# tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf [Nama], Anda harus remidi."

kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print(f"Selamat {nama}, Lulus!")
    elif nilai <=  75:
        print(f"Maaf {nama} harus remidi")