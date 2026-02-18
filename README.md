# Telefon Rückwärtssuche GUI

Ein kleines Python-Programm mit grafischer Oberfläche (GUI), das Telefonnummern auf **dasoertliche.de** rückwärts sucht und Name sowie Adresse anzeigt.

---

## 🖥️ Features

* GUI mit **Tkinter**: Eingabefeld für Telefonnummer und Ergebnisfeld
* Ruft **dasoertliche.de** auf und extrahiert Name, Straße, Hausnummer, PLZ und Stadt
* Behandelt Unicode-Zeichen korrekt (z. B. `&` statt `\u0026`)
* Fehlerbehandlung, z. B. keine Eingabe, ungültige Nummer oder nicht erreichbare Webseite

---

## ⚙️ Voraussetzungen

* Python 3.10+ (getestet mit 3.14 auf Mac)
* Virtuelle Umgebung empfohlen:

```bash
python3 -m venv venv
source venv/bin/activate
```

* Installierte Bibliotheken:

```bash
pip install requests beautifulsoup4 certifi
```

**Hinweis:** Mac-Nutzer können SSL-Probleme umgehen, indem `verify=False` in Requests gesetzt wird.

---

## 🚀 Nutzung

1. Repository klonen:

```bash
git clone https://github.com/Altuna61/telefon-rueckwaertssuche.git
cd telefon-rueckwaertssuche
```

2. Virtuelle Umgebung aktivieren:

```bash
source venv/bin/activate
```

3. GUI starten:

```bash
python telefonnrabfrage.py
```

4. Telefonnummer eingeben und auf „Suchen“ klicken. Das Ergebnis erscheint im Textfeld.

---

## 🧪 Unit Tests

Tests sind unter `tests/test_suche.py` verfügbar.
Tests ausführen:

```bash
python -m unittest discover tests
```

---

## 💾 Git Hinweise

1. Änderungen hinzufügen:

```bash
git add .
```

2. Commit erstellen (auf Deutsch, nach Best Practices):

```bash
git commit -m "Füge Rückwärtssuche GUI hinzu"
```

3. Push auf GitHub:

```bash
git push origin main
```

---

## 📌 Best Practices für Commit-Messages

* Max. 50 Zeichen in der Betreffzeile
* Erste Buchstabe groß, kein Punkt am Ende
* Leerzeile zwischen Betreff und Body
* Body max. 72 Zeichen pro Zeile
* Imperativ verwenden („Füge Feature hinzu“)
* Beschreibe **was** und **warum**, nicht **wie**

---

## ⚠️ Hinweise

* Ctrl+C im Terminal stoppt die GUI, wenn sie hängt
* Nutzung ohne Adminrechte auf Mac möglich, da `python-tk` über Brew installiert werden kann
* HTTPS-Warnungen auf Mac können auftreten (InsecureRequestWarning)
