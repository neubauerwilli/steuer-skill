---
name: steuer-rueckblick
description: >-
  Der Rückblick. Findet heraus, für welche vergangenen Jahre du noch eine
  Steuererklärung nachreichen kannst (Deutschland bis zu vier Jahre bei freiwilliger
  Abgabe, Österreich fünf Jahre Arbeitnehmerveranlagung), wann die Frist je Jahr endet
  und welche Jahre am meisten Geld versprechen. Dann geht es Jahr für Jahr mit den
  anderen Skills durch. Nutze ihn, wenn der Nutzer sagt "Steuer nachholen",
  "rückwirkend", "alte Jahre", "letzten Jahre zurückholen", "habe nie eine
  Steuererklärung gemacht" oder "verfällt mein Geld".
argument-hint: "[Land]"
---

# steuer-rueckblick

Wer als Arbeitnehmer nie eine Erklärung abgegeben hat, hat oft Jahre an Geld liegen lassen.
Ein Teil davon ist noch zu holen. Dieser Skill sagt, welcher.

Werkzeug in diesem Ordner:

```bash
python3 "${CLAUDE_SKILL_DIR}/fristen.py" --land de
python3 "${CLAUDE_SKILL_DIR}/fristen.py" --land at --heute 2026-10-28
```

## Grundregeln

Keine Steuerberatung, nichts abschicken. Fristen mit der offiziellen Quelle abgleichen.
Ergebnis nach `steuer/rueckblick.md`.

## Schritt 1: Pflicht oder freiwillig?

Die Regel für alte Jahre gilt nur, wenn der Nutzer **nicht zur Abgabe verpflichtet** war.
Frag kurz nach typischen Pflichtgründen:
- **Deutschland:** Steuerklasse III/V oder IV mit Faktor, mehrere Arbeitgeber gleichzeitig,
  Lohnersatz über 410 € (Elterngeld, Kurzarbeit, Arbeitslosengeld), Nebeneinkünfte über
  410 €, Aufforderung vom Finanzamt.
- **Österreich:** zwei oder mehr Bezüge gleichzeitig, andere Einkünfte über der
  Veranlagungsgrenze, zu Unrecht berücksichtigte Absetzbeträge, Aufforderung.
War jemand verpflichtet und hat nicht abgegeben, ist das kein Fall für diesen Skill: sag es
offen und empfiehl Lohnsteuerhilfeverein oder Steuerberatung, ohne Panik zu machen.

## Schritt 2: welche Jahre noch gehen

Lass `fristen.py` laufen. Es rechnet:
- **Deutschland:** freiwillige Erklärung (Antragsveranlagung) bis zum Ende des vierten
  Jahres nach dem Steuerjahr. Für 2022 also bis 31.12.2026.
- **Österreich:** Arbeitnehmerveranlagung bis zum Ende des fünften Jahres nach dem
  Steuerjahr. Für 2021 also bis 31.12.2026.
Es zeigt die offenen Jahre, das Fristende und die verbleibenden Tage, das dringendste zuerst.

## Schritt 3: welche Jahre sich lohnen

Frag je offenes Jahr kurz nach den Geldtreibern, ohne Belege zu verlangen:
- Jobwechsel, Arbeitslosigkeit, nicht das ganze Jahr gearbeitet
- Pendeln, Homeoffice, Umzug, Fortbildung, neuer Laptop
- Kinder, Handwerker, große Krankheitskosten
- Österreich zusätzlich: Familienbonus nicht über den Arbeitgeber bezogen

Ordne die Jahre: zuerst das Jahr, dessen Frist zuerst endet, dann das mit den meisten
Geldtreibern. Nenne keine Erstattungssumme als Versprechen; sag, warum ein Jahr
vielversprechend ist.

## Schritt 4: Jahr für Jahr abarbeiten

Für jedes Jahr ein eigener Ordner `steuer/<jahr>/`, dann die Kette wie für das aktuelle
Jahr: `/steuer-belege`, `/steuer-konto` (die Bank liefert alte Auszüge meist im
Onlinebanking oder auf Anfrage), dann die passenden Fach-Skills und `/steuer-formular`.
Werte immer für **das jeweilige Jahr** nachschlagen, nicht die von heute.

## Schritt 5: Frist sichern

Übergib die Fristen an `/steuer-fristen`, damit der Nutzer eine Erinnerung im Kalender hat,
spätestens vier Wochen vor dem Ende.

## Ergebnis

`steuer/rueckblick.md`: Tabelle Jahr, Fristende, Tage übrig, Geldtreiber, Reihenfolge.
