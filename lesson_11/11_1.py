class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok = rok_produkcji
    
    def informacje(self):
        return f'"{self.tytul.title()}" {self.rok}, reżyseria: {self.rezyser.title()}'

marvel = Film("Spider-Man", "sam raimi", 2002)
dc = Film("justice ligue", "zack snyder", 2017)

print(marvel.informacje())
print(dc.informacje())