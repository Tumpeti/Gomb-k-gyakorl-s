"""
Első idős ember korának helye a listában:
"""

korok_lista = []

def bekeres():
    i = 0
    while i < 5:
        kor = int(input("Kérek egy egész számot 0 és 120 között!"))
        korok_lista.append(kor)
        i += 1


def kiiras ():
    i = 0
    korok_kiirva = ""
    while i < len(korok_lista) - 1:
        korok_kiirva += str(korok_lista[i]) + " : "
        i += 1
    korok_kiirva += str(korok_lista[-1])
    return korok_kiirva


def elso_idos():
    i = 0
    idos = -1
    while i < len(korok_lista) and idos == -1:
        if korok_lista[i] > 70:
            idos = i
        i += 1
    return idos


def konzolra_ir():
    print(f"II/D, E:\nElső idős ember korának helye a listában: {elso_idos()}.")


def fajl_ir():
    f = open("oreg.txt", "w", encoding="utf-8")
    f.write(f"Első idős ember korának indexe: {elso_idos()}")
    f.close()
