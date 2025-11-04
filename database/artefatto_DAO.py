from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self,id,nome,tipologia,epoca,id_museo):
        self._id=id
        self._nome=nome
        self._tipologia=tipologia
        self._epoca=epoca
        self._id_museo=id_museo
#controllare
        pass

    # TODO  fare metodi setter e getter(scritto io)