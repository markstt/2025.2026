#27.10.2026

class Kontakts:
    def __init__(self, vards, uzvards, talrunis):
        self.vards = vards
        self.uzvards = uzvards
        self.talruins = talrunis
kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456");

print( kontakts1.vards)

print("Kontakts1, pirms izmainam:",kontakts1.uzvards)
kontakts1.uzvards = "Kalniņš"
print(kontakts1.uzvards)
print(kontakts1.talruins)

kontakts2 = Kontakts("Anna", "Kalniņa", "29876543")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talruins)
print("Kontakts1:", kontakts1.uzvards)