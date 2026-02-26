class MyCar: # for the naming of classes you usually use pascal case
    def __init__(self, brand, colour, year):
        self.brand = brand
        self.colour = colour
        self.year = year

p1 = MyCar("Tesla", "Grey", "2018")

print(p1.brand)
