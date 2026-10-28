# Der Steuer-Skill

Elf Claude-Skills auf Deutsch, die mit dir deine Steuererklärung machen. Für Arbeitnehmer in
Deutschland und Österreich. Das Paket ist kostenlos und MIT-lizenziert. Der Skill braucht
keine eigene Anmeldung und keinen zusätzlichen API-Schlüssel. Claude-Zugang und
Nutzungskontingente sind separat. Lokale Ergebnisdateien liegen im Projektordner;
Inhalte, die du Claude zeigst, werden über deinen Claude-Zugang verarbeitet.

Einer sortiert deine Belege. Ein anderer markiert im Kontoauszug mögliche Abzugsposten.
Ein weiterer hilft dir, Angaben für ELSTER oder FinanzOnline vorzubereiten. Der Rückblick
prüft offene Jahre und Fristen. Eine Erstattung wird nicht garantiert. Kommt der Bescheid,
vergleicht Claude ihn mit deiner Erklärung und nennt konkrete Abweichungen.

**Abgeschickt wird nichts, bevor du Ja sagst.** Kein Skill loggt sich ein oder reicht etwas ein.
Das machst du selbst.

> Keine Steuerberatung. Der Skill erklärt, rechnet vor und bereitet vor. Für Selbstständige,
> Vermieter, Auslandseinkünfte oder Grenzfälle ist eine Steuerberatung, ein
> Lohnsteuerhilfeverein oder die Arbeiterkammer der richtige Weg.

## Einrichten

Du kannst Claude den Link und die Anweisung `install skill` geben:

```
https://github.com/neubauerwilli/steuer-skill

install skill
```

Das ist eine Chat-Anweisung, keine universelle Installationsfunktion. Ob Claude Dateien
installieren kann, hängt vom verwendeten Modus ab. Der konkrete Weg in Claude Code ist:

```
/plugin marketplace add neubauerwilli/steuer-skill
/plugin install steuer-skill@steuer-skill
```

Als Plugin bekommen die Skills einen Namensraum, sie heißen dann `/steuer-skill:steuer-belege`
und so weiter. Wenn du einfach `/steuer-belege` willst, kopiere die Ordner:

```bash
git clone https://github.com/neubauerwilli/steuer-skill.git
cp -r steuer-skill/skills/steuer-* ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/neubauerwilli/steuer-skill.git
Copy-Item -Recurse steuer-skill\skills\steuer-* "$env:USERPROFILE\.claude\skills\"
```

Kein Claude Code? Lade einzelne Skill-Ordner als ZIP unter **Anpassen / Customize > Skills**
hoch und aktiviere sie. Code-Ausführung und Dateierstellung müssen eingeschaltet sein.
Der normale Chat schreibt nicht automatisch in deinen lokalen Ordner. Alternativ kannst du
eine einzelne `SKILL.md` als Arbeitsanweisung in einen Chat einfügen; das ist keine Installation
und führt die Python-Werkzeuge nicht automatisch aus.
[Aktuelle offizielle Skill-Anleitung](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Die Werkzeuge brauchen Python 3.8 oder neuer, nichts per pip installieren. Unter Windows heißt
der Aufruf oft `py` statt `python3`.

## Die elf

| Befehl | Rolle | Was er macht |
| --- | --- | --- |
| `/steuer-belege` | Belegsammler | Klärt Land, Jahr und Lage, legt den Ordner `steuer/` an und liest Fotos, Scans und PDFs in eine sortierte Belegliste. |
| `/steuer-konto` | Kontoauszug-Scanner | Geht den Kontoauszug durch und markiert jede Ausgabe, die zählen kann. Werkzeug: `scan.py`. |
| `/steuer-pendeln` | Pendler-Rechner | Weg zur Arbeit: Entfernungspauschale (DE), Pendlerpauschale und Pendlereuro über den BMF-Rechner (AT). |
| `/steuer-homeoffice` | Homeoffice | Tage zu Hause, Homeoffice-Pauschale, Arbeitszimmer, Schreibtisch und Stuhl. |
| `/steuer-werbungskosten` | Werbungskosten-Jäger | Laptop, Handy, Software, Fortbildung, Fachbücher, Gewerkschaft. Zählt zusammen, ob du über die Pauschale kommst. |
| `/steuer-haushalt` | Haushalt und Handwerker | Handwerker und Haushaltshilfe (DE), Nebenkostenabrechnung, Spenden, Kirchenbeitrag, Krankheitskosten. |
| `/steuer-familie` | Familie | Kinderbetreuung und Schulgeld (DE), Familienbonus Plus und Absetzbeträge (AT). |
| `/steuer-rueckblick` | Rückblick | Welche alten Jahre noch gehen (DE vier, AT fünf), Fristende je Jahr, welche sich lohnen. Werkzeug: `fristen.py`. |
| `/steuer-formular` | Formular-Lotse | Übersicht aller Posten und Feld für Feld durch ELSTER oder FinanzOnline. Werkzeug: `uebersicht.py`. |
| `/steuer-bescheid` | Bescheid-Prüfer | Vergleicht Bescheid und Erklärung, erklärt Abweichungen und entwirft Einspruch oder Beschwerde. |
| `/steuer-fristen` | Fristen-Wächter | Alle Termine als Kalenderdatei mit Erinnerungen. Werkzeug: `kalender.py`. |

## So nutzt du ihn

Fang mit `/steuer-belege` an. Er fragt drei Dinge und sagt dir dann, welche Skills für dich
dran sind. Jeder Skill liest und schreibt in `steuer/<jahr>/` in deinem Projekt:

```
steuer/
├── rueckblick.md
├── termine.json  ·  steuer-termine.ics
└── 2025/
    ├── profil.md
    ├── belege.csv  ·  kandidaten.csv
    ├── pendeln.md  ·  homeoffice.md  ·  werbungskosten.md  ·  haushalt.md  ·  familie.md
    ├── uebersicht.md
    └── bescheid.md  ·  einspruch.md
```

Nie eine Erklärung gemacht? Starte mit `/steuer-rueckblick`. Er zeigt, welche Jahre noch offen
sind und welche Frist zuerst endet.

## Datenschutz

Alles läuft in deinem Projektordner. Schwärze IBAN, Steuer-ID und Sozialversicherungsnummer,
bevor du Dateien zeigst; gebraucht werden Datum, Betrag und Zweck. Was du Claude zeigst, geht
an deinen Claude-Zugang, wie jede andere Unterhaltung auch.

## Werte und Jahre

Pauschalen und Grenzen ändern sich fast jedes Jahr. Die Skills nennen zu jedem Wert das Jahr
und prüfen ihn bei der offiziellen Quelle (bundesfinanzministerium.de, elster.de, bmf.gv.at).
Fällt dir ein veralteter Wert auf, schreib ein Issue.

## Ausprobieren ohne eigene Daten

Im Ordner [`beispiel`](beispiel/) liegt ein erfundener Kontoauszug:

```bash
python3 skills/steuer-konto/scan.py beispiel/kontoauszug.csv --out steuer/2025/kandidaten.csv
python3 skills/steuer-rueckblick/fristen.py --land de
python3 skills/steuer-fristen/kalender.py beispiel/termine.json --out steuer/steuer-termine.ics
```

Von Willi Neubauer · Lizenz: [MIT](LICENSE)
