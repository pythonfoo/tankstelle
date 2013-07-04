# -*- encoding: utf-8 -*-

import random

from strategie import Strategie

class DodoA(Strategie):

    lastValue = 0

    def value(self, runde):
        """Der Wert, den wir in Runde n als Preis nutzen."""
        return self.lastValue - 10
        
    def otherValue(self, runde, value):
        """Der Wert, den der Gegner in der aktuellen Runde gewählt hat."""
        self.lastValue = value

    def author(self):
        """Der Name des Autors (für die Ausgabe)."""
        return "dodo"
        
    def name(self):
        """Der Name der Strategie (für die Ausgabe)."""
        return "A"


class DodoB(Strategie):

    lastValue = 0

    def value(self, runde):
        """Der Wert, den wir in Runde n als Preis nutzen."""
        if self.lastValue >= 50:
            return random.choice(range(1,51))
        if self.lastValue >= 25 and self.lastValue < 50:
            return random.choice(range(1,26))
        if self.lastValue < 25:
            return random.choice(range(1,13))
        
    def otherValue(self, runde, value):
        """Der Wert, den der Gegner in der aktuellen Runde gewählt hat."""
        self.lastValue = value

    def author(self):
        """Der Name des Autors (für die Ausgabe)."""
        return "dodo"
        
    def name(self):
        """Der Name der Strategie (für die Ausgabe)."""
        return "B"


class DodoC(Strategie):

    lastValue = 0

    def value(self, runde):
        """Der Wert, den wir in Runde n als Preis nutzen."""
        return runde - 100
        
    def author(self):
        """Der Name des Autors (für die Ausgabe)."""
        return "dodo"
        
    def name(self):
        """Der Name der Strategie (für die Ausgabe)."""
        return "C"


