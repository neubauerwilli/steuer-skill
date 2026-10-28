#!/usr/bin/env python3
"""Übersicht aus steuer/<jahr>/ für das Ausfüllen des Formulars.

Liest belege.csv und kandidaten.csv (nur Entscheidung ja oder anteilig <prozent>)
und schreibt uebersicht.md mit Summen je Kategorie. Nur Standardbibliothek.

    python3 uebersicht.py steuer/2025
"""
import argparse
import csv
import datetime as dt
import math
import os
import re
import sys
from collections import OrderedDict


def zahl(t):
    t = (t or "").strip().replace("€", "").replace(" ", "")
    if re.search(r",\d{1,2}$", t):
        t = t.replace(".", "").replace(",", ".")
    try:
        n = float(t)
        return n if math.isfinite(n) else None
    except ValueError:
        return None


def norm_datum(text):
    text = (text or "").strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y"):
        try:
            return dt.datetime.strptime(text, fmt).date().isoformat()
        except ValueError:
            pass
    return text


def norm_text(text):
    return " ".join((text or "").casefold().split())


def beleg_schluessel(z, kandidat=False):
    # Datum und Betrag allein identifizieren keinen Umsatz.
    empfaenger = z.get("empfaenger") if kandidat else z.get("aussteller")
    zweck = z.get("verwendungszweck") if kandidat else z.get("zweck")
    if not norm_text(empfaenger) or not norm_text(zweck):
        return None
    return (norm_datum(z.get("datum")), zahl(z.get("betrag")),
            norm_text(empfaenger), norm_text(zweck))


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
    belege = lies(os.path.join(a.ordner, "belege.csv"))
    kandidaten = lies(os.path.join(a.ordner, "kandidaten.csv"))
    if not belege and not kandidaten:
        offen.append("Keine Belege oder Kontoauszugsposten vorhanden. Zuerst Material einlesen; 0 Euro ist kein fertiges Steuerergebnis.")
    for z in belege:
        if (z.get("kategorie") or "").strip().lower() == "privat":
            continue
        b = zahl(z.get("betrag"))
        if b is None:
            offen.append("Beleg ohne lesbaren Betrag: %s %s" % (z.get("datum", ""), z.get("aussteller", "")))
            continue
        posten.append((z.get("kategorie") or "Sonstiges", z.get("skill") or "", b, "Beleg"))
        if not (z.get("datei") or "").strip():
            offen.append("Ohne Belegdatei: %s %s %s" % (z.get("datum", ""), z.get("aussteller", ""), euro(b)))

    belegt = {beleg_schluessel(z) for z in belege}
    belegt.discard(None)
    for z in kandidaten:
        e = (z.get("entscheidung") or "").strip().lower()
        b = zahl(z.get("betrag"))
        if e == "nein":
            continue
        if b is None:
            offen.append("Kontoauszug ohne lesbaren Betrag: %s %s" % (z.get("datum", ""), z.get("empfaenger", "")))
            continue
        if not (e == "ja" or e.startswith("anteilig")):
            offen.append("Kontoauszug noch nicht entschieden: %s %s" % (z.get("datum", ""), z.get("empfaenger", "")))
            continue
        anteil = 100.0
        if e.startswith("anteilig"):
            m = re.fullmatch(r"anteilig\s+(\d+(?:[.,]\d+)?)\s*%?", e)
            if not m or not 0 <= float(m.group(1).replace(",", ".")) <= 100:
                offen.append("Beruflicher Anteil fehlt oder liegt nicht zwischen 0 und 100 Prozent: %s %s (%s)" % (z.get("datum", ""), z.get("empfaenger", ""), e))
                continue
            anteil = float(m.group(1).replace(",", "."))
        if beleg_schluessel(z, kandidat=True) in belegt:
            if anteil != 100:
                offen.append("Anteil aus Kontoauszug bei vorhandenem Beleg im Fach-Skill anwenden: %s %s (%s Prozent); die Belegsumme bleibt hier eine Rohsumme." % (z.get("datum", ""), z.get("empfaenger", ""), anteil))
            continue
        b = b * anteil / 100
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
