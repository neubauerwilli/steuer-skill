---
name: steuer-pendeln
description: >-
  Der Pendler-Rechner. Rechnet den Weg zur Arbeit für die Steuererklärung: in
  Deutschland die Entfernungspauschale, in Österreich Pendlerpauschale und Pendlereuro
  über den offiziellen Pendlerrechner. Dazu Dienstreisen und doppelte Haushaltsführung
  als Hinweis. Nutze ihn, wenn der Nutzer sagt "Pendlerpauschale", "Fahrtkosten",
  "Weg zur Arbeit absetzen", "Pendlereuro", "Entfernungspauschale" oder "wie viele
  Kilometer".
argument-hint: "[einfache Strecke in km] [Arbeitstage]"
---

# steuer-pendeln

Für viele der größte einzelne Posten. Und einer, den man ohne Beleg bekommt: Es zählt die
Strecke, nicht der Tankbeleg.

## Grundregeln

Keine Steuerberatung, nichts abschicken, jeden Satz mit Jahr nennen und bei der
offiziellen Quelle prüfen. Ergebnis nach `steuer/<jahr>/pendeln.md`.

## Schritt 1: die Daten

Frag nach: Wohnort und Arbeitsort (oder direkt die kürzeste Straßenstrecke in km, einfach),
Arbeitstage vor Ort im Jahr (ohne Urlaub, Krankheit, Homeoffice), Verkehrsmittel,
Jobticket vom Arbeitgeber ja oder nein, Behinderung mit Merkzeichen ja oder nein.
Die Homeoffice-Tage gehen an `/steuer-homeoffice`, damit kein Tag doppelt zählt.

## Schritt 2: Deutschland

- Es zählt die kürzeste Straßenverbindung, einfache Strecke, nur volle Kilometer, ein Mal
  pro Arbeitstag, egal welches Verkehrsmittel.
- Sätze: für 2022 bis 2025 waren es 0,30 € je km für die ersten 20 km und 0,38 € ab dem
  21. km. Für 2026 ist 0,38 € ab dem ersten km beschlossen. Prüf den Satz für das Jahr
  des Nutzers auf bundesfinanzministerium.de, bevor du rechnest.
- Ohne eigenes Auto gilt eine Obergrenze von 4.500 € im Jahr (mit Auto keine).
  Tatsächlich höhere Ticketkosten dürfen statt der Pauschale angesetzt werden.
- Steuerfreie Jobtickets und Fahrgeld vom Arbeitgeber werden abgezogen; sie stehen in
  der Lohnsteuerbescheinigung.
- Rechne offen vor: `km × Tage × Satz`, aufgeteilt nach den Kilometerstufen.
- Erinnere: Alle Werbungskosten zusammen bringen erst etwas, wenn sie den
  Arbeitnehmer-Pauschbetrag übersteigen (1.230 € seit 2023, Jahr prüfen).
  `/steuer-werbungskosten` zählt zusammen.

## Schritt 3: Österreich

- Pendlerpauschale und Pendlereuro kommen nur über den **Pendlerrechner des BMF**
  (bmf.gv.at, Pendlerrechner). Du rechnest nicht selbst nach: Rechne vor, welche Angaben
  der Nutzer dort eintragen muss, und lass ihn das Ergebnis (Ausdruck L34) mitbringen.
- Kleines oder großes Pendlerpauschale hängt davon ab, ob Öffis zumutbar sind. Das
  entscheidet der Rechner, nicht du.
- Hat der Arbeitgeber das Pauschale schon in der Lohnverrechnung berücksichtigt, steht es
  am Lohnzettel. Dann nichts doppelt eintragen.
- Werbungskostenpauschale 132 € im Jahr: Das Pendlerpauschale wird zusätzlich gewährt.

## Schritt 4: was sonst noch zählt

Nenne nur, wenn es passt: Dienstreisen (Kilometergeld oder tatsächliche Kosten, wenn der
Arbeitgeber nicht erstattet), Fahrten zur Fortbildung, doppelte Haushaltsführung bei
Zweitwohnung am Arbeitsort. Diese Posten gehen an `/steuer-werbungskosten`.

## Ergebnis

`pendeln.md` mit Strecke, Tagen, Satz und Jahr, Rechnung, Summe und Quelle. Eine Zeile in
`belege.csv` mit Kategorie `Fahrt`, `notiz`: "Pauschale, kein Beleg nötig".
