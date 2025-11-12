"""
Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
ValueError , jeśli kwota jest ujemna.
Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
BrakSrodkowError , jeśli saldo jest niewystarczające.
Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

"""
from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass

@dataclass
class KontoBankowe:
    imie: str
    nazwisko: str
    _saldo: float

    try:
        @property
        def saldo(self):
            return(f"Saldo konta wynosi: {self._saldo}")
        
        def wplac(self, kwota):
            if kwota <= 0:
                raise ValueError("Wpłacana kwota nie może być ujemna")
            else:
                self._saldo += kwota
        
        def wyplac(self, kwota):
            if kwota <= 0:
                raise ValueError("Nie można wypłacić ujemnej kwoty")
            elif kwota > self._saldo:
                raise BrakSrodkowError("Za mało pieniędzy na koncie")
            else: 
                self._saldo -= kwota
    except Exception as e:
        print("nieznany błąd", e)        


try:
    user1 = KontoBankowe(100, "Dziubak", 500.77)
    print(user1.saldo)
    user1.wplac(100)
    print(user1.saldo)
    user1.wyplac("5")
    print(user1.saldo)
except Exception as e:
    print("nieznany blad")