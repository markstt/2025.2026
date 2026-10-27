#27/10/2026
#OOP pamatprincipi
#Objekts
#Objekta ipašības
#Klase, kura ir objekta veidne(template)
#Objekts - mašina
#Ipašības - marka, modelis, krāsa

class Masina:#Objekta nosaukums vienmer ar lielo burtu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Izvedeojam funkciju kura self nozime ka tas ir objekts, kuram pieder šīs īpašības
    def __init__(self, marka, modelis, krasa):#Ipašību definēšana
        self.marka = marka
        self.modelis = modelis
        self.krasa = krasa
        #Ipasiba ar noklusēto vērtību
        self.atrums = 0
#Pirma objekta izveide
mansAuto = Masina("Audi", "R6", "melna")
print(mansAuto.marka)
print(mansAuto.modelis)
print(mansAuto.krasa)
print(mansAuto.atrums)

mansAuto.atrums = 50
print(mansAuto.atrums)

tavs = Masina("VOLVO", "V40", "zala")
print(tavs.marka)
print(tavs.modelis)
print(tavs.krasa)
print(tavs.atrums)
tavs.atrums = 75
print("Tāvs atrums:", tavs.atrums)