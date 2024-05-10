import os
import pickle
from datetime import datetime

class Assegnamento:

    def __init__(self, cliente=None, codice=None, data_ora_inizio=None, data_ora_fine=None, servizio=None):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

    def aggiungi_assegnamento(self, cliente, codice, data_ora_inizio, data_ora_fine, servizio):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

        lista_assegnamenti_salvate = self._load()

        lista_assegnamenti_salvate.append(self.get_info_assegnamento())
        self._save(lista_assegnamenti_salvate)

    def get_info_assegnamento(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "servizio": self.servizio
        }

    def _load(self):
        lista_assegnamenti_salvate = []
        if os.path.isfile("dati/assegnamenti.pickle"):
            with open("dati/assegnamenti.pickle", "rb") as f:
                lista_assegnamenti_salvate = pickle.load(f)
        return lista_assegnamenti_salvate

    def _save(self, lista):
        with open("dati/assegnamenti.pickle", "wb") as f:
            pickle.dump(lista, f)

    def verifica_fine(self):
        return datetime.now() >= self.data_ora_fine

    def rimuovi_assegnamento(self):
        lista_assegnamenti_salvate = self._load()
        for assegnamento in lista_assegnamenti_salvate:
            if assegnamento["codice"] == self.codice:
                lista_assegnamenti_salvate.remove(assegnamento)
                break
        self._save(lista_assegnamenti_salvate)
        self.cliente = None
        self.codice = None
        self.data_ora_inizio = None
        self.data_ora_fine = None
        self.servizio = None
        del self
