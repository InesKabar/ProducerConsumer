import threading
import time
import random as rd
import random


class Producteur(threading.Thread):
    def __init__(self, num, bte, lock):
        threading.Thread.__init__(self)
        self.actif = True
        self.num = num
        self.montant = random.randint(0, 1000)
        self.boite = bte
        self.lock = lock

    def log(self, msg):
        print(f'producteur {self.num}: {self.montant, msg}\n')

    def run(self):
        self.log('initialisé')
        while self.actif:
            self.lock.acquire()

            if self.boite.est_vide():
                self.log(f' a introduit {self.num}')
                self.boite.ajouter_val(self.num)
                self.actif = False

            self.lock.release()

            time.sleep(rd.randint(0, 3))
