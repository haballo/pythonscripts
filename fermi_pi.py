import random
import time

start = time.time()      #Ein Timer wird gestartet (Er misst in Sekunden)
        
pi = 3.1415926535
anzahl_schaetzungen = 1000000000      #Anzahl schüsse

def pi_schaetzen():                                    #hier wird eine Fuktion definiert(pi_schaetzen)
    treffer_kreis = 0                                  #
    for i in range(anzahl_schaetzungen):               #
        x = random.uniform(-1.0, 1.0)                  #hier wird ein Punkt zwischen x/y -1 und +1 generiert
        y = random.uniform(-1.0, 1.0)                  #
        if (x**2 + y**2) <= 1.0:                       #Es wird ein Treffer im Kreis dazu gezählt,
            treffer_kreis += 1                         #wenn y**2 + x**2 kleiner als 1 oder genau 1 ist. 
    return 4 * treffer_kreis / anzahl_schaetzungen     #Die Anzahl der Kreistreffer werden mit 4 multipliziert

#und dann durch die Ahnzahl Schüsse geteilt(gibt circa Pi)

pi_resultat = (pi_schaetzen() + pi_schaetzen() + pi_schaetzen())/3.0

#Die Funktion wird 3mal ausgeführt und dann durch 3 geteilt(ergibt denn Durchschnitt)
    
print("{} und pi ist {}".format(pi_resultat, pi)) #Dieser Befehl schreibt dann das Ergebnis mit Pi verglichen auf

end = time.time()            #Timer wird gestoppt

print("Es dauerte {:.3f}s".format(end - start)) #Zeit wird aufgeschrieben