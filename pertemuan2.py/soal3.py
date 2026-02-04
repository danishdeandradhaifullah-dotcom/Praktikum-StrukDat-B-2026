kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

kelasSama = kelas_A.intersection(kelas_B)
print(f"Mata kuliah yang diambil oleh kedua kelas adalah = {kelasSama}")
kelasBeda = kelas_A.difference(kelas_B)
print(f"Mata kuliah yang hanya diambil oleh kelas A adalah = {kelasBeda}")
kelasUnik = kelas_A.symmetric_difference(kelas_B)
print(f"Mata kuliah yang unik yang diambil oleh kedua kelas adalah = {kelasUnik}")
