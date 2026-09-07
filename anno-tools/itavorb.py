#!/usr/bin/env python3
"""Paketvorbereitung fuer `ita/riv1927mod` — siehe `annovorb.py`.

    itavorb.py <buchNr> <kapitel> [<kapitel> ...] --scratch <verzeichnis>

Setzt `ANNO_EDITION=ita/riv1927mod` voraus und liest
`PROMPT_BAUSTEIN_IT.md`.
"""
import annovorb

if __name__ == '__main__':
    annovorb.main('ita/riv1927mod')
