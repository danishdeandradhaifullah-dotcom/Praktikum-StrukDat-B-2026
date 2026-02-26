class GreekGod():
    def __init__(self, name, power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon

    def power_line(self):
        print(f"Feel the wrath of {self.power}")

    def name_callout(self):
        print(f"Hello my name is {self.name}")

g1 = GreekGod("Zeus", "Lightning", "Lightning Bolt")
g2 = GreekGod("Poseidon", "Water", "Trident")
g3 = GreekGod("Hades", "Fire", "Helmet")

g1.name_callout()
g1.power_line()

print(g1.name)
print(g2.weapon)
print(g3.power)

g3.power = "Earth"
print(g3.power)