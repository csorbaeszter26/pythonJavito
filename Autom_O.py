class Autom_O:
    def __init__(self, nev, datum):
        self.nev = nev
        self.datum = int(datum)

    def __str__(self):
        return f"A kocsi neve: {self.nev}, a kocsi gyártási dátuma: {self.datum}."
