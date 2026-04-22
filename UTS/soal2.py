klinik = ('Klinik Sehat Bersama', "Jl.Merdeka No.10,Pekanbaru", "0761-12345")
pasien_hari_ini = [ {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},]

def info_klinik(data):
    for info in data:
        print(info)

def rekap_penyakit(data):
    total = 0
    unik = set()
    for info in data:
        if info['penyakit'] not in unik:
            unik.add(info['penyakit'])
            total += 1

    print(f'Jenis penyakit unik: {unik}')
    print(f'Jumlah jenis penyakit: {total}')

    print('Rekap per penyakit: ')  
    for dis in unik:
        print(f'{dis}: {total - 1}')

    print(f'Penyakit terbanyak :{unik} ({total - 1} pasien) ')
    
    return unik

info_klinik(klinik)
rekap_penyakit(pasien_hari_ini)



      




