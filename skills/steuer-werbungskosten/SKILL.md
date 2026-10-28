---
name: steuer-werbungskosten
description: >-
  Der Werbungskosten-Jäger. Prüft alles, was du für deinen Job ausgibst: Laptop, Handy,
  Software, Fortbildung, Fachbücher, Gewerkschaft, Bewerbungen, Umzug, Arbeitskleidung.
  Rechnet berufliche Anteile, verteilt teure Geräte über die Jahre und zählt am Ende
  zusammen, ob du über die Pauschale kommst. Nutze ihn, wenn der Nutzer sagt
  "Werbungskosten", "Laptop absetzen", "Fortbildung absetzen", "Arbeitsmittel",
  "Handy absetzen", "Bewerbungskosten" oder "lohnt sich die Steuererklärung".
argument-hint: "[Jahr]"
---

# steuer-werbungskosten

Werbungskosten sind alles, was du ausgibst, um dein Gehalt zu verdienen. Das Finanzamt zieht
dir automatisch eine Pauschale ab. Alles darüber bringt Geld zurück.

## Grundregeln

Keine Steuerberatung, nichts abschicken, jede Grenze mit Jahr nennen und offiziell prüfen.
Ergebnis nach `steuer/<jahr>/werbungskosten.md`.

## Schritt 1: einsammeln

Lies `belege.csv` und `kandidaten.csv` (Zeilen mit `skill` = `steuer-werbungskosten`),
dazu `pendeln.md` und `homeoffice.md`, falls vorhanden. Frag dann gezielt nach, was oft
vergessen wird:
- Kontoführung (in Deutschland wird ein kleiner Pauschbetrag meist ohne Nachweis anerkannt)
- Gewerkschaft, Berufsverband
- Bewerbungen (Fotos, Mappen, Fahrten zum Gespräch)
- Fortbildung, Studium neben dem Job, Sprachkurs mit Jobbezug
- Arbeitskleidung, nur echte Berufskleidung (Kittel, Sicherheitsschuhe), kein Anzug
- Umzug aus beruflichem Grund
- Steuersoftware oder Lohnsteuerhilfe (Deutschland)

## Schritt 2: Anteile und Abschreibung

- **Beruflicher Anteil:** Frag nach einem ehrlichen Prozentsatz und schreib ihn dazu.
  Für Handy und Internet ist ein Teil der Kosten üblich, wenn beruflich genutzt.
- **Teure Geräte:** In Deutschland dürfen Computer, Laptop, Tablet und Software seit 2021
  im Jahr der Anschaffung voll abgesetzt werden (Nutzungsdauer ein Jahr). Andere
  Arbeitsmittel über 800 € netto werden über die Jahre verteilt.
  In Österreich gilt die Grenze für geringwertige Wirtschaftsgüter (Wert für das Jahr
  prüfen); darüber wird verteilt, ein Laptop meist über drei Jahre.
  Nenne bei jedem Gerät, welche Regel du anwendest und für welches Jahr.

## Schritt 3: zusammenzählen

| | Deutschland | Österreich |
| --- | --- | --- |
| Pauschale, die sowieso abgezogen wird | Arbeitnehmer-Pauschbetrag, 1.230 € seit 2023 | Werbungskostenpauschale 132 € |
| Pendeln | zählt in die Summe | Pendlerpauschale kommt zusätzlich |

Rechne die Summe offen vor und sag ehrlich:
- **Über der Pauschale:** Jeder Euro darüber senkt das zu versteuernde Einkommen.
- **Darunter:** Die Werbungskosten bringen nichts extra. Die Erklärung kann sich trotzdem
  lohnen, etwa durch Handwerker, Kinder, Spenden oder unterjährige Jobwechsel.

Was das in Euro Erstattung heißt, hängt vom persönlichen Steuersatz ab. Gib höchstens eine
grobe Spanne mit Rechenweg an und sag, dass der Bescheid entscheidet.

## Ergebnis

`werbungskosten.md`: Tabelle Posten, Betrag, Anteil, angesetzt, Regel, Beleg. Summe,
Vergleich mit der Pauschale, offene Fragen.
