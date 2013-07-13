# tankstelle #

Das Tankstellen-Dilemma.

Zwei Tankstellen an einer stark befahrenen Straße konkurrieren um die Kunden. Jeden Morgen bestimmen beide Tankstellen einen für den Tag gültigen Preis, ohne den Preis der jeweils anderen Tankstelle zu kennen. Dieser Preis wird morgens festgelegt und kann nicht mehr verändert werden für diesen Tag (das verbietet das Kartellamt). Auch Absprachen sind nicht möglich (Kartellamt!). Die Kunden sind natürlich gute Kapitalisten und gehen zur günstigsten Tankstelle. Haben die Tankstellen den gleichen Preis, so verteilen sich die Kunden exakt halb/halb.

Jeder Tankstellenbetreiber möchte nun natürlich so viel Gewinn wie möglich machen. Aber welchen Preis sollte er dazu wählen?

Das Tankstellen Dilemma ist deshalb ein Dilemma, weil jeder der beiden Tankstellenbetreiber nicht weiß welchen Preis der jeweils andere an diesen Tag festlegen wird. Er kann zwar sichergehen zumindestens nie zu verlieren, indem er durchgehend den niedrigsten Preis (1ct) benutzt, doch so macht er sehr wenig Gewinn. Was im Widerspruch zum Ziel des Maximalen Gewinns steht. Außerdem weiß er nur die Preise vom letzten Tag und hat keine Möglichkeit herrauszufinden, welchen Preis sein Konkurent benutzen wird. Das Tankstellen Dilemma ist eine Abwandlung des Gefangenen Dilemmas, welches von John F. Nash aufgestellt wurde. Bei einen unkooperativen Verhalten der Kontrahenten wird sich früher ein Nash Gleichgewicht am niedrigsten Wert einpendeln.


## Ausführen ##

Einfach `tankstelle.py` starten


## Bearbeiten ##


Jede Strategie muss das Interface aus `strategie.py` implementieren, sonst kommt es zu Aufruf-Fehlern. Um eine Strategie in die Arena zu schicken, muss die neu geschriebene Klasse außerdem in die Liste aller Strategien in `strategien.py` eingetragen werden.

