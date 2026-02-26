mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75} } 

for nim in mahasiswa:
    if mahasiswa[nim]["ipk"] > 3.5:
        print(mahasiswa[nim]["nama"])

for nim, mhs in mahasiswa.items():
    if mhs["ipk"] > 3.5:
        print(mhs['nama'])

