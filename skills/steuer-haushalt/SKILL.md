---
name: steuer-haushalt
description: >-
  Haushalt, Handwerker und Sonderausgaben. Findet in Deutschland Handwerkerleistungen
  und haushaltsnahe Dienstleistungen (auch in der Nebenkostenabrechnung), in beiden
  Ländern Spenden, Kirchenbeitrag, Versicherungen und Krankheitskosten. Nutze ihn, wenn
  der Nutzer sagt "Handwerker absetzen", "Putzhilfe absetzen", "Nebenkostenabrechnung",
  "Spenden absetzen", "Kirchenbeitrag", "Sonderausgaben", "Krankheitskosten" oder
  "außergewöhnliche Belastungen".
argument-hint: "[Jahr]"
---

# steuer-haushalt

Hier liegt oft Geld, das niemand vermutet: der Elektriker, der Schornsteinfeger, der
Hausmeister in der Nebenkostenabrechnung, die Spende an Weihnachten.

## Grundregeln

Keine Steuerberatung, nichts abschicken, Werte mit Jahr nennen und offiziell prüfen.
Ergebnis nach `steuer/<jahr>/haushalt.md`.

## Schritt 1: einsammeln

Lies die Zeilen mit `skill` = `steuer-haushalt` aus `belege.csv` und `kandidaten.csv`.
Frag nach der **Nebenkostenabrechnung** (Mieter) oder der **Hausgeldabrechnung**
(Eigentümer): Dort stehen oft Hausmeister, Treppenhausreinigung, Gartenpflege, Wartung,
Winterdienst und Schornsteinfeger, die anteilig zählen.

## Schritt 2: Deutschland

- **Handwerker** (Reparatur, Wartung, Modernisierung in der eigenen Wohnung, auch zur
  Miete): 20 % der Arbeitskosten, höchstens 1.200 € Steuerermäßigung im Jahr.
- **Haushaltsnahe Dienstleistungen** (Reinigung, Gartenpflege, Pflege): 20 %, höchstens
  4.000 € im Jahr. Minijob im Haushalt eigene Grenze.
- Bedingungen: Rechnung mit ausgewiesenem Arbeitslohn (Material zählt nicht) und Zahlung
  per Überweisung, nicht bar. Fehlt eins davon, sag es klar.
- Das ist eine Ermäßigung direkt auf die Steuer, nicht nur auf das Einkommen. Darum oft
  mehr wert als gleich hohe Werbungskosten.
- **Sonderausgaben:** Spenden an begünstigte Empfänger (bis 300 € reicht der Kontoauszug
  als Nachweis), Kirchensteuer (meist schon in der Lohnsteuerbescheinigung),
  Vorsorgeaufwendungen.
- **Außergewöhnliche Belastungen:** Krankheitskosten, Brille, Zahnersatz zählen erst über
  der zumutbaren Belastung, die von Einkommen und Familienstand abhängt. Erst
  zusammenzählen, dann sagen, ob es reicht.

## Schritt 3: Österreich

- Handwerker sind in der Arbeitnehmerveranlagung kein eigener Posten (der Handwerkerbonus
  ist eine Förderung, die extra beantragt wird).
- **Sonderausgaben:** Spenden an begünstigte Einrichtungen und Kirchenbeitrag werden meist
  automatisch vom Empfänger gemeldet; prüf im Formular, ob sie schon da sind. Dazu
  Steuerberatungskosten und freiwillige Weiterversicherung. Höchstgrenzen fürs Jahr prüfen.
- **Außergewöhnliche Belastungen:** Krankheitskosten mit Selbstbehalt, Behinderung,
  Katastrophenschäden. Erst zusammenzählen, dann den Selbstbehalt prüfen.

## Ergebnis

`haushalt.md` mit Posten, Betrag, Art (Ermäßigung, Sonderausgabe, Belastung), Nachweis
vorhanden ja oder nein, Jahr der Regel. Fehlende Rechnungen als Liste zum Nachfordern.
