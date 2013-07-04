# -*- encoding: utf-8 -*-
import random

RUNDEN = 100
KUNDEN = 5000


def strategieJohannes1(runde, letzterGegnerPreis):
    return 100

def generatorA(runde, lastPrice):
    if lastPrice > 10:
        return lastPrice - 10
    elif lastPrice <= 10:
        return 1
def generatorB(runde, lastPrice):
    if lastPrice >= 50:
        return random.choice(range(1,51))
    if lastPrice >= 25 and lastPrice < 50:
        return random.choice(range(1,26))
    if lastPrice < 25:
        return random.choice(range(1,13))
def generatorC(runde, lastPrice):
    return int(100-runde)

def strategieNash(runde, letzterGegnerPreis):
    """Diese Strategie gewinnt immer, aber dafür zum niedrigsten möglichen Wert."""
    return 1


def tankstellenSpiel(strategieAFun, strategieBFun):
    """Spielt das Tankstellenspiel.
    
    Die beiden übergebenen Funktionen enthalten die Strategien der beiden
    Spieler. Sie werden aufgerufen mit zwei Argumenten:
     * der Zahl der aktiven Runde,
     * dem letzten Preis, den der Gegner gewählt hat
    und geben zurück: einen Integer zwischen 1 und 100. Dieser Integer
    gibt den Preis des verkauften Benzins an. Gewinner der Runde ist die
    Strategie, die den niedrigeren Preis angibt, der Gewinn der Runde ist
    die Anzahl der Kunden multipliziert mit dem Preis des Gewinners. Sollten
    die Strategien den gleichen Preis angeben, werden die Einnahmen gerecht
    verteilt.
    """

    lastA, lastB = 0, 0
    winA, winB = 0, 0
    
    for runde in range(RUNDEN):
        strategieA = strategieAFun(runde, lastB)
        strategieB = strategieBFun(runde, lastA)
        
        lastA = strategieA
        lastB = strategieB
        
        roundWinA, roundWinB = tankstellenRunde(strategieA, strategieB)
        
        winA, winB = winA + roundWinA, winB + roundWinB
        
        print("Runde %3d: A: %3d, B: %3d --> Gewinne: %8d, %8d, Stand: %8d, %8d" % (runde, strategieA, strategieB, roundWinA, roundWinB, winA, winB))
        
    if winA > winB:
        print "Gewinner: A mit %d vs. %d" % (winA, winB)
    elif winA < winB:
        print "Gewinner: B mit %d vs. %d" % (winA, winB)
    else:
        print "Gleichstand bei %d" % winA
        
        
        
    return winA, winB



def tankstellenRunde(strategieA, strategieB):
    """
    Wertet eine Runde des Tankstellenspiels aus und gibt die Einnahmen zurück.
    Die Strategien sind dabei Integerwerte zwischen 1 und 100.
    Rückgabewert ist die Einnahme pro Spieler nach o.g. Regeln.
    """

    if strategieA < strategieB:
        return strategieA * KUNDEN, 0
    elif strategieB < strategieA:
        return 0, strategieB * KUNDEN
    else:
        totalWin = strategieA * KUNDEN
        return totalWin / 2, totalWin / 2

def main():
    tankstellenSpiel(generatorA, generatorB)
    
    
if __name__ == "__main__":
    main()