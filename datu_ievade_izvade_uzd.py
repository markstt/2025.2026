#27/01/2026

"""Izveido Python programmu, kas:

Pajautā lietotājam:

vārdu (string)

vecumu (number)

trīs iecienītākās krāsas (list)

Saglabā datus vārdnīcā (dictionary)

Izvada visu informāciju vienā print() komandā

📌 Atļauts izmantot tikai:

input

print

string, number, list, dictionary"""
#vardu string
#vecumu number
#Lietotaja input()
vards = input("Ievadi savu vardu:")
vecums = int(input("Ievadi savu vecumu:"))
print("Tavs vards", vards, "tavs vecums:", vecums)

#trīs iecienītākās krāsas (list)
#Saglabā datus vārdnīcā (dictionary)
#Izvada visu informāciju vienā print() komandā
krasas = []
krasas.append(input("Ievadi savu pirmo iecienītāko krāsu:"))
krasas.append(input("Ievadi savu otro iecienītāko krāsu:"))  
krasas.append(input("Ievadi savu trešo iecienītāko krāsu:"))
print(krasas)