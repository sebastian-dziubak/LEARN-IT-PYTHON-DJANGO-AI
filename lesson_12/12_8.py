"""
Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
Całość umieść w pętli while True , aby program działał do momentu przerwania.
Użyj bloku try...except do obsługi:
ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
ZeroDivisionError przy próbie dzielenia przez zero.
Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
obliczeń."

"""

class Calculator:
    @staticmethod
    def plus(x, y):
        return x + y
    def minus(x, y):
        return x - y
    def multi(x, y):
        return x * y
    def div(x, y):
        return x / y

print("** Calculator **\n")
while True:
    try:
        numner1 = float(input("Podaj pierwszą liczbę: "))
        numner2 = float(input("Podaj drugą liczbę: "))
        action = input('Podaj symbol operacji ("+", "-", "*", "/"): ')
        if action == "+":
            result = Calculator.plus(numner1, numner2)
        elif action == "-":
            result = Calculator.minus(numner1, numner2)
        elif action == "*":
            result = Calculator.multi(numner1, numner2)
        elif action == "/":
            result = Calculator.div(numner1, numner2)
    except ValueError:
        print("Nie podano liczby. Spróbuj jeszcze raz...")  
    except ZeroDivisionError:
        print("Nie można dzielić przez zero. Spróbuj jeszcze raz")
    else:
        print(f"Wynik obliczeń: {numner1} {action} {numner2} = {result:.2f}")
    finally:
        print("Koniec obliczeń")
        exit = input('Naciśnij "x" aby wyjść... ')
        if exit.lower() == "x":
            break

        