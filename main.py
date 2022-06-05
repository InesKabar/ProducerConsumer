import threading


class Caissier:
    def __init__(self, id, nom):
        self.nom = nom
        self.id = Caisse(self.id)
    def Retirer(self, montantRetirer):
        self.montantRetirer = montantRetirer


    def Ajouter(self, montantAjouter):
        self.montantAjouter = montantAjouter



class Proprietaire:
    def __init__(self, nom):
        self.nom = nom
        self.id = 0





class Caisse:
    def __init__(self, id,montant):
        self.nbcaisse = 5
        self.id = id
        self.montant = montant
        self.montantAjouter = Caissier(self.montant) + self.montant
        self.montantRetirer = Caissier(self.montant) - self.montant
        self.montant = self.montant + self.montantAjouter - self.montantRetirer




#if __name__ == '__main__':


#from boite import Boite #caisse
#from consommateur import  Consommateur #admin
#from producteur import Producteur #caissier
#from threading import Lock

#CST_NB_PRODUCERS = 3

#lock = Lock()
#b = Boite()



#cons = Consommateur(b, lock)
#prods = []

#cons.start()
#for i in range(CST_NB_PRODUCERS):
#    prods.append(Producteur(i+1, b, lock))
#    prods[i].start()
