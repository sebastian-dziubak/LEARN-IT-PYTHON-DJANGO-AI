"""
Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

"""

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
        print (f"dzień: {self.dzien}, miesiąc: {self.miesiac}, rok: {self.rok}")

    @classmethod
    def ze_stringa(cls, data: str):
        data_split = data.split("-")
        dzien = int(data_split[0])
        miesiac = int(data_split[1])
        rok = int(data_split[2])
        return cls(dzien, miesiac, rok)

data1 = Data(6, 6, 1988)
data2 = Data.ze_stringa("10-10-2022")
