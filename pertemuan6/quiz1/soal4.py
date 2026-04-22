level_diskon = (
(500000, 15), # belanja >= 500.000 -> diskon 15%
(300000, 10), # belanja >= 300.000 -> diskon 10%
(100000, 5), # belanja >= 100.000 -> diskon 5%
(0, 0), # default -> tidak ada diskon 
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    
    batas, diskon = level_diskon[index]

    if total_belanja >= batas:
        nominal_diskon = total_belanja * diskon/100
        total_bayar = total_belanja - nominal_diskon
        return(diskon, nominal_diskon, total_bayar)
    
    return hitung_diskon(total_belanja, level_diskon, index + 1)

total_belanja = int(input("Total Belanja: "))

persen, nominal, total_bayar = hitung_diskon(total_belanja, level_diskon)

print("--Rincian--")
print(f"Total pembelanjaan: {total_belanja}")

if persen == 0:
    print("Tidak ada diskon")
else:
    print(f"Diskon: {persen}%")

print(f"Nominal diskon: {nominal}")
print(f"Total bayar: Rp. {total_bayar}")