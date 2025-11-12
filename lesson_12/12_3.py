"""
Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.

"""

class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(pln):
        USD = 4.0
        result = pln / USD
        return f"{pln} PLN = {result} USD (przy kursie 1 USD = {USD} PLN)"

print(KalkulatorWalut.usd_na_pln(40))