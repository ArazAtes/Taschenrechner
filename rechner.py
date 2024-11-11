# Funktion für Addition
def add(x, y):
    return x + y

# Funktion für Subtraktion
def subtract(x, y):
    return x - y

# Funktion für Multiplikation
def multiply(x, y):
    return x * y

# Funktion für Division
def divide(x, y):
    if y == 0:
        return "Fehler! Division durch Null."
    else:
        return x / y

# Benutzeroberfläche
def calculator():
    print("Taschenrechner")
    print("Wählen Sie die Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    # Eingabe der Auswahl
    choice = input("Geben Sie Ihre Wahl (1/2/3/4): ")

    # Eingabe der Zahlen
    try:
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie gültige Zahlen ein.")
        return

    # Operation basierend auf der Auswahl durchführen
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Ungültige Eingabe! Bitte wählen Sie eine gültige Option.")

# Hauptloop des Programms
while True:
    calculator()
    again = input("Möchten Sie noch eine Berechnung durchführen? (ja/nein): ").lower()
    if again != 'ja':
        print("Tschüss! Danke, dass Sie den Taschenrechner verwendet haben.")
        break
