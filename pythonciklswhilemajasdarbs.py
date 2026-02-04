"""📝 Uzdevuma nosacījumi
Izpildi VISUS uzdevumus vienā Python programmā.

🔹 1. uzdevums – skaitītājs (number)
Izmanto ciklu while, lai:

izvadītu skaitļus no 1 līdz 10

📌 Padoms: izmanto skaitītāja mainīgo.

🔹 2. uzdevums – pāra skaitļi
Izmanto ciklu while, lai:

izvadītu tikai pāra skaitļus no 1 līdz 20

📌 Padoms: izmanto if nosacījumu.

🔹 3. uzdevums – teksts (string)
Dots teksts:

 
text = "Python"
 
 
Izmanto ciklu while, lai:

izvadītu katru burtu atsevišķā rindā

📌 Padoms: izmanto indeksu (i).

🔹 4. uzdevums – saraksts (list)
Dots saraksts:

 
numbers = [3, 6, 1, 8, 4]
 
 
Izmanto ciklu while, lai:

izvadītu visus saraksta elementus

saskaitītu un izvadītu visu skaitļu summu"""

number = 1
while number <= 10:#izvada skailus no viens lidz 10
    print(number)
    number += 1


number = 1
while number <= 20:
    if number % 2 == 0:
        print("Tika para skaitli", number)#izvada tikai paru skaitlus
    number += 1
text = "Python"
i = 0

while i < len(text):#izvada katru burtu atseviski
    print(text[i])
    i += 1


