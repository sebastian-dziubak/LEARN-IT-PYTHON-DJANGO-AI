"""
Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
(domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
metody do zarządzania telewizorem:
wlacz() i wylacz()
zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
jest włączony.
info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
100.

"""

class Telewizor:
    def __init__(self, kanal=1, glosnosc=10, wlaczony=False):
        self.__kanal = kanal
        self.__glosnosc = glosnosc
        self.__wlaczony = wlaczony
    
    def wlacz(self):
        if self.__wlaczony == False:
            self.__wlaczony = True
    
    def wylacz(self):
        if self.__wlaczony == True:
            self.__wlaczony = False
    
    def zmien_kanal(self, numer):
        if self.__wlaczony == True:
            self.__kanal = numer

    def glosniej(self):
        if self.__wlaczony == True and 0 <= self.__glosnosc <= 100:    
            self.__glosnosc += 1

    def ciszej(self):
        if self.__wlaczony == True and 0 <= self.__glosnosc <= 100:  
            self.__glosnosc -= 1

    def info(self):
        info = {
            "Telewizor włączony: ": self.__wlaczony,
            "Kanał: ": self.__kanal,
            "Głośność ": self.__glosnosc
        }
        print("Stan telewizora:")
        for key, value in info.items():
            print(key, value)

samsung = Telewizor()
