---
name: steuer-homeoffice
description: >-
  Homeoffice für die Steuererklärung. Zählt die Tage zu Hause, wendet die
  Homeoffice-Pauschale an (Deutschland Tagespauschale, Österreich seit 2025 Telearbeitspauschale
  und Ausstattung), prüft, ob ein echtes Arbeitszimmer mehr bringt, und sammelt
  Schreibtisch, Stuhl, Monitor und Co. Nutze ihn, wenn der Nutzer sagt "Homeoffice
  absetzen", "Homeoffice-Pauschale", "Arbeitszimmer", "ich arbeite von zu Hause",
  "Schreibtisch absetzen" oder "Remote".
argument-hint: "[Homeoffice-Tage im Jahr]"
---

# steuer-homeoffice

Wer zu Hause arbeitet, zahlt Strom, Heizung und Möbel selbst. Ein Teil davon kommt zurück.

## Grundregeln

Keine Steuerberatung, nichts abschicken, Werte mit Jahr nennen und offiziell prüfen.
Ergebnis nach `steuer/<jahr>/homeoffice.md`.

## Schritt 1: die Tage

Frag nach den Tagen, an denen der Nutzer überwiegend zu Hause gearbeitet hat. Hilfen:
Kalender, Arbeitszeiterfassung, Homeoffice-Vereinbarung, Bestätigung des Arbeitgebers.
Gleiche mit `/steuer-pendeln` ab: Ein Tag ist entweder Pendeltag oder Homeofficetag. In
Deutschland darf an einem Tag mit Fahrt zur Arbeit die Pauschale nur gelten, wenn für die
Arbeit kein anderer Arbeitsplatz zur Verfügung stand; im Zweifel nicht doppelt ansetzen.

## Schritt 2: Deutschland

- Tagespauschale 6 € je Homeofficetag, höchstens 1.260 € im Jahr (210 Tage), so seit 2023.
  Jahr prüfen.
- Ein häusliches Arbeitszimmer (eigener Raum, fast nur beruflich) geht nur, wenn es der
  Mittelpunkt der gesamten Arbeit ist; dann Jahrespauschale oder tatsächliche Kosten
  statt der Tagespauschale. Frag nach, ob das zutrifft, und erkläre den Unterschied in
  zwei Sätzen.
- Arbeitsmittel wie Schreibtisch, Stuhl, Monitor, Headset zählen zusätzlich als
  Werbungskosten (über `/steuer-werbungskosten`).

## Schritt 3: Österreich

- Seit 2025 Telearbeitspauschale (vorher Homeoffice-Pauschale): bis zu 3 € je qualifiziertem
  Telearbeitstag für höchstens 100 Tage. Zahlt der
  Arbeitgeber weniger, darf die Differenz als Werbungskosten angesetzt werden. Die Tage
  stehen am Lohnzettel L16. Grenzen jährlich auf bmf.gv.at prüfen.
- Ergonomische Einrichtung (Schreibtisch, Stuhl, Beleuchtung) war mit eigener Obergrenze
  absetzbar. Prüf, ob und in welcher Höhe das für das Jahr des Nutzers noch gilt.
- Digitale Arbeitsmittel (Laptop, Handy) laufen über `/steuer-werbungskosten`.

## Ergebnis

`homeoffice.md` mit Tagen, Quelle der Tage, Pauschale, Rechnung und Jahr. Möbel und
Technik als Zeilen in `belege.csv` mit `skill` = `steuer-werbungskosten`.
