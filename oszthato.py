import random

def ottel_oszthato():
    szamok = []
    for index in range(0, 50, 1):
        vszam = random.randint(1, 100)
        szamok.append(vszam)
    print("A lista elemei:")
    print("\t", szamok)

    db= 0
    for index in range(0, len(szamok), 1):
        if szamok[index]%5==0:
            db += 1
    print(f"A listában  {db}  darab öttel osztható szám van.")



def masodik():
    lista = ottel_oszthato()
