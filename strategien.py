# -*- encoding: utf-8 -*-

"""
Dieses Modul enthält die KOMPLETTE LISTE aller registrierten Strategien
Um eine Strategie hinzuzufügen, muss die Strategieklasse alle Methoden von
`Strategy` implementieren UND eine Instanz muss in die Liste der Strategien (hier
am unteren Ende) hinzugefügt werden.
"""

import nash
import dodoTankstelle


allStrategies = [nash.NashLow(), nash.NashHigh(), dodoTankstelle.DodoA(), dodoTankstelle.DodoB(), dodoTankstelle.DodoC()]

