#!/usr/bin/env python3
"""Welche Steuerjahre lassen sich als Arbeitnehmer noch nachholen?

Deutschland: freiwillige Erklärung (Antragsveranlagung) bis Ende des 4. Folgejahres.
Österreich: Arbeitnehmerveranlagung bis Ende des 5. Folgejahres.
Gilt nur ohne Pflicht zur Abgabe. Nur Standardbibliothek.

    python3 fristen.py --land de
    python3 fristen.py --land at --heute 2026-10-28 --json
"""
import argparse
import datetime as dt
import json
import sys

JAHRE_ZURUECK = {"de": 4, "at": 5}
NAME = {"de": "Deutschland, Antragsveranlagung", "at": "Österreich, Arbeitnehmerveranlagung"}


def offene_jahre(land, heute):
    n = JAHRE_ZURUECK[land]
    jahre = []
    # Ein Jahr ist erst nach seinem Ende erklärbar; das laufende Jahr zählt nicht
    for jahr in range(heute.year - n - 1, heute.year):
        ende = dt.date(jahr + n, 12, 31)
        if ende >= heute:
            jahre.append({"jahr": jahr, "frist_ende": ende.isoformat(), "tage_uebrig": (ende - heute).days})
    return sorted(jahre, key=lambda j: j["frist_ende"])

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--land", choices=["de", "at"], required=True)
    ap.add_argument("--heute", help="Stichtag JJJJ-MM-TT, Standard: heute")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    heute = dt.date.fromisoformat(a.heute) if a.heute else dt.date.today()
    jahre = offene_jahre(a.land, heute)

    if a.json:
        print(json.dumps({"land": a.land, "stichtag": heute.isoformat(), "jahre": jahre}, ensure_ascii=False, indent=2))
        return
    print("%s, Stichtag %s" % (NAME[a.land], heute.strftime("%d.%m.%Y")))
    print("Noch offen (dringendstes zuerst):")
    for j in jahre:
        ende = dt.date.fromisoformat(j["frist_ende"])
        warn = "  << weniger als 90 Tage" if j["tage_uebrig"] < 90 else ""
        print("  %d  bis %s  (%d Tage)%s" % (j["jahr"], ende.strftime("%d.%m.%Y"), j["tage_uebrig"], warn))
    print("Gilt nur ohne Pflicht zur Abgabe. Fristen bei der offiziellen Quelle prüfen.")


if __name__ == "__main__":
    main()
