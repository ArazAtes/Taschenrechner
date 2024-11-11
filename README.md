# Taschenrechner - README

## Projektbeschreibung

Dieses Python-Skript ist ein einfacher, textbasierter Taschenrechner, der die grundlegenden Rechenoperationen Addition, Subtraktion, Multiplikation und Division unterstützt. Der Benutzer kann eine Rechenoperation auswählen und zwei Zahlen eingeben, auf die die Operation angewendet wird. Am Ende der Berechnung kann der Benutzer entscheiden, ob er eine weitere Berechnung durchführen möchte.

## Funktionen

- **Addition**: Berechnet die Summe zweier Zahlen.
- **Subtraktion**: Berechnet die Differenz zwischen zwei Zahlen.
- **Multiplikation**: Berechnet das Produkt zweier Zahlen.
- **Division**: Berechnet den Quotienten zweier Zahlen und gibt eine Fehlermeldung bei Division durch Null aus.

## Voraussetzungen

- Python 3.x

## Installation

1. Speichern Sie den Code in einer Python-Datei, z. B. `taschenrechner.py`.
2. Stellen Sie sicher, dass Python 3 installiert ist.
3. Führen Sie das Skript in einer Kommandozeile oder IDE aus:

   ```bash
   python taschenrechner.py
   ```

## Verwendung

1. Wählen Sie die gewünschte Rechenoperation:
   - **1** für Addition
   - **2** für Subtraktion
   - **3** für Multiplikation
   - **4** für Division
2. Geben Sie zwei Zahlen ein, auf die die gewählte Operation angewendet wird.
3. Das Ergebnis wird direkt auf dem Bildschirm angezeigt.
4. Am Ende jeder Berechnung werden Sie gefragt, ob Sie eine weitere Berechnung durchführen möchten:
   - Geben Sie `ja` ein, um eine neue Berechnung zu starten.
   - Geben Sie `nein` ein, um das Programm zu beenden.

## Codeübersicht

### Funktionen

- **`add(x, y)`**: Gibt die Summe von `x` und `y` zurück.
- **`subtract(x, y)`**: Gibt die Differenz zwischen `x` und `y` zurück.
- **`multiply(x, y)`**: Gibt das Produkt von `x` und `y` zurück.
- **`divide(x, y)`**: Überprüft, ob `y` gleich Null ist. Falls ja, gibt sie eine Fehlermeldung aus; ansonsten gibt sie den Quotienten zurück.

### Benutzeroberfläche

- Die `calculator()`-Funktion leitet den Benutzer durch die Auswahl einer Operation, die Eingabe von Zahlen und zeigt das Ergebnis an.
- Am Ende der Berechnung wird der Benutzer gefragt, ob er eine neue Berechnung durchführen möchte.

### Endlosschleife

Das Programm läuft in einer Schleife, bis der Benutzer "nein" eingibt.

## Beispiel

```plaintext
Taschenrechner
Wählen Sie die Operation:
1. Addition
2. Subtraktion
3. Multiplikation
4. Division
Geben Sie Ihre Wahl (1/2/3/4): 1
Geben Sie die erste Zahl ein: 10
Geben Sie die zweite Zahl ein: 5
10.0 + 5.0 = 15.0
Möchten Sie noch eine Berechnung durchführen? (ja/nein): nein
Tschüss! Danke, dass Sie den Taschenrechner verwendet haben.
```

## Fehlerbehandlung

- **Ungültige Eingaben**: Wenn eine nicht-numerische Eingabe erfolgt, wird eine Fehlermeldung ausgegeben.
- **Division durch Null**: Bei Division durch Null wird eine spezifische Fehlermeldung zurückgegeben.

## Lizenz

Dieses Projekt ist Open-Source und kann frei kopiert, modifiziert und weiterverwendet werden.
