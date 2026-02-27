from tabulate import tabulate
from konverter import konversi
from kurs import kurs

def display():
    print("=== KONVERTER MATA UANG ===")

    tabel = []
    for kode, nilai in kurs.items():
        tabel.append([kode, f"{nilai:,.2f}".replace(",", ".")])

    print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    display()

    currency = ["IDR"] + list(kurs.keys())

    ori = input("Dari (IDR/USD/JPY/EUR/CNY/CAD): ").upper()
    to = input("Ke (IDR/USD/JPY/EUR/CNY/CAD): ").upper()

    if ori not in currency or to not in currency:
        print("Not a currency that exists or wrong currency code!")
        return
    
    try:
        amount = float(input("Jumlah: "))
    except ValueError:
        print("Input jumlah harus numerik!")
        return
    
    result = konversi(ori, to, amount)
    
    if ori == "IDR":
        print(f"\nRp {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    elif ori == "USD":
        print(f"\n$ {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    elif ori == "JPY":
        print(f"\n¥ {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    elif ori == "EUR":
        print(f"\n€ {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    elif ori == "CNY":
        print(f"\nCN¥ {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    elif ori == "CAD":
        print(f"\nCA$ {amount:,.0f} {ori} = {result:,.2f} {to}".replace(",", "."))
    

if __name__ == "__main__":
    main()