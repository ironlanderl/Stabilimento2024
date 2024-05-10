from servizio import Servizio
import os
import pickle


class Cabina(Servizio):
    tipo = "cabina"

    def __init__(self, codice=None, prezzo_giornata=None):
        super().__init__(codice)
        self.prezzo_giornata = prezzo_giornata

    def _load(self):
        lista_cabine_salvate = []
        if os.path.isfile("dati/servizi.pickle"):
            with open("dati/servizi.pickle", "rb") as f:
                lista_cabine_salvate = pickle.load(f)
        return lista_cabine_salvate

    def _save(self, lista):
        with open("dati/servizi.pickle", "wb") as f:
            pickle.dump(lista, f)

    def get_info_servizio(self):
        info = super().get_info_servizio()
        info["prezzo_giornata"] = self.prezzo_giornata
        info["tipo"] = Cabina.tipo
        return info

    def aggiungi_cabina(self, codice, prezzo_giornata):
        super().aggiungi_servizio(codice)
        self.prezzo_giornata = prezzo_giornata
        lista_servizi_salvata = self._load()
        lista_servizi_salvata.append(self.get_info_servizio())
        self._save(lista_servizi_salvata)

    def rimuovi_servizio(self):
        lista_servizi = self._load()
        for servizio in lista_servizi:
            if servizio["tipo"] == Cabina.tipo and servizio["codice"] == self.codice:
                lista_servizi.remove(servizio)
                break
        self._save(lista_servizi)
        self.codice = None
        self.prezzo_giornata = None
        self.tipo = None

    def ricerca_servizio(self, codice):
        lista_servizi = self._load()
        for servizio in lista_servizi:
            if servizio["tipo"] == Cabina.tipo and servizio["codice"] == codice:
                return self._from_dict(servizio)
        return None

    def _from_dict(self, dizionario):
        return Cabina(dizionario["codice"], dizionario["prezzo_giornata"])
