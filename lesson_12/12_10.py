"""
Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
niepoprawnie udokumentowanymi metodami.

"""

class MetaWalidujMetody:
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if not key.startswith("__"):
                if not value.__doc__:
                    raise TypeError(f"Metoda {key} wymaga docstringa")
        return super().__new__(cls, name, bases, dct)

try:
    class Poprawna(metaclass=MetaWalidujMetody):
        def metoda_a(self):
            "docstring"
            return "metoda_a"
except TypeError as e:
    print("Error", e)

try:
    class Niepoprawna(metaclass=MetaWalidujMetody):
        def metoda_b(self):
            return "metoda_b"
except TypeError as e:
    print("Error", e)