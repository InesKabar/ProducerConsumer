import threading
class Boite:
    def __init__(self):
        self.pleine = False
        self.valeur = None


    def est_vide(self):
        #with self.lock:
            return not self.pleine

    def est_pleine(self):
        #with self.lock:
            return self.pleine

    def ajouter_val(self, val):
        #with self.lock:
            if not self.est_pleine():
                self.valeur = val
                self.pleine = True

    def retirer_val(self):
        #with self.lock:
            if self.est_pleine():
                self.pleine = False
                return self.valeur