"""
Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
super().graj().
Instrument.graj() -> "Wydaje dźwięk."
Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]"

"""

class Instrument:
    def graj(self):
        return "Instrument wydaje dźwięk."

class Strunowy(Instrument):
    def graj(self):
        return super().graj() + "[instrument strunowy]"

class Dety(Instrument):
    def graj(self):
        return super().graj() + "[instrument dęty]"
    
class Gitara(Strunowy):
    def graj(self):
        return super().graj() + "[granie gitary]"

class Trabka(Dety):
     def graj(self):
        return super().graj() + "[granie trąbki]"


instrument = Instrument()
strunowy = Strunowy()
dety = Dety()
gitara = Gitara()
trabka = Trabka()

print(instrument.graj())
print(strunowy.graj())
print(dety.graj())
print(gitara.graj())
print(trabka.graj())
