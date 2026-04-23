#23.04.2026

#Datu validacija 

#Datu ievade

vecums = input("Ievadi vecumu: ")
if vecums.isdigit():   #.isdigit() metode parbauda vai saņemtaijs lielumus ir skaitlis vai nav metode atgriez True or False
    print("Ir skaitlis")
    if int(vecums) >= 18:
        print("Tu esi pilngadigs.")
    else:
        print("Tu vel ne sasniedzi 18.")
else:
    print("Nav skaitlis")

print(vecums)