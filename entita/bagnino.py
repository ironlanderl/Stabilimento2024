import os.path
import pickle
from utilizzatore import Utilizzatore


class Bagnino(Utilizzatore):

    def __init__(self, id=None, nome=None, cognome=None, cf=None, indirizzo=None, email=None, telefono=None,
                 datanascita=None, luogonascita=None, licenza=None):
        super().__init__(id, nome, cognome, cf, indirizzo, email, telefono)
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.licenza = licenza

    def _from_dict(self, bagnino_dict):
        return Bagnino(
            bagnino_dict["id"],
            bagnino_dict["nome"],
            bagnino_dict["cognome"],
            bagnino_dict["cf"],
            bagnino_dict["indirizzo"],
            bagnino_dict["email"],
            bagnino_dict["telefono"],
            bagnino_dict["datanascita"],
            bagnino_dict["luogonascita"],
            bagnino_dict["licenza"]
        )

    def aggiungi_bagnino(self, id, nome, cognome, cf, indirizzo, email, telefono, datanascita, luogonascita, licenza):
        super().aggiungi_utilizzatore(id, nome, cognome, cf, indirizzo, email, telefono)
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.licenza = licenza

        lista_bagnini_salvata = self._load()

        lista_bagnini_salvata.append(self.get_info_bagnigno())
        self._save(lista_bagnini_salvata)

    def ricerca_utilizzatore_cf(self, cf):
        lista_bagnini_salvata = self._load()

        for bagnino_dict in lista_bagnini_salvata:
            if bagnino_dict["cf"] == cf:
                return self._from_dict(bagnino_dict)

    def ricerca_utilizzatore_codice(self, codice):
        lista_bagnini_salvata = self._load()

        for bagnino_dict in lista_bagnini_salvata:
            if bagnino_dict["codice"] == codice:
                return self._from_dict(bagnino_dict)

    def ricerca_utilizzatore_nome_cognome(self, nome, cognome):
        lista_bagnini_salvata = self._load()

        for bagnino_dict in lista_bagnini_salvata:
            if bagnino_dict["nome"] == nome and bagnino_dict["cognome"] == cognome:
                return self._from_dict(bagnino_dict)

    def get_info_bagnigno(self):
        info = super().get_info_utilizzatore()
        info["datanascita"] = self.datanascita
        info["lougonascita"] = self.luogonascita
        info["licenza"] = self.licenza

        return info

    def _load(self):
        lista_bagnini_salvata = []
        if os.path.isfile("dati/bagnini.pickle"):
            with open("dati/bagnini.pickle", "rb") as f:
                lista_bagnini_salvata = pickle.load(f)
        return lista_bagnini_salvata

    def _save(self, lista):
        with open("dati/bagnini.pickle", "wb") as f:
            pickle.dump(lista, f)

    def rimuovi_bagnino(self):
        lista_bagnini_salvata = self._load()

        for bagnino_dict in lista_bagnini_salvata:
            if bagnino_dict["id"] == self.id:
                lista_bagnini_salvata.remove(bagnino_dict)
                self._save(lista_bagnini_salvata)
                break

        self._save(lista_bagnini_salvata)
        super().rimuovi_utilizzatore()
        self.datanascita = None
        self.luogonascita = None
        self.licenza = None
        del self
