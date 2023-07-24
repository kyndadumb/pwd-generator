# Passwortgenerator

## Benutzung
Aufruf: ``python main.py --l [Länge] --u [Benutzername] [Benutzername2] [Benutzername3] ...``

- erstellt eine *credentials.txt* in der Form wie im Beispiel
- ist keine Länge gegeben, werden automatisch 16 Zeichen verwendet

## Hilfe
Aufruf: ``python main.py --help``

Passwortgenerator

options:
  -h, --help     show this help message and exit
  --l L          Länge des Passworts (Standard: 16)
  --u U [U ...]  Nutzernamen (mindestens einer)