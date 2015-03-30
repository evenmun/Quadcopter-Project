
from airtravle import *;



f = Flight("SV123",Aircraft("G-EUPT", "Airbus-A319", num_row=22, num_seats_per_row= 6));

print f.number();
print f.aircraft_model()