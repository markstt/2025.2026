#12.05.2026

#meklsenas algoritmi

#kur tie atrodas
#vai teksra ir kada noteikta dala
#in -kur ieksa
#ciklus (for)
#nosacijums (if)
#meklesanas saraksats

vardi = ["Janis","Anna","Zigrids"]
if "Anna" in vardi: #nosacijums varda meklešana
    print("ir")
else:
    print("nav atrast")

#meklesana ar lietotaja ievadi

vardi = ["Janis","Anna","Zigrids"]
meklet = input("Ievadi kadu vardu meklet: ")
if meklet in vardi: #nosacijums varda meklešana
    print("ir")
else:
    print("nav atrast")

#3.meklešana csv
meklet = input("Ievadi kadu vardu meklet: ")
atrasts = False
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for rinda in f:
        vards,atzime = rinda.strip().split(",")
        if vards == meklet:
            print("ir atrasts")
        atrasts = True

if not atrasts:
    print("nav atrast")

#daleji
teksts = "Programešana"
if "gramm" in teksts:
    print("atrasts")
else:
    print("nav atrast")