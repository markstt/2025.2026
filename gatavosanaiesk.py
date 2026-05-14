"""1. uzdevums — Datu kvalitāte (6 p)
1.1. Nosaki, kuri dati ir kvalitatīvi. Pamato. (4 p)
Laura,17,Rīga
???,-15,Mēness
Jānis,18
1.2. Pārveido dotos nestrukturētos datus strukturētā tabulā. (2 p)
“Marta dzīvo Jelgavā un viņai ir 16 gadi.”

2. uzdevums — Datu validācija (8 p)
2.1. Uzraksti programmu, kas pārbauda, vai ievadītais skaitlis ir robežās no 1 līdz 10. (5 p)
2.2. Paskaidro, kāpēc validācija ir svarīga programmās. (3 p)
3. uzdevums — Datu apstrāde CSV failā (10 p)
Dota datne:

 
produkts,cena
Piens,1.50
Maize,2.00
Sula,3.20
Cepumi,4.50
 
 
3.1. Uzraksti programmu, kas izvada tikai produktus, kuru cena ir lielāka par 2.00. (5 p)
3.2. Aprēķini visu produktu kopējo summu. (5 p)
4. uzdevums — Kārtošana (8 p)
4.1. Sakārto sarakstu dilstošā secībā. (3 p)
 
scores = [7, 10, 5, 8, 9]
 
 
4.2. Paskaidro, kur dzīvē izmanto datu kārtošanu. Min vienu piemēru. (2 p)
4.3. Uzraksti programmu, kas izvada 2 lielākos skaitļus sarakstā. (3 p)
5. uzdevums — Meklēšana (8 p)
5.1. Uzraksti programmu, kas pārbauda, vai skaitlis 15 atrodas sarakstā. (3 p)
 
numbers = [5, 12, 15, 20]
 
 
5.2. Paskaidro, kāpēc meklēšana lielās sistēmās var būt lēnāka. (2 p)
5.3. Uzraksti programmu, kas CSV failā atrod produktu “Sula”. (3 p)"""
#1.uzd
""""1. uzdevums — Datu kvalitāte (6 p)
1.1. Nosaki, kuri dati ir kvalitatīvi. Pamato. (4 p)
Laura,17,Rīga
???,-15,Mēness
Jānis,18
1.2. Pārveido dotos nestrukturētos datus strukturētā tabulā. (2 p)
“Marta dzīvo Jelgavā un viņai ir 16 gadi.”"""
#1. ir kvalitativs jo ir vardas,vecums
#2.Jānis,18 un šis ir kvalitativs jo ir vards valids vecums
#1.2 Marta,16,Jelgavā
"""2. uzdevums — Datu validācija (8 p)
2.1. Uzraksti programmu, kas pārbauda, vai ievadītais skaitlis ir robežās no 1 līdz 10. (5 p)
2.2. Paskaidro, kāpēc validācija ir svarīga programmās. (3 p)
3. uzdevums — Datu apstrāde CSV failā (10 p)
Dota datne:"""
#skaitlis = int(input("ievadi skaitli no 1 lidz 10: "))
#if skaitlis in range(1,11):
   # print("ir robežās no 1 līdz 10.")
#else:
  #  print("Nav robežas")

"""3. uzdevums — Datu apstrāde CSV failā (10 p)
Dota datne:

 
produkts,cena
Piens,1.50
Maize,2.00
Sula,3.20
Cepumi,4.50
 
 
3.1. Uzraksti programmu, kas izvada tikai produktus, kuru cena ir lielāka par 2.00. (5 p)
3.2. Aprēķini visu produktu kopējo summu. (5 p)
4. uzdevums — Kārtošana (8 p)
4.1. Sakārto sarakstu dilstošā secībā. (3 p)
 
scores = [7, 10, 5, 8, 9]
 
 
4.2. Paskaidro, kur dzīvē izmanto datu kārtošanu. Min vienu piemēru. (2 p)
4.3. Uzraksti programmu, kas izvada 2 lielākos skaitļus sarakstā. (3 p)"""
#cenas = 0 #saraksts kur tiks saglabati atzimes no faila
#with open("produkti.csv", encoding="utf-8") as f:
   # next(f)

    #for rinda in f:
       # produkts,cena = rinda.strip().split(",")
        #cenas.append(float(cena)) #.append() - metode
#cenas.sort()
#print(cenas)

scores = [7, 10, 5, 8, 9]
#4.1
scores.sort(reverse=True) # metode .sort reverse sakarto dilstosa seciba
print(scores)
#4.2
#4.3

