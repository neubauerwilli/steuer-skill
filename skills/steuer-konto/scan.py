#!/usr/bin/env python3
"""Kontoauszug nach steuerlich relevanten Ausgaben durchsuchen.

Liest einen CSV-Export (Semikolon oder Komma), erkennt die Spalten selbst und
schreibt Treffer aus regeln.json nach kandidaten.csv. Nur Standardbibliothek.

    python3 scan.py kontoauszug.csv --out steuer/2025/kandidaten.csv
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import OrderedDict

HIER = os.path.dirname(os.path.abspath(__file__))

SPALTEN = {
    "datum": ["datum", "buchungstag", "buchungsdatum", "valuta", "wertstellung", "date", "buchungstag/valuta"],
    "empfaenger": ["empfaenger", "empfänger", "zahlungsempfänger", "zahlungsempfaenger", "name zahlungsbeteiligter",
                   "beguenstigter/zahlungspflichtiger", "begünstigter/zahlungspflichtiger", "auftraggeber/empfänger",
                   "partnername", "name", "payee", "gegenkonto name"],
    "verwendungszweck": ["verwendungszweck", "buchungstext", "beschreibung", "zweck", "text", "description", "umsatztext"],
    "betrag": ["betrag", "betrag (eur)", "umsatz", "amount", "betrag in eur", "soll/haben"],
}


def finde_spalten(kopf):
    normal = [k.strip().lower().replace("﻿", "") for k in kopf]
    treffer = {}
    for feld, namen in SPALTEN.items():
        for i, k in enumerate(normal):
            if k in namen:
                treffer[feld] = i
                break
    fehlt = [f for f in ("datum", "betrag") if f not in treffer]
    if fehlt:
        sys.exit("Spalten nicht erkannt: %s. Gefunden: %s" % (", ".join(fehlt), ", ".join(kopf)))
    return treffer


def zahl(text):
    t = text.strip().replace("EUR", "").replace("€", "").replace(" ", "")
    if not t:
        return None
    if re.search(r",\d{1,2}$", t):
        t = t.replace(".", "").replace(",", ".")
    else:
        t = t.replace(",", "")
    try:
        return float(t)
    except ValueError:
        return None


def passt(muster, text):
    # Kurze Muster wie "o2" oder "kita" nur als ganzes Wort, längere auch in Komposita
    if len(muster) <= 4:
        return re.search(r"(?<!\w)" + re.escape(muster) + r"(?!\w)", text) is not None
    return muster in text


def lies(pfad):
    with open(pfad, encoding="utf-8-sig", errors="replace") as f:
        inhalt = f.read()
    zeilen = [z for z in inhalt.splitlines() if z.strip()]
    trenner = ";" if zeilen and zeilen[0].count(";") >= zeilen[0].count(",") else ","
    reader = list(csv.reader(zeilen, delimiter=trenner))
    # Bankexporte haben oft Kopfzeilen vor der Tabelle: erste Zeile mit Datum und Betrag suchen
    for start, kopf in enumerate(reader):
        try:
            sp = finde_spalten(kopf)
        except SystemExit:
            continue
        return sp, reader[start + 1:]
    finde_spalten(reader[0] if reader else [])

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("auszug")
    ap.add_argument("--out", default="kandidaten.csv")
    ap.add_argument("--regeln", default=os.path.join(HIER, "regeln.json"))
    a = ap.parse_args()

    with open(a.regeln, encoding="utf-8") as f:
        regeln = json.load(f)
    sp, zeilen = lies(a.auszug)

    treffer, summen, ausgaben = [], OrderedDict(), 0
    for z in zeilen:
        def feld(n):
            i = sp.get(n)
            return z[i].strip() if i is not None and i < len(z) else ""
        betrag = zahl(feld("betrag"))
        if betrag is None or betrag >= 0:
            continue
        ausgaben += 1
        text = (feld("empfaenger") + " " + feld("verwendungszweck")).lower()
        for r in regeln:
            if any(passt(m, text) for m in r["muster"]):
                treffer.append([feld("datum"), feld("empfaenger"), feld("verwendungszweck"),
                                ("%.2f" % -betrag).replace(".", ","), r["kategorie"], r["skill"], r["hinweis"], ""])
                summen[r["kategorie"]] = summen.get(r["kategorie"], 0) - betrag
                break

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["datum", "empfaenger", "verwendungszweck", "betrag", "kategorie", "skill", "hinweis", "entscheidung"])
        w.writerows(treffer)

    print("Ausgaben geprüft: %d, Treffer: %d -> %s" % (ausgaben, len(treffer), a.out))
    for k, v in summen.items():
        print("  %-16s %10s EUR" % (k, ("%.2f" % v).replace(".", ",")))
    if not treffer:
        print("Keine Treffer. Muster in regeln.json ergänzen oder Umsätze von Hand durchgehen.")


if __name__ == "__main__":
    main()
