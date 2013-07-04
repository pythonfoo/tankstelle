# -*- encoding: utf-8 -*-

"""
Dieses Modul enthält das Interface für eine einzelne Tankstellenstrategie.

Beispiele sind in nash.py zu finden.
"""

class Strategie:
    
    def value(self, runde):
        """Der Wert, den wir in Runde n als Preis nutzen."""
        return 0
        
    def otherValue(self, runde, value):
        """Der Wert, den der Gegner in der aktuellen Runde gewählt hat."""

    def author(self):
        """Der Name des Autors (für die Ausgabe)."""
        return None
        
    def name(self):
        """Der Name der Strategie (für die Ausgabe)."""
        return None





