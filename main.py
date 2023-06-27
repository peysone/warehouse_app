from pprint import pprint
"""Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
konto - Program wyświetla stan konta.
lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
koniec - Aplikacja kończy działanie."""


account = 0
warehouse = {}

while True:
    print("\nDostępne komendy:\n")
    print("saldo\n"
          "sprzedaż\n"
          "zakup\n"
          "konto\n"
          "lista\n"
          "magazyn\n"
          "przegląd\n"
          "koniec")

    command = input("Wprowadź komendę: ")

    #operacja dodawania kwoty do salda
    if command == "saldo":
        sum = float(input("Wprowadź kwotę: "))
        account += sum
        action = print(f"Dodano {sum} do konta")



    if command == "sprzedaż":
        name = input("Wprowadź nazwę produktu: ")

        if name in warehouse:
            price = float(input("Wprowadź cenę: "))
            quantity = int(input("Wprowadź liczbę sztuk: "))
#logika sprzedazy produktow, odjecie ze stanu magazaynu liczby towarów oraz kwoty od stanu konta
            if warehouse[name] >= quantity:
                warehouse[name] -= quantity
                sum = price * quantity
                account += sum
                action = print(f"Sprzedano {quantity} sztuk produktu '{name}' za {sum} zł")
            else:
                print("Nie wystarczająca ilość produktu w magazynie")
        if name not in warehouse:
            print("Produkt nie istnieje w magazynie")


    if command == "zakup":
        name = input("Wprowadź nazwę produktu: ")
        price = float(input("Wprowadź cenę: "))
        quantity = int(input("Wprowadź liczbę sztuk: "))
#logika działania zakupu towaru, dodanie go do stanu magazynu oraz odjecie kwoty od stanu konta
        if account >= price * quantity:
            account -= price * quantity

            if name in warehouse:
                warehouse[name] += quantity

            action = print(f"Zakupiono {quantity} sztuk produktu '{name}' za {price * quantity} zł")
        else:
            print("Brak wystarczających środków na koncie")