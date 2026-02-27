from kurs import kurs

def konversi(ori, to, amount ):
    if ori == "IDR":
        return amount / kurs[to]
    elif to == "IDR":
        return amount * kurs[ori]
    else:
        to_idr = amount * kurs[ori]
        return to_idr / kurs[to]
