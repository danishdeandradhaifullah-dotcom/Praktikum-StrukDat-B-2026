mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75} } 


mahasiswa['004'] = {
    'nama' : 'Dina',
    'prodi' : 'Informatika',
    'ipk' : 3.8
}

total = 0

for nim, data in mahasiswa.items():
    if data['ipk'] > 3.5:
        print(data['nama'])

for nim,data in mahasiswa.items():
    total += data['ipk']

rata_rata = total / len(mahasiswa)
print(rata_rata)

