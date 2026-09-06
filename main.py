import threading

from boite import Boite
from consommateur import Consommateur
from producteur import Producteur


CST_NB_PRODUCERS = 3


lock = threading.Lock()
b = Boite()

cons = Consommateur(b, lock)
prods = []

cons.start()

for i in range(CST_NB_PRODUCERS):
    prods.append(Producteur(i + 1, b, lock))
    prods[i].start()

cons.join()

for i in range(CST_NB_PRODUCERS):
    prods[i].join()
