class Pasien():
    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit
        
    def get_id (self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_penyakit(self):
        return self.__penyakit
    
    def tampilkan_info(self):
        return self.__id, self.__nama, self.__penyakit
    
    @staticmethod
    def hitung_pasien(self):
        count = 0
            
       
class PasienPrioritas(Pasien):
    def __init__(self, id, nama, penyakit):
        super().__init__(id, nama, penyakit)

p1 = Pasien('001', "Danish", 'Maag')
hasil = p1.tampilkan_info()
for info in hasil:
    print(info)
    
