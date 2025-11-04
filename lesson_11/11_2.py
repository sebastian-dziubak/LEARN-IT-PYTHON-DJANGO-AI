"""
Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

"""

class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria

produkt1 = Produkt("iphone 12", 3799, "elektronika")

print(f"nazwa: {produkt1.nazwa.title()}")
print(f"cena: {produkt1.cena} PLN")
print(f"kategoria: {produkt1.kategoria}")