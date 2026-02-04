angka = [10, 20, 30, 40, 50]
angka.append(60)
angka.remove(20)
max = angka[0]
min = angka[0]
for x in range(len(angka)):
    if angka[x] > max:
        max = angka[x]
    if angka[x] < min:
        min = angka[x]
print(f"Angka paling tinggi = {max} " )
print(f"Angka paling rendah = {min}")
print(angka) # list setelah perubahan