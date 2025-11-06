"""
Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
Zadania z gwiazdką (challenge)
przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
pętli wydrukuj pole każdej figury.

"""

class Figura:
    def __init__(self):
        pass
    def oblicz_pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self):
        super().__init__(self)
    def oblicz_pole(bok):
        return bok ** 2

class Kolo(Figura):
    def __init__(self):
        super().__init__(self)
    def oblicz_pole(promien):
        PI = 3.14159
        return PI * promien ** 2

kwadrat1 = Kwadrat
kolo1 = Kolo

figures = [kwadrat1, kolo1]
for figure in figures:
    print(f"{figure.oblicz_pole(5):.2f}")