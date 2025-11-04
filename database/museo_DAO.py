from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self,id, nome, tipologia):
        self._id=id
        self._nome=nome
        self._tipologia=tipologia
    #controllare
        pass

    # TODO  (usare metodi setter e getter, scritto io)
