"""
Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
__add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
sobie współrzędne).
__sub__(self, other) : do odejmowania wektorów.
eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
dwa wektory i wykonując na nich wszystkie zaimplementowane operacje.

"""

class Wektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x - other.x, self.y - other.y)
        
    def __eq__(self, other):
        if isinstance(other, Wektor2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented
       
    def __str__(self):
        return f"({self.x}, {self.y})"
    

wektor1 = Wektor2D(5,-5)
wektor2 = Wektor2D(6, 8)
wektor3 = Wektor2D(6, 8)

print(f"suma wektorów {wektor1} i {wektor2} = {wektor1 + wektor2}")
print(f"różnica wektorów {wektor1} i {wektor2} = {wektor1 - wektor2}")
print(f"Czy wektor {wektor1} jest równy {wektor2}?:", wektor1 == wektor2)
print(f"Czy wektor {wektor2} jest równy {wektor3}?:", wektor2 == wektor3)




