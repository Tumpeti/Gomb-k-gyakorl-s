from Gomba import Gomba
gombak_lista = []


def beolvasas():
    fajlom = open("gombak.txt", "r", encoding="utf-8")
    cimsor = fajlom.readline()
    print(cimsor)
    sorok = fajlom.readlines()
    fajlom.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        gombak_lista.append(Gomba(sor))
        print(gombak_lista[i])
        i += 1


def gombak_szama():
   return len(gombak_lista)