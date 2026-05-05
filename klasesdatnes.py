#05.05.2026

with open("vardi.txt", "w", encoding="utf-8") as f:
    f.write("Karlis\n")
    f.write("Jānis\n")
    f.write("Andrejs")
with open("klase.csv", "w", encoding="utf-8") as f:
    f.write("vards,atzime\n")
    f.write("Jānis, 7\n")
    f.write("Marks, 8\n")
    f.write("Andrejs, 10")
with open("klase.csv", "a", encoding="utf-8") as f:
    f.write("\nKārlis, 6")

vards=input("Ievadi vardu: ")
vecums=input("Ievadi vecumu: ")
with open("cilveki.csv", "w", encoding="utf-8") as f:
    f.write("vards,vecums\n")
    f.write(vards + ",")
    f.write(vecums)