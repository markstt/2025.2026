"""Izveido programmu, kas:

prasa 3 produktu nosaukumus
saglabā failā produkti.txt
Katru jaunā rindā.

Pēc darba pabeigšanas, nosūti to uz GitHub."""


produkts = input("Ievadi produkta nosaukumu: ")
produkts1 = input("Ievadi produkta nosaukumu: ")
produkts2 = input("Ievadi produkta nosaukumu: ")
with open("produkti.txt", "w", encoding="utf-8") as file:
        file.write(produkts + "\n")
        file.write(produkts1 + "\n")
        file.write(produkts2 + "\n")
