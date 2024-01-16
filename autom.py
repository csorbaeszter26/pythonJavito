import Autom_O

def beolvas():
    kocsi = []
    beFile = open("auto.txt", "r", encoding="utf-8")
    beFile.readline()
    szoveg = beFile.readlines()
    for index in range(0, len(szoveg), 1):
        tisztaSzoveg = szoveg[index].strip().split("$")
        peldany = Autom_O.Autom_O(tisztaSzoveg[0], tisztaSzoveg[1])
        kocsi.append(peldany)
    # print(lista)
    beFile.close()
    return kocsi

def tabla(kocsi):
    hossz = 0
    lista = len(kocsi)
    for index in range(0, len(kocsi), 1):

        hossz += 1
    print("III/Tábla")
    print(f"\t{kocsi[0]}: {hossz} hosszú.")
    return hossz

def kiiras(hossz):
    kiFile = open("kiir.txt", "w", encoding="utf-8")
    print(f"Skoda Fabia: {hossz} hosszú.", file=kiFile)



def flotta(kocsi):
    print("III/Flotta")
    print(f"\tAutók száma: {len(kocsi)}")


def ertekes(kocsi):
    print("III/Értékes")
    minimum = 2020
    for index in range(1, len(kocsi), 1):
        if kocsi[index].datum < kocsi[index].datum:
            minimum = index
    print(f"\tA legfiatalabb autó: {kocsi[minimum].nev}({kocsi[minimum].datum})")
    return minimum



def harmadik():
    kocsi = beolvas()
    hossz = tabla(kocsi)
    minimum = ertekes(kocsi)
    ertekes(minimum)


    tabla(kocsi)
    kiiras(hossz)
    flotta(kocsi)


