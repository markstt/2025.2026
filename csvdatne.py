
#29.04.2026
#CSV datnes atvēršana, nolasīšana un datu apstrāde
#encoding="utf-8" - ļauj apstrādāt garumzīmes un mīkstinājuma zīmes
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails
    print(fails) #Izvada faila informāciju, bet nevar redzēt faila saturu
#Faila satura izvadīšana
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails
    for rinda in fails:
        print(rinda) #Izvada informāciju, iekļaujot tab
   
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails    
    for rinda in fails:    
        print(rinda.strip()) #Izvada informāciju, noņemot atstarpes as metodi .strip()
#Izlaižam kolonnu nosaukumus jeb pirmo faila rindu
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:    
        print(rinda.strip()) #Izvada informāciju, noņemot atstarpes
   
#Datu sadalīšana kolonnās
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        print(vards,uzvards,pilseta) #Izvada informāciju
#Tikai vārdu izvadīšana
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        print(vards) #Izvada tikai vārdu
#Datu apstrādāšana - izvada tikai personas, kas dzīvo Rīgā
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        if pilseta == "Rīga": #Pārbaude, vai pilsēta ir Rīga
            print(vards) #Izvada personas vārdu, kas dzīvo Rīgā
