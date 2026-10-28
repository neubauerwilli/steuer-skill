---
name: steuer-konto
description: >-
  Der Kontoauszug-Scanner. Geht einen Kontoauszug (CSV-Export der Bank oder PDF) Zeile
  für Zeile durch und markiert jede Ausgabe, die steuerlich zählen kann: Arbeitsmittel,
  Software, Fortbildung, Handwerker, Spenden, Versicherungen, Kinderbetreuung und mehr.
  Ergebnis ist kandidaten.csv mit Grund und zuständigem Skill. Nutze ihn, wenn der
  Nutzer sagt "geh meinen Kontoauszug durch", "was kann ich absetzen",
  "Kontoauszug für die Steuer", "finde absetzbare Ausgaben" oder "Umsätze prüfen".
argument-hint: "[Pfad zum Kontoauszug]"
---

# steuer-konto

Die meisten vergessen Geld, weil der Beleg weg ist. Die Abbuchung steht aber noch im
Konto. Dieser Skill findet sie.

Werkzeug in diesem Ordner:

```bash
python3 "${CLAUDE_SKILL_DIR}/scan.py" kontoauszug.csv --out steuer/<jahr>/kandidaten.csv
```

Unter Windows oft `py` statt `python3`. Nur Python 3.8 oder neuer, nichts installieren.

## Grundregeln

Keine Steuerberatung, nichts abschicken, Werte mit Jahr und offizieller Quelle prüfen,
IBAN und Kontonummern schwärzen lassen. Alles bleibt in `steuer/<jahr>/`.

## Schritt 1: den Auszug holen

Bitte um den CSV-Export der Bank für das Steuerjahr (fast jede Bank bietet ihn im
Onlinebanking an). Ein PDF geht auch: Dann liest du die Umsätze selbst und schreibst sie
als CSV mit den Spalten `datum;empfaenger;verwendungszweck;betrag`.

## Schritt 2: Werkzeug laufen lassen

`scan.py` erkennt Spaltennamen der gängigen Banken selbst, liest Komma und Punkt als
Dezimalzeichen und prüft nur Ausgaben. Es vergleicht Empfänger und Verwendungszweck mit
den Mustern in `regeln.json` und schreibt jeden Treffer mit Kategorie, Skill und Hinweis
in `kandidaten.csv`. Am Ende druckt es die Summe je Kategorie.

Die Muster sind ein Netz, kein Urteil. Ein Treffer heißt: anschauen.

## Schritt 3: mit dem Nutzer durchgehen

Geh die Treffer nach Kategorie durch, nicht Zeile für Zeile. Frag je Gruppe nur, was du
nicht weißt, zum Beispiel:
- Laptop, Handy, Software: Wie viel davon nutzt du beruflich? (Anteil in Prozent)
- Handwerker: Gibt es eine Rechnung mit ausgewiesenem Arbeitslohn?
- Abos: Ist das ein Fachmagazin oder Unterhaltung?

Markiere jede Zeile in `kandidaten.csv` mit `ja`, `nein` oder `anteilig <prozent>`.
Bestätigte Posten kommen nach `belege.csv`, falls dort noch nicht vorhanden (gleiche
Spalten, `datei` bleibt leer, `notiz`: "aus Kontoauszug, Beleg suchen").

## Schritt 4: Übergabe

Sag, wie viel Euro bestätigt sind, je Kategorie, und welcher Skill sie weiter prüft.
Erfinde keine Erstattung: Was am Ende zurückkommt, hängt vom Steuersatz ab und steht erst
im Bescheid.

## Muster erweitern

Fehlt ein Händler, ergänz `regeln.json`: ein Eintrag mit `muster` (Wörter, Groß- und
Kleinschreibung egal), `kategorie`, `skill` und `hinweis`.
