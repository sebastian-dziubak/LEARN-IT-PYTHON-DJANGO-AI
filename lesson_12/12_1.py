"""
Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.

"""

from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int


film1 = Film("Avengers Infinity War", "Russo Brothers", 2018)
film2 = Film("Sucker Punch", "Zack Snyder", 2011)

print(film1)
print(film2)