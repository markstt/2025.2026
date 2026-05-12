#12/05/2026
#kartosanas algoritmi
#.sort() - metode
#sorted() - funkcija
#1. skaitlu kartosana

skaitli = [5,9,3,20,2]
skaitli.sort() # sakarto skaitlus augoša seciba
print(skaitli)

#2.skaitlu sakartošana dilstosa
skaitli = [5,9,3,20,2]
skaitli.sort(reverse=True) # metode .sort reverse sakarto dilstosa seciba
print(skaitli)

#3.vardu kartošana

vardi = ["Janis","Anna","Zigrids"]
vardi.sort()#sakarto alfabetiska seciba
print(vardi)

#4. Kartošana no csv faila
atzimes = [] #saraksts kur tiks saglabati atzimes no faila
with open("klase.csv", encoding="utf-8") as f:
    next(f)

    for rinda in f:
        vards,atzime = rinda.strip().split(",")
        atzimes.append(int(atzime)) #.append() - metode
atzimes.sort()
print(atzimes)