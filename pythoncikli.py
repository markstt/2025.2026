"""🔁 Kas ir cikls?
Cikls programmēšanā ļauj atkārtoti izpildīt koda bloku, kamēr ir spēkā noteikts nosacījums vai kamēr tiek apstrādāti visi dati.

Python valodā visbiežāk izmanto divus ciklus:

for – ja ir zināms, cik reižu vai pa kādiem elementiem jāatkārto darbība

while – ja cikls darbojas, kamēr nosacījums ir patiess (True)"""


#🔹 Cikls for
#Cikls for tiek izmantots, lai izietu cauri secīgai datu kopai (piemēram, skaitļu virknei, tekstam, sarakstam vai vārdnīcai).
#📌 for ar skaitļiem (number)
for i in range(5): #izvada no 1 lidz 4
    print(i)

#📌 for ar tekstu (string)
text = "Python"

for letter in text:
    print(letter)#katrs burts atseviški

#📌 for ar sarakstu (list)
numbers = [3, 7, 2, 9]

for n in numbers:
    print(n * 2)#katrs saeakstsa elements izmnatots apreikonos

#
#📌 for ar vārdnīcu (dictionary)
student = {
    "vārds": "Anna",
    "vecums": 16,
    "kurss": "Programmēšana"
}

for key, value in student.items():
    print(key, ":", value)#izvada visus atslēgu–vērtību pārus

#🔹 Cikls while
#Cikls while darbojas tik ilgi, kamēr nosacījums ir patiess.
#📌 while ar skaitītāju (number)
count = 0

while count < 5:
    print(count)
    count += 1#izvada no 0 lidz 4
#⚠️ Svarīgi!
#Ja mainīgais netiek mainīts, cikls var kļūt bezgalīgs.
# NEPAREIZI – bezgalīgs cikls
#while True:
    #print("Cikls darbojas")
#📌 while ar nosacījumu
number = 10

while number > 0:
    print(number)
    number -= 1#skaitli iet uz leju
#🔸 break un continue
#📌 break – pārtrauc ciklu
for i in range(10):
    if i == 5:
        break
    print(i)#cikls beidzas pie 5
#📌 continue – izlaiž vienu atkārtojumu
for i in range(5):
    if i == 2:
        continue
    print(i)#skaitlis 2 neizvadas
"""✅ Kopsavilkums
for – izmanto, ja strādā ar secīgām vērtībām (range, list, string, dictionary)

while – izmanto, ja cikls atkarīgs no nosacījuma

Nosacījumi (if) ļauj kontrolēt cikla darbību

break pārtrauc ciklu, continue izlaiž vienu atkārtojumu"""