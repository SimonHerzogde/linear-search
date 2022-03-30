""" ************************************************
Lineare Suche
************************************************"""
# der Import der Funktion randrange() aus dem Modul random
from random import randrange
# die maximale Anzahl der Werte
anzahl = 1000
# eine leere Liste für die Werte
werte = []
# für die Suche
suchen = 0
print("Lineare Suche")
# die Liste füllen, benutzt werden zufällige Zahlen bis 200
durchlauf = 1
while durchlauf <= anzahl:
    werte.append(randrange(1, 201))
    durchlauf = durchlauf + 1
# zur Kontrolle ausgeben
print("Die Werte sind: ")
for wert in werte:
    print(wert, end = " ")
print()
# Abfrage des Suchkriteriums
kriterium = int(input("Wonach soll gesucht werden? "))
# und jetzt suchen, bis das Ende erreicht wurde oder die Zahl
# gefunden wurde
"""
Positionen werden in einem Array gesammelt und die Werte dann ausgegeben

"""
# Leeres Array für die Positionen
positionen = []

# while-Schleife in jedem Fall bis zum Ende laufen lassen
while suchen < anzahl:
    if werte[suchen] == kriterium:
        # Position in Array anhängen und dabei +1, da index/suchen bei 0 beginnt
        positionen.append(suchen + 1)
        # Schleifenvariable erhöhen
        suchen += 1
    else:
        suchen += 1

# wenn der Wert gefunden wurde, ist die Liste positionen nicht leer/0 und so wird Treffernachricht ausgegeben
if len(positionen) != 0:
    # kleine kosmetische Anpassung, dass bei mehreren Treffern der Plural von Positionen genutzt wird
    # könnte man noch schöner mit einer entsprechenden Funktion lösen um redundanten Code zu vermeiden
    if len(positionen) == 1:
        print("Der Wert", kriterium, "befindet sich an der Position", end=" ")
    else:
        print("Der Wert", kriterium, "befindet sich an den Positionen", end=" ")
    #for-Schleife die durch positionen itteriert und diese ausgibt
    for position in positionen:
        print(position, end=" ")
else:
    print("Der Wert", kriterium, "wurde nicht gefunden.")
print()
