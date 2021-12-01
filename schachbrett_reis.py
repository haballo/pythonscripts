import math

summe = 0
last = 70
gewicht_reiskorn = 0.02 /1000 / 1000    # Ein Reiskorn ist 0.02g schwer, oder 0.00000002t

for feld in range(64):
    anzahl_reiskoerner = 2**feld
    summe = summe + anzahl_reiskoerner
    gewicht = summe * gewicht_reiskorn
    wagon = math.ceil(gewicht / last)
    print ("Feld {} hat {:,} Reiskörner, insgesammt sind es {:,} Reiskörner. Sie sind {:4,.0f}t schwer. Es braucht {:4,.0f} Wagons.".format(feld+1,anzahl_reiskoerner,summe,gewicht,wagon))