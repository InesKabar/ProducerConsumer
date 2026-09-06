import threading


class Consommateur(threading.Thread):
    def __init__(self, bte, lock):
        threading.Thread.__init__(self)
        self.actif = True
        self.boite = bte
        self.nb_msg_lus = 0
        self.lock = lock

    def log(self, msg):
        print(f'Admin : {msg}\n')

    def run(self):
        self.log('initialisé')

        while self.actif:
            self.lock.acquire()

            if self.boite.est_pleine():
                val = self.boite.retirer_val()
                self.log(f" j'ai retire {val}")
                self.nb_msg_lus += 1

                if self.nb_msg_lus == 3:
                    self.actif = False

            self.lock.release()
