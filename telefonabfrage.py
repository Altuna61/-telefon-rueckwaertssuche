# certifi sorgt dafür, dass HTTPS-Verbindungen verifiziert werden, auch wenn Mac keine Systemzertifikate richtig hat
import certifi
# Macht die grafische Oberfläche (Fenster, Buttons, Textfelder)
import tkinter as tk
# Macht HTTP-Anfragen
import requests
# Parst HTML, also liest die Webseite aus, damit wir Name & Adresse rausziehen können
from bs4 import BeautifulSoup
# Für das Durchsuchen des JavaScript-Blocks
import re

# Funktion zur echten Rückwärtssuche
# 	•	Baut die URL, die die Telefonnummer sucht
#	•	requests.get holt die HTML-Seite
#	•	timeout=10 → nach 10 Sekunden Abbruch, falls die Seite hängt
def suche_nummer(telefonnummer):
    try:
        url = "https://www.dasoertliche.de/"
        params = {
            "form_name": "search_inv",
            "ph": telefonnummer
        }

        response = requests.get(
            url,
            params=params,
            timeout=10,
            verify=False
        )

        if response.status_code != 200:
            return "Webseite nicht erreichbar."

        # HTML-Seite wird lesbar gemacht -> Dinge suchbar
        soup = BeautifulSoup(response.text, "html.parser")

        # handlerData aus dem JavaScript holen
        text = str(soup)
        result = []

        for line in text.splitlines():
            if "var handlerData " in line:
                result = re.findall(r'"(.*?)"', line)

        if result:
            try:
                name = result[14]
                strasse = result[9]
                hausnummer = result[10]
                stadt = result[4]
                plz = result[8]

                # Gibt Name + Adresse als Text zurück
                return f"{name}\n{strasse} {hausnummer}\n{plz} {stadt}"
            except IndexError:
                return "Eintrag gefunden, aber Struktur unerwartet."

        # Falls handlerData nicht gefunden wurde
        return "Kein Eintrag gefunden."

    except Exception as e:
        return f"Fehler bei der Suche: {e}"


# GUI 
def suchen():
    # Holt die Nummer aus dem Eingabefeld
    nummer = eingabe.get().replace(" ", "")  # Leerzeichen entfernen
    # Führt die Rückwärtssuche aus
    ergebnis = suche_nummer(nummer)
    # Löscht alte Ergebnisse
    ausgabe.delete("1.0", tk.END)
    # Zeigt das neue Ergebnis an
    ausgabe.insert(tk.END, ergebnis)


# Erstellt das Hauptfenster (GUI)
fenster = tk.Tk()
fenster.title("Telefon Rückwärtssuche")

# Text über dem Eingabefeld
tk.Label(fenster, text="Telefonnummer eingeben:").pack(pady=5)

# Feld zum Tippen der Telefonnummer
eingabe = tk.Entry(fenster)
# Zeigt dieses Element im Fenster an
eingabe.pack(fill="x", padx=10)

# Button
# Klick = Funktion suchen()
tk.Button(fenster, text="Suchen", command=suchen).pack(pady=10)

# Erstellt ein Textfeld, in das mehrere Zeilen Text reinpassen
#	•	tk.Text → Mehrzeiliges Textfeld
#	•	fenster → gehört zu diesem Fenster
#	•	height=8 → 8 Textzeilen hoch
ausgabe = tk.Text(fenster, height=8)
# Zeigt das Textfeld an (s.oben)
ausgabe.pack(fill="both", padx=10, pady=5)

# Hält das Fenster offen
# Ohne das schließt es sich sofort
fenster.mainloop()


# source venv/bin/activate
# python telefonnrabfrage.py 

# geht nicht, weil:
# keine Systembibliothek
# brew install python-tk
# kein Neuinstallieren von Python

# WEIL KEINE ADMIN RECHTEEEEE