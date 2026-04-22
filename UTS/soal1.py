pasien_hari_ini = [ {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},]

def tampilkan_pasien(data):
    print('\n===== DATA PASIEN KLINIK =====')
    print(f'{"ID":<5}|{"Nama":<8}|{"Usia":<6}|{"Penyakit":<10}|{"Status Bayar":<5}')
    print('-' * 45)
    for info in data:
        if info['bayar']:
            print(f'{info['id']:<5}|{info['nama']:<8}|{info['usia']:<6}|{info['penyakit']:<10}|{'Lunas':<15}')
        else:
            print(f'{info['id']:<5}|{info['nama']:<8}|{info['usia']:<6}|{info['penyakit']:<10}|{'Belum Bayar':<15}')

def filter_belum_bayar(data):
    print('\n===== PASIEN BELUM BAYAR =====')
    total = 0
    number = 1
    for info in data:
        status = info['bayar']
        if not status:
            print(f'{number}. {info['nama']}')
            total += 1
            number += 1
    print(f'Total belum bayar: {total}')

tampilkan_pasien(pasien_hari_ini)
filter_belum_bayar(pasien_hari_ini)

            
    








