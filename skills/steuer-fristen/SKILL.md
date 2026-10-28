---
name: steuer-fristen
description: >-
  Der Fristen-Wächter. Sammelt alle Steuertermine des Nutzers (Abgabefrist, Fristende
  für alte Jahre, Einspruchsfrist, Belege nachreichen) und baut daraus eine
  Kalenderdatei (.ics) mit Erinnerungen, die in Google, Outlook oder Apple Kalender
  importiert wird. Nutze ihn, wenn der Nutzer sagt "erinnere mich", "Steuerfristen",
  "bis wann muss ich abgeben", "Kalender für die Steuer", "Abgabefrist" oder
  "Einspruchsfrist eintragen".
argument-hint: "[Land]"
---

# steuer-fristen

Geld verfällt nicht, weil es niemandem zusteht, sondern weil ein Datum vorbeigeht. Dieser
Skill legt jedes Datum in den Kalender.

Werkzeug in diesem Ordner:

```bash
python3 "${CLAUDE_SKILL_DIR}/kalender.py" steuer/termine.json --out steuer/steuer-termine.ics
```

## Grundregeln

Keine Steuerberatung, nichts abschicken. Du legst nichts selbst in einen fremden Kalender
an: Du erzeugst eine Datei, die der Nutzer importiert. Termine mit der offiziellen Quelle
abgleichen.

## Schritt 1: Termine sammeln

Aus den anderen Skills, falls vorhanden:
- `steuer/rueckblick.md`: Fristende je offenes Jahr (`/steuer-rueckblick`)
- `steuer/<jahr>/bescheid.md`: Einspruchs- oder Beschwerdefrist (`/steuer-bescheid`)
- `steuer/<jahr>/uebersicht.md`: offene Belege zum Nachfordern

Dazu die festen Termine, wenn der Nutzer zur Abgabe verpflichtet ist (Jahr prüfen):
- **Deutschland:** Pflichtabgabe ohne Berater bis 31. Juli des Folgejahres; mit
  Steuerberatung oder Lohnsteuerhilfeverein deutlich später. Freiwillige Erklärung: vier
  Jahre Zeit.
- **Österreich:** Pflichtveranlagung bis 30. April (Papier) bzw. 30. Juni (FinanzOnline)
  des Folgejahres. Freiwillige Arbeitnehmerveranlagung: fünf Jahre Zeit.

## Schritt 2: termine.json schreiben

```json
[
  {"titel": "Steuer 2022 nachholen, letzter Tag", "datum": "2026-12-31", "erinnern_tage": [28, 7]},
  {"titel": "Einspruchsfrist Bescheid 2025", "datum": "2026-08-14", "erinnern_tage": [7, 2]}
]
```

`erinnern_tage`: wie viele Tage vorher der Kalender erinnert. Vorgabe: vier Wochen und
eine Woche vorher, bei Einspruchsfristen eine Woche und zwei Tage.

## Schritt 3: Kalenderdatei bauen

`kalender.py` erzeugt ganztägige Termine mit Erinnerungen in einer `.ics`-Datei. Erklär den
Import in einem Satz je Kalender:
- Google Kalender: Einstellungen, Importieren und Exportieren, Datei wählen.
- Outlook: Datei öffnen oder in den Kalender ziehen.
- Apple: Datei doppelklicken.

## Ergebnis

`steuer/termine.json` und `steuer/steuer-termine.ics`, dazu eine kurze Liste aller Termine
nach Datum.
