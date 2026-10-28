---
name: steuer-bescheid
description: >-
  Der Bescheid-Prüfer. Vergleicht den Steuerbescheid mit dem, was du erklärt hast,
  findet gestrichene oder gekürzte Posten und Rechenfehler, erklärt die Begründung des
  Finanzamts in normaler Sprache und entwirft bei einem Fehler den Einspruch
  (Deutschland) oder die Beschwerde (Österreich), samt Frist. Nutze ihn, wenn der
  Nutzer sagt "prüf meinen Steuerbescheid", "Bescheid ist da", "stimmt der Bescheid",
  "Einspruch schreiben", "Beschwerde gegen den Bescheid" oder "warum bekomme ich weniger".
argument-hint: "[Pfad zum Bescheid]"
---

# steuer-bescheid

Bescheide sind nicht immer richtig. Wer nicht prüft, merkt es nie. Und die Frist für einen
Einspruch ist kurz.

## Grundregeln

Keine Steuerberatung, nichts abschicken. Einspruch oder Beschwerde reicht der Nutzer selbst
ein. Ergebnis nach `steuer/<jahr>/bescheid.md`, Entwurf nach `steuer/<jahr>/einspruch.md`.

## Schritt 1: Frist zuerst

Frag nach dem Datum des Bescheids und wie er kam (Post oder elektronisch).
- **Deutschland:** Einspruch innerhalb eines Monats nach Bekanntgabe. Ein Brief gilt seit
  2025 am vierten Tag nach der Aufgabe zur Post als bekanntgegeben (davor am dritten);
  fällt das auf ein Wochenende oder einen Feiertag, verschiebt es sich auf den nächsten
  Werktag.
- **Österreich:** Bescheidbeschwerde innerhalb eines Monats ab Zustellung, über
  FinanzOnline oder schriftlich. Eine Verlängerung der Frist kann beantragt werden.
Nenne das errechnete letzte Datum und gib es an `/steuer-fristen` weiter. Bei Zweifel das
frühere Datum nehmen.

## Schritt 2: vergleichen

Lies den Bescheid (PDF oder Foto) und die Übersicht aus `uebersicht.md` und den Dateien der
Fach-Skills. Vergleiche Zeile für Zeile:
- Lohn und einbehaltene Lohnsteuer wie in Lohnsteuerbescheinigung bzw. Lohnzettel?
- Werbungskosten, Pendeln, Homeoffice angesetzt wie erklärt?
- Sonderausgaben, Handwerker, Kinder, Familienbonus vollständig?
- Steht ein Abschnitt "Erläuterungen", "Begründung" oder ein Hinweis auf Abweichungen?

## Schritt 3: Abweichungen erklären

Je Abweichung: was erklärt war, was angesetzt wurde, Differenz, Begründung des Finanzamts
in einfachen Worten, und deine Einschätzung in drei Stufen:
- **Fehler des Amts:** Zahl falsch übernommen, Beleg lag vor. Einspruch sinnvoll.
- **Strittig:** Begründung nachvollziehbar, aber anfechtbar mit Beleg oder Erklärung.
- **Berechtigt:** Kürzung stimmt. Kein Einspruch, aber merken fürs nächste Jahr.

Rechne grob, was eine Korrektur bringt, und sag, dass es nur eine Schätzung ist.

## Schritt 4: Einspruch oder Beschwerde entwerfen

Nur, wenn es mindestens einen Fehler oder strittigen Punkt gibt. Kurz und sachlich:
- Absender, Finanzamt, Steuernummer (Platzhalter, nicht ausfüllen), Bescheid vom, Jahr.
- "Hiermit lege ich Einspruch gegen den Bescheid ... ein." bzw. "Hiermit erhebe ich
  Beschwerde gegen den Bescheid ...".
- Je Punkt: was geändert werden soll, warum, welcher Beleg beiliegt.
- Bitte um Aussetzung der Vollziehung nur, wenn eine Nachzahlung strittig ist.
- In Deutschland reicht der Einspruch formlos über ELSTER (Sonstige Nachricht oder
  Einspruch); in Österreich über FinanzOnline.

Lies den Entwurf mit dem Nutzer durch. Absenden tut er selbst.

## Ergebnis

`bescheid.md` mit Fristende, Tabelle der Abweichungen und Einschätzung; bei Bedarf
`einspruch.md`.
