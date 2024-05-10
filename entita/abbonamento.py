class Abbonamento():

    def __init__(self, codice=None, data_inizio=None, data_rilascio=None, data_scadenza=None, stagionale=None):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.stagionale = stagionale