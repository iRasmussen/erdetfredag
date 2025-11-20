#!/usr/bin/env python3
"""
erdetfredag.py
Lille Python-script inspireret af erdetfredag.dk.
Svarer på spørgsmålet: Er det fredag i dag?

Version: 2025.11.20.a
Forfatter: Jens Rasmussen (JENR)

Struktur:
- Først importerer vi nødvendige moduler.
- Dernæst definerer vi de funktioner, vi skal bruge.
- Til sidst kalder vi funktionerne i main(), når scriptet køres direkte.
"""

import datetime

def hent_dagens_dato() -> datetime.date:
    """Returnér dagens dato som et date-objekt."""
    return datetime.date.today()

def er_det_fredag(dato: datetime.date) -> bool:
    """Returnér True hvis datoen er en fredag, ellers False."""
    # weekday(): mandag=0, tirsdag=1, ..., søndag=6
    return dato.weekday() == 4  # 4 svarer til fredag

def dansk_ugedag(dato: datetime.date) -> str:
    """Returnér ugedagen på dansk for en given dato."""
    ugedage = [
        "mandag",
        "tirsdag",
        "onsdag",
        "torsdag",
        "fredag",
        "lørdag",
        "søndag",
    ]
    return ugedage[dato.weekday()]

def main() -> None:
    """Kør den simple fredagstjekker."""
    idag = hent_dagens_dato()
    ugedag = dansk_ugedag(idag)

    # Lille "header" med dato og ugedag
    print("-" * 40)
    print("Er det fredag i dag?")
    print(f"Dagens dato er {idag.isoformat()} ({ugedag}).")
    print("-" * 40)

    if er_det_fredag(idag):
        print("Ja, det er fredag!")
    else:
        print(f"Nej, det er {ugedag}.")

    print("-" * 40)


# Her afgør vi, om scriptet køres direkte (fx `python3 erdetfredag.py`)
# eller importeres som modul. Funktionen main() kaldes kun, når det
# køres direkte.
if __name__ == "__main__":
    main()
