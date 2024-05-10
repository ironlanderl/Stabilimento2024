import datetime
import os
import pickle

class Prenotazione():

    def __init__(self, cliente=None, codice=None, data_ora_inizio=None, data_ora_fine=None, servizio=None):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

    def aggiungi_prenotazione(self, cliente, codice, data_ora_inizio, data_ora_fine, servizio):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

        lista_prenotazioni_salvata = self._load()

        lista_prenotazioni_salvata.append(self.get_info_prenotazione())
        self._save(lista_prenotazioni_salvata)

    def get_info_prenotazione(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "servizio": self.servizio
        }

    def _load(self):
        lista_prenotazioni_salvate = []
        if os.path.isfile("dati/prenotazioni.pickle"):
            with open("dati/prenotazioni.pickle", "rb") as f:
                lista_prenotazioni_salvate = pickle.load(f)
        return lista_prenotazioni_salvate

    def _save(self, lista):
        with open("dati/prenotazioni.pickle", "wb") as f:
            pickle.dump(lista, f)

    def verifica_fine(self):
        return datetime.datetime.now() >= self.data_ora_fine

    def disdici_prenotazione(self):
        lista_prenotazioni_salvate = self._load()
        for prenotazione in lista_prenotazioni_salvate:
            if prenotazione["codice"] == self.codice:
                lista_prenotazioni_salvate.remove(prenotazione)
                break
        self._save(lista_prenotazioni_salvate)
        self.cliente = None
        self.codice = None
        self.data_ora_inizio = None
        self.data_ora_fine = None
        self.servizio = None
        del self