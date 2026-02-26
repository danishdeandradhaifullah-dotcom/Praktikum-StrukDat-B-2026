# 3. Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"} 

#  a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang) 
keduaSesi = sesi_pagi.intersection(sesi_siang)
print(keduaSesi)
# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua sesi tanpa duplikat).
unikSesi = sesi_pagi.symmetric_difference(sesi_siang)
print(unikSesi)
# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
sesi_hari_ini = keduaSesi.symmetric_difference(unikSesi)
print(sesi_hari_ini)