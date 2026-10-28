---
name: steuer-belege
description: >-
  Der Belegsammler und Einstieg in den Steuer-Skill. Klärt Land (Deutschland oder
  Österreich), Steuerjahr und Lebenslage, legt den Ordner steuer/ an und liest
  Rechnungen und Quittungen aus Fotos, Scans und PDFs in eine sortierte Liste
  belege.csv. Nutze ihn, wenn der Nutzer sagt "mach meine Steuererklärung",
  "wo fange ich an", "sortier meine Belege", "Rechnungen für die Steuer",
  "Quittungen abfotografiert", "Steuer-Skill starten" oder "Arbeitnehmerveranlagung".
argument-hint: "[Ordner mit Belegen]"
---

# steuer-belege

Der Anfang von allem: Wer seine Belege beisammen hat, hat die halbe Steuererklärung.
Dieser Skill macht aus einem Haufen Fotos und PDFs eine Liste, mit der die anderen zehn
Skills arbeiten.

## Grundregeln (gelten für das ganze Paket)

- Du bist keine Steuerberatung und schickst nie etwas ab. Abgeben tut der Nutzer selbst.
- Pauschalen und Grenzen ändern sich. Nenne immer das Jahr eines Werts und prüfe ihn bei
  der offiziellen Quelle (Deutschland: bundesfinanzministerium.de, elster.de; Österreich:
  bmf.gv.at). Weißt du einen Wert nicht sicher, sag es.
- Rate dem Nutzer, IBAN, Steuer-ID und Sozialversicherungsnummer zu schwärzen. Gebraucht
  werden Datum, Betrag, Aussteller und Zweck.
- Alles bleibt im Ordner `steuer/<jahr>/` auf dem Rechner des Nutzers.

## Schritt 1: drei Fragen

1. **Land:** Deutschland oder Österreich?
2. **Jahr:** Welches Steuerjahr? Unsicher, welche Jahre noch gehen: `/steuer-rueckblick`.
3. **Lage:** angestellt, Studium, Ausbildung, Kinder, Homeoffice, Pendeln, Nebenjob.
   Selbstständig, Vermietung oder Auslandseinkünfte: sag offen, dass dieses Paket dafür
   nicht reicht, und empfiehl Steuerberatung.

Schreib die Antworten nach `steuer/<jahr>/profil.md`. Gibt es die Datei schon, lies sie
und frag nicht erneut.

## Schritt 2: Belege einlesen

Lies jede Datei, die der Nutzer gibt (Foto, Scan, PDF, Mail-Rechnung). Pro Beleg eine
Zeile in `steuer/<jahr>/belege.csv`, getrennt mit Semikolon:

```
datum;aussteller;betrag;zweck;kategorie;skill;datei;bezahlt_per;notiz
2025-03-14;Elektromarkt;899,00;Laptop;Arbeitsmittel;steuer-werbungskosten;belege/laptop.jpg;Karte;privat mitgenutzt?
```

- `kategorie`: Arbeitsmittel, Fortbildung, Fachliteratur, Fahrt, Homeoffice, Handwerker,
  Haushaltshilfe, Kinderbetreuung, Spende, Versicherung, Gesundheit, Sonstiges, Privat.
- `skill`: welcher der Skills den Posten weiter prüft.
- `bezahlt_per`: Überweisung, Karte oder bar. Wichtig in Deutschland: Handwerker und
  Haushaltshilfe zählen nur per Überweisung, nicht bar.
- Unleserlich oder unklar: Zeile trotzdem anlegen, `notiz` sagt, was fehlt.

Rein private Käufe ohne Bezug zu Arbeit, Familie, Gesundheit, Wohnung oder Spende
kommen mit Kategorie `Privat` in die Liste, damit nichts doppelt geprüft wird.

## Schritt 3: Lücken nennen

Sag am Ende in wenigen Zeilen:
- wie viele Belege, Summe je Kategorie,
- welche Belege fehlen, die bei dieser Lage fast jeder hat (etwa Lohnsteuerbescheinigung
  in Deutschland, Lohnzettel L16 in Österreich, Spendenbestätigungen, Kita-Rechnungen),
- welcher Skill als Nächstes dran ist. Meist `/steuer-konto`, weil im Kontoauszug die
  Posten stehen, für die es keinen Beleg mehr gibt.
