#05/05/2026

#datu saglabašana datne

#saglabasim datus teksta faila

with open("primais_fails.txt", "w", encoding="utf-8") as f:#w -write mode jeb rakstišanas/izveidošanas
    f.write("Sveiki Pasaule!")#.write() metode - ieraksta nora'dita teksta failu

#vairaku rindu saglabašana
with open("primais_fails.txt", "w", encoding="utf-8") as f:#w -write mode jeb rakstišanas/izveidošanas
    f.write("Anna\n")#\n - pēc teksta parnes kursoru jauna rinda
    f.write("Pēteris!")#.write() metode - ieraksta nora'dita teksta failu    

#datu saglabašana csv faila
with open("primais_fails.csv", "w", encoding="utf-8") as f:
    f.write("vards,uzvards,vecums,skola\n")
    f.write("Anna,Bērziņa,17,Rīgas Valsts 1.ģimnazija\n")
#datu piveinošana csv faila
with open("primais_fails.csv", "a", encoding="utf-8") as f:
    f.write("Jānis,Ozoliņš,15, Rēzeknes Valsts 1.ģimnāzija")