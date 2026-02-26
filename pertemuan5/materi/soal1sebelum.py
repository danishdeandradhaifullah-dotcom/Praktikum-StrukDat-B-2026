angka = [10, 20, 30, 40, 50]
angka.append(60)
angka.remove(20)
print(f"Angka paling tinggi = {max(angka)} " )
print(f"Angka paling rendah = {min(angka)}")
rataRata = sum(angka) / len(angka)
print(rataRata)

print(angka) # list setelah perubahan