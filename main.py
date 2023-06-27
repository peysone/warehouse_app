from pprint import pprint

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

    if command == "saldo":
        sum = float(input("Wprowadź kwotę: "))
        account += sum
        action = f"Dodano {sum} do konta"


    if command == "sprzedaż":
        name = input("Wprowadź nazwę produktu: ")

        if name in warehouse:
            price = float(input("Wprowadź cenę: "))
            quantity = int(input("Wprowadź liczbę sztuk: "))

            if warehouse[name] >= quantity:
                warehouse[name] -= quantity
                sum = price * quantity
                account += sum
                action = f"Sprzedano {quantity} sztuk produktu '{name}' za {sum}"
            else:
                print("Nie wystarczająca ilość produktu w magazynie")
        if name not in warehouse:
            print("Produkt nie istnieje w magazynie")


    if command == "zakup":
        name = input("Wprowadź nazwę produktu: ")
        price = float(input("Wprowadź cenę: "))
        quantity = int(input("Wprowadź liczbę sztuk: "))

        if account >= price * quantity:
            account -= price * quantity

            if name in warehouse:
                warehouse[name] += quantity
            else:
                warehouse[name] = quantity

            action = f"Zakupiono {quantity} sztuk produktu '{name}' za {price * quantity}"
        else:
            print("Brak wystarczających środków na koncie")