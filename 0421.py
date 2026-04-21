class Auto:
    def __init__(self, tipus, szin, ar):
        self.tipus = tipus
        self.szin = szin
        self.ar = ar

autok = []

for i in range(3):
    print(i+1, ". autó adatai:")
    tipus = input("Típus: ")
    szin = input("Szín: ")
    ar = int(input("Ár: "))
    
    auto = Auto(tipus, szin, ar)
    autok.append(auto)


legdragabb = autok[0]

for auto in autok:
    if auto.ar > legdragabb.ar:
        legdragabb = auto

f = open("draga.txt", "w", encoding="utf-8")
f.write(legdragabb.tipus + " típusú " + legdragabb.szin + " színű autó a legdrágább: " + str(legdragabb.ar) + " Ft")
f.close()


keresett_szin = input("\nAdj meg egy színt: ")
van = False

for auto in autok:
    if auto.szin.lower() == keresett_szin.lower():
        print(auto.tipus, auto.szin, auto.ar)
        van = True

if not van:
    print("Nincs ilyen színű autó.")


osszeg = 0

for auto in autok:
    osszeg += auto.ar

print("Az autók összértéke:", osszeg, "Ft")