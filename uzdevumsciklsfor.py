""" Uzdevuma nosacījumi
Izpildi VISUS uzdevumus vienā Python programmā.

🔹 1. uzdevums – skaitļi
Izmanto ciklu for, lai:

izvadītu visus skaitļus no 1 līdz 10

izvadītu tikai pāra skaitļus

📌 Padoms: izmanto range() un if nosacījumu.

🔹 2. uzdevums – teksts (string)
Dots teksts:

 
text = "Programmēšana"
 
 
Izmanto ciklu for, lai:

izvadītu katru burtu jaunā rindā

saskaitītu, cik burtu ir tekstā

📌 Padoms: izmanto skaitītāja mainīgo.

🔹 3. uzdevums – saraksts (list)
Dots saraksts:

 
numbers = [4, 7, 2, 9, 12]
 
 
Izmanto ciklu for, lai:

izvadītu katru skaitli

izvadītu tikai tos skaitļus, kas ir lielāki par 5

🔹 4. uzdevums – vārdnīca (dictionary)
Dots vārdnīcas objekts:

 
student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
 
 
Izmanto ciklu for, lai:

izvadītu katru atslēgu un tās vērtību šādā formātā:

 
vārds : Jānis
vecums : 17
kurss : Programmēšana I
 
 
"""

for i in range(10):#izvada no 1 lidz 10
    print("No viens lidz desmit:",i) 
for i in range(1, 11):# izvada tikai para skaitlus
    if i % 2  == 0:
        print("tikai para", i)
    

text = "Programmēšana"
count = 0

for letter in text:#izvada katru burtu atseviski
    print(letter)
for letter in text:#saskaita visus burtus
    print(letter)
    count += 1

print("Burtu skaits:", count)#izvada



numbers = [4, 7, 2, 9, 12]
for n in numbers:
    print("Visi skaitli", n)#izvada visus skaitlus
for n in numbers:
    if n > 5:
        print("Lelakie par ", n)#skaitlus lielakus par 5


student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
for key, value in student.items():#izvadītu katru atslēgu un tās vērtību šādā formātā:
    print(key, ":", value)

