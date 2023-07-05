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

"""
Saldo konta oraz magazyn mają zostać zapisane do pliku tekstowego, 
a przy kolejnym uruchomieniu programu ma zostać odczytany. 
Zapisać należy również historię operacji (przegląd), 
która powinna być rozszerzana przy każdym kolejnym uruchomieniu programu."""
import json


def save_account(account):
    with open('saldo.txt', 'wb') as file:
        json.dump(account, file)


def save_warehouse(warehouse):
    with open('magazyn.txt', 'wb') as file:
        json.dump(warehouse, file)


def load_account():
    try:
        with open('saldo.txt', 'rb') as file:
            return json.load(file)
    except FileNotFoundError:
        return 0


def load_warehouse():
    try:
        with open('magazyn.txt', 'rb') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


account = load_account()
warehouse = load_warehouse()
prices = {}
history = []



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

    # operacja dodawania kwoty do salda i sprawdzanie czy saldo nie jest ujemne
    if command == "saldo":
        amount = float(input("Wprowadź kwotę: "))
        if account + amount < 0:
            action = print("Nie można mieć ujemnego salda!")
            history.append(action)
            print(action)
        else:
            account += amount
            action = print(f"Dodano {amount} do konta")
            history.append(action)
            save_account(account)

    elif command == "sprzedaż":
        name = input("Wprowadź nazwę produktu: ")
        if name in warehouse:
            price = prices[name]
            quantity = int(input("Wprowadź liczbę sztuk: "))
            if warehouse[name] >= quantity:
                warehouse[name] -= quantity
                total_price = price * quantity
                account += total_price
                action = f"Sprzedano {quantity} sztuk produktu '{name}' za {total_price} zł"
                history.append(action)
            else:
                action = print("Nie wystarczająca ilość produktu w magazynie")
                history.append(action)
        else:
            action = print("Produkt nie istnieje w magazynie")
            history.append(action)

    elif command == "zakup":
        name = input("Wprowadź nazwę produktu: ")
        price = float(input("Wprowadź cenę: "))
        quantity = int(input("Wprowadź liczbę sztuk: "))

        if account >= price * quantity:
            account -= price * quantity
            if name in warehouse:
                warehouse[name] += quantity
            else:
                warehouse[name] = quantity
            prices[name] = price
            action = print(f"Zakupiono {quantity} sztuk produktu '{name}' za {price * quantity} zł")
            history.append(action)
            save_warehouse(warehouse)
        else:
            action = print("Brak wystarczających środków na koncie")
            history.append(action)

    elif command == "konto":
        action = print(f"Stan konta: {account}")
        history.append(action)
        print(action)

    elif command == "lista":
        action = "Stan magazynu:"
        history.append(action)
        print(action)
        for name, quantity in warehouse.items():
            if name in prices:
                price = prices[name]
                action = print(f"{name}: ilość - {quantity}, cena - {price} zł")
                print(action)
                history.append(action)

    elif command == "magazyn":
        action = "Stan magazynu:"
        history.append(action)
        print(action)
        for name, quantity in warehouse.items():
            action = print(f"{name}: ilość - {quantity}")
            print(action)
            history.append(action)

    elif command == "przegląd":
        start_index = int(input("Podaj indeks 'od': "))
        end_index = int(input("Podaj indeks 'do': "))

        if not history:
            action = "Brak zapisanych operacji."
            history.append(action)
            print(action)
        elif start_index < 0 or end_index >= len(history):
            action = print(f"Nieprawidłowy zakres. Dostępne indeksy: od 0 do {len(history) - 1}")
            history.append(action)
            print(action)
        elif start_index > end_index:
            action = print("'Od' nie może być większe niż 'do'.")
            history.append(action)
            print(action)
        else:
            idx = history[start_index:end_index + 1]
            for index, operation in enumerate(idx):
                action = print(f"[{start_index + index}] {operation}")
                history.append(action)
                print(action)

    elif command == "koniec":
        break