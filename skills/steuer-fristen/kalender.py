#!/usr/bin/env python3
"""Steuertermine als Kalenderdatei (.ics) mit Erinnerungen.

Eingabe: JSON-Liste mit titel, datum (JJJJ-MM-TT), optional erinnern_tage und notiz.
Ausgabe: ganztägige Termine nach RFC 5545. Nur Standardbibliothek.

    python3 kalender.py steuer/termine.json --out steuer/steuer-termine.ics
"""
import argparse
import datetime as dt
import hashlib
import json
import sys


def esc(t):
    return t.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def falte(zeile):
    # Zeilen über 75 Byte nach RFC 5545 umbrechen
    b = zeile.encode("utf-8")
    if len(b) <= 75:
        return zeile
    teile, aktuell = [], b""
    for ch in zeile:
        c = ch.encode("utf-8")
        if len(aktuell) + len(c) > (75 if not teile else 74):
            teile.append(aktuell.decode("utf-8"))
            aktuell = b""
        aktuell += c
    teile.append(aktuell.decode("utf-8"))
    return "\r\n ".join(teile)

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("termine")
    ap.add_argument("--out", default="steuer-termine.ics")
    a = ap.parse_args()
    with open(a.termine, encoding="utf-8") as f:
        termine = json.load(f)

    jetzt = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    z = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//steuer-skill//DE", "CALSCALE:GREGORIAN"]
    for t in sorted(termine, key=lambda x: x["datum"]):
        try:
            tag = dt.date.fromisoformat(t["datum"])
        except (KeyError, ValueError):
            sys.exit("Ungültiges Datum in: %s" % t)
        uid = hashlib.sha1((t["titel"] + t["datum"]).encode("utf-8")).hexdigest()[:16] + "@steuer-skill"
        z += ["BEGIN:VEVENT", "UID:" + uid, "DTSTAMP:" + jetzt,
              "DTSTART;VALUE=DATE:" + tag.strftime("%Y%m%d"),
              "DTEND;VALUE=DATE:" + (tag + dt.timedelta(days=1)).strftime("%Y%m%d"),
              "SUMMARY:" + esc(t["titel"]),
              "DESCRIPTION:" + esc(t.get("notiz", "Erstellt mit dem Steuer-Skill. Keine Steuerberatung."))]
        for tage in t.get("erinnern_tage", [28, 7]):
            z += ["BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + esc(t["titel"]),
                  "TRIGGER:-P%dD" % int(tage), "END:VALARM"]
        z.append("END:VEVENT")
    z.append("END:VCALENDAR")

    with open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(falte(x) for x in z) + "\r\n")
    for t in sorted(termine, key=lambda x: x["datum"]):
        print("%s  %s" % (dt.date.fromisoformat(t["datum"]).strftime("%d.%m.%Y"), t["titel"]))
    print("-> %s (%d Termine)" % (a.out, len(termine)))


if __name__ == "__main__":
    main()
