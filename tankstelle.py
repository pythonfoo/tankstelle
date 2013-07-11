# -*- encoding: utf-8 -*-

RUNDEN = 100
KUNDEN = 5000

AUSGABE = False


def tankstellenArena(strategien):
    """Erwartet eine Liste von Strategiefunktionen, die alle gegeineinander ausgewertet werden.
    Ausgabe ist der GRAND WINNER!
    """

    wins = {s: 0 for s in strategien}

    for strategieA in strategien:
        for strategieB in strategien:
            winA, winB = tankstellenSpiel(strategieA, strategieB)
            wins[strategieA] += winA
            wins[strategieB] += winB

    rangfolge = sorted(wins, key=lambda k: wins[k], reverse=True)
    maximal_win = float(RUNDEN * KUNDEN * 100 * (len(strategien) - 1))
    # warum ist maximal_win diese Anzahl?
    #   RUNDEN ist die Anzahl der Runden
    #   KUNDEN * 100 ist die maximal Einnahme pro gespielter Runde
    #   jede Strategie spielt gegen jede andere, also gegen len(strategien) - 1
    print "maximal_win", maximal_win
    print "Endstand:"
    for strategie in rangfolge:
        print "  %20s -> %10d (%2.1f)   (von: %s)" % (strategie.name(), wins[strategie], wins[strategie] / maximal_win * 100, strategie.author())


def tankstellenSpiel(strategieA, strategieB):
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
        priceA = strategieA.value(runde)
        priceB = strategieB.value(runde)
        
        strategieA.otherValue(runde, priceB)
        strategieB.otherValue(runde, priceA)
        
        roundWinA, roundWinB = tankstellenRunde(priceA, priceB)
        
        winA, winB = winA + roundWinA, winB + roundWinB
        
    if AUSGABE:
        print "Spiel:\n  %20s -> %8d\n  %20s -> %8d" % (strategieA.name(), winA, strategieB.name(), winB)
        
    return winA, winB



def tankstellenRunde(priceA, priceB):
    """
    Wertet eine Runde des Tankstellenspiels aus und gibt die Einnahmen zurück.
    Die Strategien sind dabei Integerwerte, die die erwarteten Einnahmen angeben.
    Rückgabewert ist die Einnahme pro Spieler nach o.g. Regeln.
    """

    if priceA is None and priceB is None:
        return 0, 0
    if priceA is None:
        return 0, priceB * KUNDEN
    if priceB is None:
        return priceA * KUNDEN, 0

    if priceA < priceB:
        return priceA * KUNDEN, 0
    elif priceB < priceA:
        return 0, priceB * KUNDEN
    else:
        totalWin = priceA * KUNDEN
        return totalWin / 2, totalWin / 2


def main():
    import strategien
    tankstellenArena(strategien.allStrategies)
    
    
if __name__ == "__main__":
    main()