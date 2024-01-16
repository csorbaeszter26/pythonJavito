def elso():
    helyesNev = "bori99"
    helyesJelszo = "Szivecske<3"

    nev = input("Adja meg a felhasználónevét!")
    jelszo = input("Adja meg a jelszavát!")

    if nev == helyesNev and jelszo == helyesJelszo:
        print("Belépés engedélyezve.")
    else:
        while nev != helyesNev and jelszo != helyesJelszo:
            print("Belépés megtagadva.")
            nev = input("Adja meg a felhasználónevét!")
            jelszo = input("Adja meg a jelszavát!")
            if nev == helyesNev and jelszo == helyesJelszo:
                print("Belépés engedélyezve.")




