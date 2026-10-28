---
name: steuer-formular
description: >-
  Der Formular-Lotse. Fasst alles aus dem Ordner steuer/ zu einer Übersicht zusammen
  und führt Feld für Feld durch ELSTER (Deutschland) oder FinanzOnline (Österreich):
  welcher Wert in welchen Abschnitt kommt, was schon vorausgefüllt ist und was nicht
  doppelt eingetragen wird. Abschicken tust du selbst. Nutze ihn, wenn der Nutzer sagt
  "füll mit mir das Formular aus", "ELSTER", "FinanzOnline", "wo trage ich das ein",
  "Anlage N", "L1" oder "jetzt die Erklärung machen".
argument-hint: "[Jahr]"
---

# steuer-formular

Das Formular ist der Teil, vor dem die meisten aufgeben. Mit allen Zahlen vorbereitet und
einem, der sagt, wohin was gehört, ist es eine halbe Stunde.

Werkzeug in diesem Ordner:

```bash
python3 "${CLAUDE_SKILL_DIR}/uebersicht.py" steuer/<jahr>
```

## Grundregeln

- Du loggst dich nicht ein, tippst nichts ins Portal und schickst nichts ab. Der Nutzer hat
  das Portal offen, du sagst, was wohin kommt.
- Bezeichnungen von Anlagen, Abschnitten und Kennzahlen ändern sich zwischen den Jahren.
  Richte dich nach dem, was der Nutzer auf seinem Bildschirm sieht. Frag lieber nach dem
  genauen Feldnamen, als einen alten zu raten.
- Keine Steuerberatung. Bei Grenzfällen: offen sagen und auf Lohnsteuerhilfe,
  Steuerberatung oder Arbeiterkammer verweisen.

## Schritt 1: Übersicht bauen

`uebersicht.py` liest `belege.csv` und `kandidaten.csv` (nur Zeilen mit Entscheidung `ja`
oder `anteilig`) und schreibt `uebersicht.md`: Summe je Kategorie und je Skill, offene
Punkte ohne Beleg. Lies dazu `pendeln.md`, `homeoffice.md`, `werbungskosten.md`,
`haushalt.md` und `familie.md`, falls vorhanden.

## Schritt 2: Deutschland, ELSTER

- Zugang: Mein ELSTER mit Zertifikat oder ELSTER über die Ausweis-App. Ist noch keiner da,
  erkläre die Registrierung (der Aktivierungscode kommt per Post, das dauert ein paar Tage).
- Belegabruf aktivieren: Dann sind Lohnsteuerbescheinigung, Kranken- und
  Rentenversicherung vorausgefüllt. Nichts davon von Hand überschreiben, nur prüfen.
- Grobe Zuordnung, je nach Jahr in eigenen Anlagen oder geführten Abschnitten:
  Lohn und Werbungskosten (Pendeln, Homeoffice, Arbeitsmittel, Fortbildung) in der
  Anlage für Arbeitnehmer; Kinder in der Anlage für Kinder; Spenden, Kirchensteuer,
  Handwerker und haushaltsnahe Dienstleistungen im Bereich Sonderausgaben und
  Steuerermäßigungen; Versicherungen in der Anlage für Vorsorge.
- Geh mit dem Nutzer Abschnitt für Abschnitt durch. Je Feld: Wert, woher er kommt, Beleg.

## Schritt 3: Österreich, FinanzOnline

- Zugang über ID Austria. Arbeitnehmerveranlagung (Formular L1), bei Kindern die Beilage
  für Kinder (L1k), für Werbungskosten und Sonderausgaben die passenden Abschnitte.
- Lohnzettel, Spenden, Kirchenbeitrag und oft Versicherungsbeiträge meldet der Empfänger
  selbst: prüfen, nicht doppelt eintragen.
- Pendlerpauschale nur mit dem Wert aus dem BMF-Pendlerrechner.

## Schritt 4: Prüfen vor dem Absenden

Mach mit dem Nutzer einen Durchgang:
- Stimmen die Summen mit `uebersicht.md` überein?
- Ist nichts doppelt (Homeofficetage gegen Pendeltage, Spenden automatisch und von Hand)?
- Liegen alle Belege bereit, falls das Finanzamt nachfragt?
- Wurde die Vorschau oder Berechnung im Portal angeschaut?

Dann sag: Jetzt kannst du selbst abschicken. Hinterher den Bescheid mit `/steuer-bescheid`
prüfen und die Einspruchsfrist mit `/steuer-fristen` in den Kalender legen.
