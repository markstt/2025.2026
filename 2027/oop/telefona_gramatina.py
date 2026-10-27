#27.10.2026

class Kontakts:
    def __init__(self, vards, uzvards, talrunis,epasts):
        self.vards = vards
        self.uzvards = uzvards
        self.talruins = talrunis
        self.epasts = epasts
kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456", "janiisberzins@gmail.com");

print( kontakts1.vards)

print("Kontakts1, pirms izmainam:",kontakts1.uzvards)
kontakts1.uzvards = "Kalniņš"
print(kontakts1.uzvards)
print(kontakts1.talruins)
print(kontakts1.epasts)
kontakts1.epasts = "janiskalnins@gmail.com"
kontakts2 = Kontakts("Anna", "Kalniņa", "29876543", "anna.kalnina@gmail.com")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talruins)
print(kontakts2.epasts)
print("Kontakts1:", kontakts1.uzvards)
print(kontakts1.epasts)