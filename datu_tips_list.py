#22/01/2026



#List - saraksts




#Teksts, vesels skaitlis, decimalskaitlis,
saraksts = ["Anna", 5, 4.2, [1, 2, 3]]

""""✍️ Praktiskais uzdevums
Izveido sarakstu ar vismaz 5 elementiem
Izvadi pirmo un pēdējo elementu
Pievieno jaunu elementu
Nomaini vienu esošu elementu
Izvadi rezultātu pēc katras darbības"""


masinas = ["Audi", "BMW", "Opel", "Toyota", "Honda"]
print(masinas)
#Izvadi pirmo un pēdējo elementu
#indeksešna
print(masinas[0])
print(masinas[-1])

#Pievieno jaunu elementu
#.append() - metode, lai pievienotu elementu saraksta beigās
masinas.append("Ford")
print(masinas)
#Nomaini vienu esošu elementu
masinas[2] = "Nissan"
print(masinas)