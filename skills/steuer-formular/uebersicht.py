#!/usr/bin/env python3
"""Übersicht aus steuer/<jahr>/ für das Ausfüllen des Formulars.

Liest belege.csv und kandidaten.csv (nur Entscheidung ja oder anteilig <prozent>)
und schreibt uebersicht.md mit Summen je Kategorie. Nur Standardbibliothek.

    python3 uebersicht.py steuer/2025
"""
import argparse
import csv
import os
import re
import sys
from collections import OrderedDict


def zahl(t):
    t = (t or "").strip().replace("€", "").replace(" ", "")
    if re.search(r",\d{1,2}$", t):
        t = t.replace(".", "").replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def euro(x):
    s = "{:,.2f}".format(x)
    return s.replace(",", "X").replace(".", ",").replace("X", ".") + " €"


def lies(pfad):
    if not os.path.exists(pfad):
        return []
    with open(pfad, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ordner")
    a = ap.parse_args()

    posten, offen = [], []
    for z in lies(os.path.join(a.ordner, "belege.csv")):
        if (z.get("kategorie") or "").strip().lower() == "privat":
            continue
        b = zahl(z.get("betrag"))
        if b is None:
            offen.append("Beleg ohne lesbaren Betrag: %s %s" % (z.get("datum", ""), z.get("aussteller", "")))
            continue
        posten.append((z.get("kategorie") or "Sonstiges", z.get("skill") or "", b, "Beleg"))
        if not (z.get("datei") or "").strip():
            offen.append("Ohne Belegdatei: %s %s %s" % (z.get("datum", ""), z.get("aussteller", ""), euro(b)))

    belegt = {(z.get("datum"), zahl(z.get("betrag"))) for z in lies(os.path.join(a.ordner, "belege.csv"))}
    for z in lies(os.path.join(a.ordner, "kandidaten.csv")):
        e = (z.get("entscheidung") or "").strip().lower()
        b = zahl(z.get("betrag"))
        if b is None or not (e == "ja" or e.startswith("anteilig")):
            continue
        if (z.get("datum"), b) in belegt:
            continue
        if e.startswith("anteilig"):
            m = re.search(r"(\d+(?:[.,]\d+)?)", e)
            b = b * float(m.group(1).replace(",", ".")) / 100 if m else b
        posten.append((z.get("kategorie") or "Sonstiges", z.get("skill") or "", b, "Kontoauszug"))

    summen = OrderedDict()
    for kat, skill, b, quelle in posten:
        summen.setdefault(kat, [0.0, skill, 0])
        summen[kat][0] += b
        summen[kat][2] += 1

    zeilen = ["# Übersicht %s" % os.path.basename(os.path.normpath(a.ordner)), "",
              "| Kategorie | Posten | Summe | weiter mit |", "| --- | --- | --- | --- |"]
    for kat, (s, skill, n) in summen.items():
        zeilen.append("| %s | %d | %s | %s |" % (kat, n, euro(s), skill))
    zeilen += ["", "**Gesamt:** %s (vor Pauschalen, Anteilen und Grenzen der Fach-Skills)" % euro(sum(v[0] for v in summen.values()))]
    if offen:
        zeilen += ["", "## Offen", ""] + ["- " + o for o in offen]
    zeilen += ["", "Keine Steuerberatung. Was zurückkommt, steht erst im Bescheid."]

    ziel = os.path.join(a.ordner, "uebersicht.md")
    with open(ziel, "w", encoding="utf-8") as f:
        f.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen))
    print("\n-> %s" % ziel)


if __name__ == "__main__":
    main()
