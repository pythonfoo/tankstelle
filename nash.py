# -*- encoding: utf-8 -*-

"""
Nash-Beispielstrategien
"""

import strategie

class NashLow(strategie.Strategie):
    
    def value(self, runde):
        return 1
        
    def author(self):
        return "John Nash"
        
    def name(self):
        return "Gleichgewicht"


class NashHigh(strategie.Strategie):
    
    def value(self, runde):
        return 100
        
    def author(self):
        return "De Beers"
        
    def name(self):
        return "Das Kartell"