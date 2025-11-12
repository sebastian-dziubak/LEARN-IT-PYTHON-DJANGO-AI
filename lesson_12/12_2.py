"""
Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
zmieniać wartości.

"""

class Uzytkownik:
    def __init__(self, name, wiek):
        self.name = name
        self._wiek = wiek
    
    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self, nowy_wiek):
        if 0 <= nowy_wiek <= 120:
            self._wiek = nowy_wiek
        else:
            print("Wiek nie mieści się w zakresie")
    
user1 = Uzytkownik("Seba", 38)
print(user1.wiek)

user1.wiek = 110
print(user1.wiek)

user1.wiek = 150
print(user1.wiek)

