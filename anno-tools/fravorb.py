#!/usr/bin/env python3
"""Paketvorbereitung fuer `fra/lsg1910mod` — siehe `annovorb.py`.

Der Rumpf ist seit dem italienischen Durchgang gemeinsam; dieses Skript
ist der franzoesische Einstieg und haelt die Ausgabe fest, damit ein
vergessenes `ANNO_EDITION` hier auffliegt statt lautlos das deutsche
Verzeichnis zu lesen. Aufruf unveraendert:

    fravorb.py <buchNr> <kapitel> [<kapitel> ...] --scratch <verzeichnis>
"""
import annovorb

if __name__ == '__main__':
    annovorb.main('fra/lsg1910mod')
